from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

country_blueprint = Blueprint("country", __name__)

@country_blueprint.route("/countries")
def countries():
    # countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)