"""Server for movie ratings app."""

from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


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


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    app.run(host="0.0.0.0", debug=True)
