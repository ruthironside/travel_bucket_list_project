from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    # cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities = cities)

@cities_blueprint.route("/cities/<id>")
def show(id):
    city = city_repository.select(id)
    countries = city_repository.countries(city)
    return render_template("cities/show.html", city=city, countries=countries)



@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template("cities/new.html", all_countries = countries)

