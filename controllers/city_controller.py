from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

city_blueprint = Blueprint("city", __name__)

@city_blueprint.route("/city")
def cities():
    # cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities = cities)

# NEW
# GET '/tasks/new'
@tasks_blueprint.route("/tasks/new", methods=['GET'])
def new_task():
    users = user_repository.select_all()
    return render_template("tasks/new.html", all_users = users)

# # CREATE
# # POST '/tasks'
# @tasks_blueprint.route("/tasks",  methods=['POST'])
# def create_task():
#     description = request.form['description']
#     user_id     = request.form['user_id']
#     duration    = request.form['duration']
#     completed   = request.form['completed']
#     user        = user_repository.select(user_id)
#     task        = Task(description, user, duration, completed)
#     task_repository.save(task)
#     return redirect('/tasks')


# # SHOW
# # GET '/tasks/<id>'
# @tasks_blueprint.route("/tasks/<id>", methods=['GET'])
# def show_task(id):
#     task = task_repository.select(id)
#     return render_template('tasks/show.html', task = task)

# # EDIT
# # GET '/tasks/<id>/edit'
# @tasks_blueprint.route("/tasks/<id>/edit", methods=['GET'])
# def edit_task(id):
#     task = task_repository.select(id)
#     users = user_repository.select_all()
#     return render_template('tasks/edit.html', task = task, all_users = users)

# # UPDATE
# # PUT '/tasks/<id>'
# @tasks_blueprint.route("/tasks/<id>", methods=['POST'])
# def update_task(id):
#     description = request.form['description']
#     user_id     = request.form['user_id']
#     duration    = request.form['duration']
#     completed   = request.form['completed']
#     user        = user_repository.select(user_id)
#     task        = Task(description, user, duration, completed, id)
#     task_repository.update(task)
#     return redirect('/tasks')

# # DELETE
# # DELETE '/tasks/<id>'
# @tasks_blueprint.route("/tasks/<id>/delete", methods=['POST'])
# def delete_task(id):
#     task_repository.delete(id)
#     return redirect('/tasks')
