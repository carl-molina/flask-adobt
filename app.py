"""Flask app for adopt app."""

import os

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Pet, db

from forms import AddPetForm, EditPetForm

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
            notes = form.notes.data,
            available= True)

        flash(f"{pet.name} added!")

        db.session.add(pet)
        db.session.commit()

        return redirect ('/')

    else:
        return render_template("add_pet_form.html", form=form)


@app.route('/<int:pet_id>', methods=["GET","POST"])
def show_pet_info_and_edit_pet_info(pet_id):
    """Show pet info and form for edit pet info"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data


        flash(f"Pet {pet.id} successfully edited!")

        db.session.commit()

        return redirect('/')

    else:
        return render_template("display_edit_form.html", form=form)

# create a link on the homepage to edit pet info
# create each pet a hyperlink on homepage