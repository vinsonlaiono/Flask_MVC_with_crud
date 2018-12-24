
from flask import Flask, render_template, redirect, request
app = Flask(__name__, template_folder="views")

# Import Controllers
from controllers.hobbys import Hobbys
hobby = Hobbys()
from controllers.index import Index
index = Index()

# Routes
@app.route('/')
def Index(): 
    return index.index()

@app.route('/hobbys')
def hobbysIndex():
    return hobby.index()

@app.route('/add_user', methods=['POST'])
def add_user():
    newUser = {
        'first_name': request.form['fname'],
        'last_name': request.form['lname'],
    }
    return index.add_user(newUser)

@app.route('/delete/<id>')
def delete(id):
    return index.delete(id)

# Run Server
app.run(debug=True)