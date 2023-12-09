"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL

class AddPetForm(FlaskForm):
    """Form for adding a pet."""

    # pet, species, photo url, age, notes
    name = StringField("Pet Name",
                       validators=[InputRequired()])
    species = StringField("Species",
                        validators=[InputRequired()])
    photo_url = StringField("Photo URL",
                        validators=[InputRequired(), URL()])
    age = SelectField("Age",
                      choices=[('baby','Baby'),
                               ('young', 'Young'),
                               ('adult','Adult'),
                               ('senior', 'Senior')],
                       validators=[InputRequired()])
    notes = BooleanField("Notes",
                        validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editing pet information."""

    photo_url = StringField("Photo URL",
                        validators=[InputRequired(), URL()])

    notes = BooleanField("Notes",
                        validators=[Optional()])

    available = BooleanField("Available",
                        validators=[Optional()])