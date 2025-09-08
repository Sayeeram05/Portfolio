from flask import Blueprint, render_template

view = Blueprint("view",__name__)

@view.route("/")
def homePage():
    return render_template("home.html")

@view.route("/aboutMe")
def aboutMe():
    return render_template("aboutMe.html")