from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)


# GET '/countries/new'
@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/new.html", countries = countries)

# CREATE
# POST '/countries'
@countries_blueprint.route("/countries",  methods=['POST'])
def new_country():
    name = request.form['name']
    continent = request.form['continent']
    country = Country(name, continent)
    country_repository.save(country)
    return redirect('/countries')