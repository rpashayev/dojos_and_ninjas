from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/new_ninja')
def show_new_ninja_form():
    all_dojos = Dojo.show_all_dojos()
    return render_template('new_ninja.html', dojos=all_dojos)

@app.route('/add_ninja', methods=['POST'])
def new_ninja():
    Ninja.insert_ninja(request.form)
    return redirect('/dojos')
