from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash, session)

from flask_debugtoolbar import DebugToolbarExtension

from model import User, Movie, Color, Ensemble, connect_to_db, db

from wtforms import Form, BooleanField, TextField, PasswordField, validators

from passlib.hash import sha256_crypt

import etsy

import random

import re

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/register', methods=["GET", "POST"])
def register_page():
    """Register user."""

    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = sha256_crypt.encrypt((str(request.form.get("password"))))
        email_re = re.search(r".+@.+\..+", email)  # email validation
        username_re = re.search(r"[^@]+", username)

        if not username_re:
            flash("Username can not contain '@' sign.")
            return render_template('register.html')

        if not email_re:
            flash("Please use legal email format.")
            return render_template('register.html')

        if User.query.filter(User.username == username).first():
            flash("That username is already taken, please choose another.")
            return render_template('register.html')
   
        flash("Thanks for registering!")
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        session['logged_in'] = new_user.id

        return redirect('/search')

    else:
        return render_template("register.html")


@app.route('/login')
def show_login_form():
    """Show login form."""
    return render_template('log_in.html')


@app.route('/login', methods=['POST'])
def process_form():
    """Validate user login info."""

    login = request.form.get('login')
    password = request.form.get('password')

    user = User.query.filter((User.email == login) | (User.username == login)).first()

    # if not user or if user is None:
    if not user:
        flash('Username or email not recognized, try again.')
        return render_template('log_in.html')

    elif user.password != password:
        flash('Password is wrong, please log in again')
        return render_template('log_in.html')

    else:
        session['logged_in'] = user.id
        flash('Log in successful!')
        return redirect('/users/' + str(user.id))


@app.route('/logout')
def logout():
    """Log out user."""
    del session['logged_in']
    del session['movie']
    flash("You have been logged out.", "success")

    return redirect("/search")


@app.route('/users/<user_id>')
def show_user_profile(user_id):
    """Show user profile page."""

    user = User.query.filter(User.id == user_id).one()
    email = user.email
    username = user.username

    ensembles = user.ensembles

    return render_template('user_profile.html',
                            email=email,
                            username=username,
                            ensembles=ensembles)


@app.route('/ensembles', methods=['POST'])
def save_ensemble():
    """User save ensembles."""
    top_listing = request.form.get("top_listing")
    bottom_listing = request.form.get("bottom_listing")
    accessory_listing = request.form.get("accessory_listing")
    shoe_listing = request.form.get('shoe_listing')
    bag_listing = request.form.get('bag_listing')
    dress_listing = request.form.get('dress_listing')
    movie_id = request.form.get('movie_id')

    user_id = session['logged_in']
    user = User.query.filter(User.id == user_id).one()

    ensemble = Ensemble.query.filter(Ensemble.top_url == top_listing,
                                     Ensemble.bottom_url == bottom_listing,
                                     Ensemble.accessory_url == accessory_listing,
                                     Ensemble.shoe_url == shoe_listing,
                                     Ensemble.bag_url == bag_listing,
                                     Ensemble.dress_url == dress_listing).first()

    if ensemble:

        ensemble.users.append(user)
        db.session.add(ensemble)
        db.session.commit()
        print "added new User-Ensemble relationship"
    else:
        new_ensemble = Ensemble(top_url=top_listing,
                            bottom_url=bottom_listing,
                            accessory_url=accessory_listing,
                            shoe_url=shoe_listing,
                            bag_url=bag_listing,
                            dress_url=dress_listing,
                            movie_id=movie_id
                            )

        new_ensemble.users.append(user)
        db.session.add(new_ensemble)
        db.session.commit()
        print "added new ensemble to the database"

    return "successfully saved your ensemble"


@app.route('/search')
def search():
    """Search for list items matching with movie colors from Etsy."""
    movie_list = Movie.query.all()

    movie_names = [m.name for m in movie_list]

    if request.args.get("movie_name"):
        movie_name = request.args.get("movie_name")
        movie = Movie.query.filter(Movie.name == movie_name).one()
        session['movie'] = movie.name

    else:
        movie = random.choice(Movie.query.all())
    
    colors = Color.query.filter(Color.movie_id == movie.id).all()

    color_list = []

    for color in colors:
        color_list.append(color.hexcode)

    result_dict = etsy.get_listing_items(color_list)

    
    
    (t_img_url, bo_img_url, s_img_url, a_img_url, 
        b_img_url, d_img_url) = etsy.get_image_urls(result_dict)
    
    (top_listing, bottom_listing, accessory_listing, dress_listing,
        shoe_listing, bag_listing) = etsy.get_listing_urls(result_dict)

    return render_template('homepage.html',
                                logged_in=bool(session.get('logged_in')),
                                chosen_movie=session.get('movie'),
                                movie_names=movie_names,
                                t_img_url=t_img_url,
                                bo_img_url=bo_img_url,
                                s_img_url=s_img_url,
                                a_img_url=a_img_url,
                                b_img_url=b_img_url,
                                d_img_url=d_img_url,
                                top_listing=top_listing,
                                bottom_listing=bottom_listing,
                                accessory_listing=accessory_listing,
                                shoe_listing=shoe_listing,
                                bag_listing=bag_listing,
                                dress_listing=dress_listing,
                                movie_id=movie.id
                            )



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)


    
    app.run(port=5000, host='0.0.0.0')