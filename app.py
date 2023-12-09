"""Flask app for adopt app."""

import os

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Pet, db

from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def index():
    """Routes to homepage"""
    pets = Pet.query.order_by(Pet.name).all()
    return render_template('homepage.html', pets=pets)

@app.get('/')
def show_add_pet_form():
    """Routes to add pet form """

    return render_template('add_pet_form.html')

@app.route('/add', methods=["GET","POST"])
def add_new_pet():
    """Add a pet"""
# name, species, age, photo url, notes

    form = AddPetForm()
    if form.validate_on_submit():
        pet = Pet(
            name = form.name.data,
            species = form.species.data,
            age = form.age.data,
            photo_url = form.photo_url.data or "",
            notes = form.notes.data)

        flash(f"{pet.name} added!")
        return redirect ('/')

    else:
        return render_template("add_pet_form.html", form=form)