"""Models and database functions for Wes World project"""

from flask_sqlalchemy import SQLAlchemy
import pprint

db = SQLAlchemy()

class Movie(db.Model):
    """Movie names"""
    __tablename__ = "movies"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        """Show info about movie."""

        return "<Movie id={} name={}>".format(self.id, self.name)

    ensembles = db.relationship('Ensemble',
                                backref="movie")

class User(db.Model):
    """User info"""
    __tablename__ = "users"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __repr__(self):
        """Show info about user."""

        return "<User id={} name={} email={} password={}>".format(self.id, 
                                                                  self.username, 
                                                                  self.email, 
                                                                  self.password)


class Color(db.Model):
    """Color hex code info"""
    __tablename__ = "colors"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    hexcode = db.Column(db.String)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))

    def __repr__(self):
        """Show info about color."""

        return "<Color id={} color_name={}>".format(self.id, self.hexcode)

    # Define relationship to Movie
    movie = db.relationship("Movie", backref=db.backref("colors"))


ensemble_user = db.Table('ensemble_user',
    db.Column('ensemble_id', db.Integer, db.ForeignKey('ensembles.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
)


class Ensemble(db.Model):
    """Ensemble info"""
    __tablename__ = "ensembles"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    accessory_url = db.Column(db.String)
    shoe_url = db.Column(db.String)
    top_url = db.Column(db.String)
    bottom_url = db.Column(db.String)
    bag_url = db.Column(db.String)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    # Define relationship to user
    users = db.relationship("User", secondary=ensemble_user, backref=db.backref("ensembles"))

    def __repr__(self):
        """Show info about Ensemble."""

        return "<Color id={} accessory={} shoe={} top={} bottom={} bag={}>".format(
                                                                                    self.id, 
                                                                                    self.accessory_url,
                                                                                    self.shoe_url,
                                                                                    self.top_url,
                                                                                    self.bottom_url,
                                                                                    self.bag_url
                                                                                    )


    

##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///wesworld'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."