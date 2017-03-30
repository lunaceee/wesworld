from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session)
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Movie, Color, Ensemble, connect_to_db, db

from random import shuffle

import requests

import etsy


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
	"""Show homepage."""

	return render_template('homepage.html')


@app.route('/search')
def search():
	"""Search for list items matching with movie colors from Etsy."""

	movie_name = request.args.get("movie_name")

	movie = Movie.query.filter_by(Movie.name == movie_name).one()

	colors = Color.query.filter_by(Color.movie_id == movie.id).all()

	color_list = []

	for color in colors:
		color_list.append(colors.hexcode)

	top_dict, bottom_dict, shoe_dict, accessory_dict, bag_dict = etsy.get_listing_items(color_list)
	top_img_url, bottom_img_url, shoe_img_url, accessory_img_url, bag_img_url = etsy.get_image_urls(top_dict, bottom_dict, shoe_dict, accessory_dict, bag_dict)
	top_listing, bottom_listing, accessory_listing, shoe_listing, bag_listing = etsy.get_listing_urls(top_dict, bottom_dict, shoe_dict, accessory_dict, bag_dict)


	return render_template('homepage.html',
							top_img_url=top_img_url,
							bottom_img_url=bottom_img_url,
							shoe_img_url=shoe_img_url,
							accessory_img_url=accessory_img_url,
							bag_img_url=bag_img_url,
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