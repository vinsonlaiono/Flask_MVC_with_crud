from flask import Flask, render_template, redirect, request

from models.models import Hobby
hobby = Hobby()

class Hobbys:
    """Product Controller"""

    def index(app):
        content = {}
        content['hobby']= hobby.retrieveAllHobbies()
        return render_template("product.html", content=content)                     