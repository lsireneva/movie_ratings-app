"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Replace this with your code!
class User (db.Model): 
    """ A User"""
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, 
                        primary_key= True,
                        autoincrement= True,)
    email = db.Column(db.String, nullable = False, unique=True,)
    password = db.Column(db.String, nullable=False,)
    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email} password={self.password}>'


class Rating (db.Model):
    """Ratings of movies"""

    __tablename__="ratings"

    rating_id = db.Column(db.Integer, 
                        primary_key= True,
                        autoincrement= True) 
    score = db.Column (db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    
    movie = db.relationship("Movie", backref="ratings")
    user = db.relationship("User", backref="ratings")

    def __repr__(self):
        return f'<Movie {self.movie_id} score = {self.score} from user {self.user_id}>'


class Movie(db.Model):
    """Information about movies"""
    __tablename__= "movies"

    movie_id = db.Column(db.Integer, 
                        primary_key= True,
                        autoincrement= True,) 
    title = db.Column(db.String, nullable=False,)
    overview = db.Column(db.String, nullable=False,)
    release_date= db.Column(db.DateTime, nullable=False,)
    poster_path = db.Column(db.String,)

    def __repr__(self):
        return f'<Movie {self.movie_id} title = {self.title} date = {self.release_date}>'



def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
