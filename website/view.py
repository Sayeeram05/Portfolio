from flask import Blueprint, render_template, views

view = Blueprint("view",__name__)

@view.route("/")
def homePage():
    return render_template("home.html")

@view.route("/aboutMe")
def aboutMe():
    return render_template("aboutMe.html")

@view.route("/skill")
def skill():
    return render_template("skill.html")

@view.route("/projects")
def projects():
    return render_template("projects.html")