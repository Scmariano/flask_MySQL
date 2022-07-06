from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    users = User.get_all()
    return render_template("read.html", users = users)

@app.route('/new/user')
def new():
    return render_template("create.html")

@app.route('/create/user', methods=['POST'])
def create_user():
    User.save(request.form)
    return redirect('/users')
