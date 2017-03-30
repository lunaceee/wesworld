"""Utility file to seed wesworld database from seed_data/"""

from sqlalchemy import func
from model import Movie, User, Color, Ensemble, connect_to_db, db
from server import app
import datetime



movies = [
  {
    'name': 'The Grand Budapest Hotel',
    'colors': [
        '5B1A18',
        '7294D4',
        'C6CDF7',
        'D67236',
        'D8A499',
        'E6A0C4',
        'F1BB7B',
        'FD6467'
    ],
  },
  {
    'name': 'Bottle Rocket',
    'colors': [
		'0C1707',
		'1E1E1E',
		'273046',
		'354823',
		'3F5151',
		'4E2A1E',
		'550307',
		'5F5647',
		'9B110E',
		'A42820',
		'CB2314',
		'FAD510'
    ],
  },
  {
    'name': 'Castello Cavalcanti',
    'colors': [
		'02401B',
		'81A88D',
		'972D15',
		'A2A475',
		'D8B70A',
    ],
  },
  {
    'name': 'Fantastic Mr. Fox',
    'colors': [
		'46ACC8',
		'B40F20',
		'DD8D29',
		'E2D200',
		'E58601',
    ],
  },
  {
    'name': 'Hotel Chevalier',
    'colors': [
		'446455',
		'C7B19C',
		'D3DDDC',
		'FDD262'
    ],
  },
  {
    'name': 'Moonrise Kingdom',
    'colors': [
		'24281A',
		'29211F',
		'798E87',
		'85D4E3',
		'9C964A',
		'C27D38',
		'CCC591',
		'CDC08C',
		'CEAB07',
		'D5D5D3',
		'F3DF6C',
		'F4B5BD',
		'FAD77B'
    ],
  },
  {
    'name': 'Rushmore',
    'colors': [
		'0B775E',
		'35274A',
		'E1BD6D',
		'EABE94',
		'F2300F'
    ],
  },
  {
    'name': 'The Darjeeling Limited',
    'colors': [
		'000000',
		'00A08A',
		'046C9A',
		'5BBCD6',
		'ABDDDE',
		'D69C4E',
		'ECCBAE',
		'F2AD00',
		'F98400',
		'FF0000'
    ],
  },
  {
    'name': 'The Life Aquatic with Steve Zissou',
    'colors': [
		'3B9AB2',
		'78B7C5',
		'E1AF00',
		'EBCC2A',
		'F21A00'
    ],
  },
  {
    'name': 'The Royal Tenenbaums',
    'colors': [
		'74A089',
		'899DA4',
		'9A8822',
		'C93312',
		'DC863B',
		'F5CDB4',
		'F8AFA8',
		'FAEFD1',
		'FDDDA0'
    ],
  }
]


def load_users():
    """Load users from u.user into database."""

    print "Users"

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    User.query.delete()

    # Read user_data file and insert data
    for row in open("seed_data/user_data.txt"):
        row = row.rstrip()
        user_id, name, email, password = row.split("|")

        user = User(
                    name=name,
                    email=email,
                    password=password
                    )

        # We need to add to the session or it won't ever be stored
        db.session.add(user)

    # Once we're done, we should commit our work
    db.session.commit()



def load_movies_and_colors():
    """Load movies from movie_data into database."""
    print "Movies and Colors"

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate movies
    Movie.query.delete()
    Color.query.delete()

    for movie_dict in movies:
    	movie = Movie(
                      name=movie_dict['name'],
                     )
    	db.session.add(movie)
    	db.session.commit()
    	for hexcode in movie_dict['colors']:
    		color = Color(
                       hexcode=hexcode,
                       movie_id=movie.id
                       )
    		db.session.add(color)

    db.session.commit()



if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_users()
    load_movies_and_colors()
