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

@app.route('/users', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    user = crud.get_user_by_email(email)
    if user:
        flash(f'{user.email} already exists.')
        # if (email == ) 
    else:
        crud.create_user(email, password)
        flash("Account created! Please log in")

    return redirect('/')

@app.route('/', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = crud.get_user_by_email(email)

    if password == user.password:
         flash("Logged in!")
        
    else: 
         flash("Incorrect password")
    
    return redirect('/')

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

@app.route('/movie_detail/<id>', methods=['GET'])
def show_movie_detail(id):
    movie = crud.get_movie_by_id(id)
    print('MOVIE',movie)
    user_score = request.form.get('score')
    print(user_score)

    return render_template('movie_detail.html', movie=movie)

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
