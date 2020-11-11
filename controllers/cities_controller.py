from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities = cities)

#NEW
@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template("cities/new.html", countries=countries)

# CREATE
@cities_blueprint.route("/cities",  methods=['POST'])
def create_city():
    name = request.form['name']
    country_id = request.form['country']
    country = country_repository.select(country_id)
    city = City(name, country)
    city_repository.save(city)
    return redirect('/cities')


# SHOW
@cities_blueprint.route("/cities/<id>", methods=['GET'])
def show_city(id):
    city = city_repository.select(id)
    return render_template('cities/show.html', city=city)

# EDIT
@cities_blueprint.route("/cities/<id>/edit", methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    return render_template('cities/edit.html', city=city)

# UPDATE
@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    visited = request.form["visited"]
    name = request.form["name"]
    city = city_repository.select(id)
    updated_city = City(name, city.country, visited, id)
    city_repository.update(updated_city)
    return redirect('/cities')

# DELETE
@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities')

# Show visited cities
@cities_blueprint.route("/visited", methods=['GET'])
def visited_city():
    cities = city_repository.visited()
    return render_template('cities/index.html', cities=cities)

# Show cities still to visit
@cities_blueprint.route("/stilltosee", methods=['GET'])
def stilltosee_city():
    cities = city_repository.stilltosee()
    return render_template('cities/index.html', cities=cities)