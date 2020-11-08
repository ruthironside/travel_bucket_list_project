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

# SHOW
@countries_blueprint.route("/countries/<id>", methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('countries/show.html', country = country)

# EDIT
@countries_blueprint.route("/countries/<id>/edit", methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    city = country_repository.select_all()
    return render_template('countries/edit.html', country = country, cities = cities)

# UPDATE
@countries_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):
    name = request.form['name']
    continent = request.form['continent']
    country = Country(name, continent)
    country_repository.save(country)
    return redirect('/countries')

# DELETE
@countries_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')