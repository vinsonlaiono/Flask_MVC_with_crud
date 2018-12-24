from flask import Flask, render_template, redirect, request

from models.models import  User
user = User()

class Index:
    """Index Controller"""

    def index(app):

        users = user.retrieveAllUsers()
        print(users)
        return render_template("welcome.html", users = users)
    
    def add_user(app, newUser):
        print("*"*80)
        print("In controller", newUser)
        user.add(newUser)

        return redirect('/')

    def delete(app, id):
        user.delete(id)
        return redirect('/')