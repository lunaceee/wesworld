from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session)
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Movie, Color, Ensemble, connect_to_db, db

from wtforms import Form, BooleanField, TextField, PasswordField, validators

from passlib.hash import sha256_crypt

import etsy

import random

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


# @app.route('/')
# def show_home_page():
#     """Show an ensemble when user land in the homepage."""

#     return render_template("homepage.html")


class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=20)])
    email = TextField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the <a href="">Terms of Service</a> and Privacy Notice (Last updated Apr 1st, 2017)', [validators.Required()])


@app.route('/register/', methods=["GET", "POST"])
def register_page():
    try:
        form = RegistrationForm(request.form)

        if request.method == "POST" and form.validate():
            username = request.form.get("username")
            email = request.form.get("email")
            password = sha256_crypt.encrypt((str(request.form.get("password"))))
            # c, conn = connection()

            # x = c.execute("SELECT * FROM users WHERE username = (%s)",
            #               (thwart(username)))

            if User.query.filter(User.username == username).first():
                flash("That username is already taken, please choose another.")
                return render_template('register.html', form=form)

            else:
                # c.execute("INSERT INTO users (username, password, email, tracking) VALUES (%s, %s, %s, %s)",
                #           (thwart(username), thwart(password), thwart(email), thwart("/introduction-to-python-programming/")))
                
                # conn.commit()
                flash("Thanks for registering!")
                # c.close()
                # conn.close()
                # gc.collect()

                new_user = User(username=username, email=email, password=password)
                db.session.add(new_user)
                db.session.commit()
                
                session['logged_in'] = True
                session['username'] = username

                return redirect('/')

        return render_template("register.html", form=form)

    except Exception as e:
        return(str(e))



# @app.route('/login', methods=['POST'])
# def process_form():
#     """Validate user login info."""

#     login = request.form.get('login')
#     password = request.form.get('password')

#     user = User.query.filter(User.email == login, User.username == login).first()

#     # if not user or if user is None:
#     if not user:
#         flash('Username or email not recognized, create your account right now.')
#         return render_template('register.html')

#     elif user.password != password:
#         flash('Password is wrong, please log in again')
#         return render_template('login_form.html')
#     else:
#         session['logged_in'] = user.user_id
#         flash('Log in successful!')
#         return redirect('users/' + str(user.user_id))
#     return render_template("homepage.html")


# @app.route('logout')
# def logout():
#     """Log out user."""
#     del session['logged_in']
#     flash("You have been logged out.", "success")

#     return redirect("/")


# @app.route('/user_profile/<username>')
# def show_user_profile(username):
#     """Show user profile page."""
#     return redirect('user_profile' + username)


@app.route('/search')
def search():
    """Search for list items matching with movie colors from Etsy."""

    if request.args.get("movie_name"):
        movie_name = request.args.get("movie_name")
        movie = Movie.query.filter(Movie.name == movie_name).one()

    else:
        movie = random.choice(Movie.query.all())
    
    colors = Color.query.filter(Color.movie_id == movie.id).all()

    color_list = []

    for color in colors:
        color_list.append(color.hexcode)

    result_dict = etsy.get_listing_items(color_list)
    
    (t_img_url, bo_img_url, s_img_url, a_img_url, 
        b_img_url) = etsy.get_image_urls(result_dict)
    
    (top_listing, bottom_listing, accessory_listing, 
        shoe_listing, bag_listing) = etsy.get_listing_urls(result_dict)


    return render_template('homepage.html',
                                t_img_url=t_img_url,
                                bo_img_url=bo_img_url,
                                s_img_url=s_img_url,
                                a_img_url=a_img_url,
                                b_img_url=b_img_url,
                                top_listing=top_listing,
                                bottom_listing=bottom_listing,
                                accessory_listing=accessory_listing,
                                shoe_listing=shoe_listing,
                                bag_listing=bag_listing
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