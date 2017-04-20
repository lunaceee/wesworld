"""Models and database functions for Wes World project"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pprint
import os

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
    # pic = db.Column(db.String)
    password = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    modified_at = db.Column(db.DateTime)

    def __repr__(self):
        """Show info about user."""

        return "<User id={} name={} email={} password={}>".format(self.id, 
                                                                  self.username, 
                                                                  self.email,
                                                                  # self.pic,
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


class EnsembleUser(db.Model):
    """Association table for ensembles and users."""
    __tablename__ = "ensemble_user"

    #id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ensemble_id = db.Column(db.Integer, db.ForeignKey('ensembles.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    points = db.Column(db.Integer, default=0)

    user = db.relationship("User", backref=db.backref("ensemble_associations"))
    ensemble = db.relationship("Ensemble", backref=db.backref("ensemble_associations"))


class Ensemble(db.Model):
    """Ensemble info"""
    __tablename__ = "ensembles"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    top_id = db.Column(db.Integer, db.ForeignKey('tops.id'))
    bottom_id = db.Column(db.Integer, db.ForeignKey('bottoms.id'))
    accessory_id = db.Column(db.Integer, db.ForeignKey('accessories.id'))
    shoe_id = db.Column(db.Integer, db.ForeignKey('shoes.id'))
    bag_id = db.Column(db.Integer, db.ForeignKey('bags.id'))
    dress_id = db.Column(db.Integer, db.ForeignKey('dresses.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    modified_at = db.Column(db.DateTime)

    # Define relationship to user
    users = db.relationship("User", secondary='ensemble_user', backref=db.backref("ensembles"))
    accessory = db.relationship("Accessory", backref=db.backref("ensembles"))
    top = db.relationship("Top", backref=db.backref("ensembles"))
    bottom = db.relationship("Bottom", backref=db.backref("ensembles"))
    dress = db.relationship("Dress", backref=db.backref("ensembles"))
    bag = db.relationship("Bag", backref=db.backref("ensembles"))
    shoe = db.relationship("Shoe", backref=db.backref("ensembles"))

    def __repr__(self):
        """Show info about Ensemble."""

        return "<Ensemble id={}>".format(self.id)
                                                                          

class Accessory(db.Model):
    """Accessory info"""
    __tablename__ = "accessories"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    listing_url = db.Column(db.String)
    img_url = db.Column(db.String)
    color = db.Column(db.Integer, db.ForeignKey('colors.id'))

    def __repr__(self):
        """Show info about accessories."""
        return "<Accessory id={} listing={} image={}>".format(
            self.id,
            self.listing_url,
            self.img_url
            )



class UserAccessory(db.Model):
    """Association table for accessories and users."""
    __tablename__ = "user_accessory"

    accesssory_id = db.Column(db.Integer, db.ForeignKey('accessories.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)


class Top(db.Model):
    """Top info"""
    __tablename__ = "tops"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    listing_url = db.Column(db.String)
    img_url = db.Column(db.String)

    def __repr__(self):
        """Show info about tops."""
        return "<Top id={} listing={} image={}>".format(
            self.id,
            self.listing_url,
            self.img_url
            )

class UserTop(db.Model):
    """Association table for tops and users."""
    __tablename__ = "user_top"

    top_id = db.Column(db.Integer, db.ForeignKey('tops.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

class Bottom(db.Model):
    """Bottom info"""
    __tablename__ = "bottoms"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    listing_url = db.Column(db.String)
    img_url = db.Column(db.String)

    def __repr__(self):
        """Show info about bottoms."""
        return "<Bottom id={} listing={} image={}>".format(
            self.id,
            self.listing_url,
            self.img_url
            )

class UserBottom(db.Model):
    """Association table for bottoms and users."""
    __tablename__ = "user_bottom"

    bottom_id = db.Column(db.Integer, db.ForeignKey('bottoms.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

class Bag(db.Model):
    """Bag info"""
    __tablename__ = "bags"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    listing_url = db.Column(db.String)
    img_url = db.Column(db.String)

    def __repr__(self):
        """Show info about bags."""
        return "<Bag id={} listing={} image={}>".format(
            self.id,
            self.listing_url,
            self.img_url
            )

class UserBag(db.Model):
    """Association table for bags and users."""
    __tablename__ = "user_bag"

    bag_id = db.Column(db.Integer, db.ForeignKey('bags.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

class Dress(db.Model):
    """Accessory info"""

    __tablename__ = "dresses"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    listing_url = db.Column(db.String)
    img_url = db.Column(db.String)

    def __repr__(self):
        """Show info about dresses."""
        return "<Dress id={} listing={} image={}>".format(
            self.id,
            self.listing_url,
            self.img_url
            )

class UserDress(db.Model):
    """Association table for dresses and users."""
    __tablename__ = "user_dress"

    dress_id = db.Column(db.Integer, db.ForeignKey('dresses.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)

class Shoe(db.Model):
    """Shoe info"""
    __tablename__ = "shoes"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    listing_url = db.Column(db.String)
    img_url = db.Column(db.String)

    def __repr__(self):
        """Show info about shoes."""
        return "<Shoe id={} listing={} image={}>".format(
            self.id,
            self.listing_url,
            self.img_url
            )


class UserShoe(db.Model):
    """Association table for shoes and users."""
    __tablename__ = "user_shoe"

    shoe_id = db.Column(db.Integer, db.ForeignKey('shoes.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)


class Cache(db.Model):
    """Cache objects."""

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    key = db.Column(db.String, index=True)
    value = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """Show info about Ensemble."""

        return "<Cache key={}>".format(self.key)

    

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