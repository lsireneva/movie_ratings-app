"""Server for movie ratings app."""

from flask import (Flask, request, redirect, render_template, flash, session, redirect)
from flask_sqlalchemy import SQLAlchemy
from model import Movie, connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """""Homepage Route"""
    return render_template('homepage.html')

@app.route('/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    user = User.query.filter(User.email == email).first()
    if user:
        return 'A user already exists with that email.'
    else:
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit(new_user)

    return redirect('/login-form')

@app.route('/all-movies')
def view_all_movies():
    movies = crud.get_movies()
   
    for movie in movies: 
        print(movie)
    
    return render_template('all_movies.html', movies=movies)

@app.route('/all-users')
def display_all_users(): 
    users = crud.get_users()
    return render_template('all_users.html', users=users)

@app.route('/movie_detail/<id>')
def show_movie_detail(id):
    movie = crud.get_movie_by_id(id)
    print('MOVIE',movie)

    return render_template('movie_detail.html', movie=movie)

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
