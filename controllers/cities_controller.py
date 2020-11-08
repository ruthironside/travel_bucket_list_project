from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities = cities)

@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    country = country_repository.select_all()
    return render_template("cities/new.html", countries = countries)

# CREATE
@cities_blueprint.route("/cities",  methods=['POST'])
def create_task():
    name = request.form['name']
    country_id     = request.form['country_id']
    visited   = request.form['visited']
    country        = country_repository.select(country_id)
    city        = City(name, country, visited)
    city_repository.save(city)
    return redirect('/cities')


# SHOW
@cities_blueprint.route("/cities/<id>", methods=['GET'])
def show_city(id):
    city = city_repository.select(id)
    return render_template('cities/show.html', city = city)

# EDIT
@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    countries = city_repository.select_all()
    return render_template('cities/edit.html', city = city, countries = countries)

# UPDATE
@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    name = request.form['name']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(name, country, visited)
    city_repository.save(city)
    return redirect('/cities')

# DELETE
@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities')