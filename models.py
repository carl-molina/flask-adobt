"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pets table"""

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    name = db.Column(
        db.String(50),
        nullable=False,
    )

    species = db.Column(
        db.String(50),
        nullable=False,
    )

    photo_url = db.Column(
        db.String(500),
        nullable=False,
        default='',
    )

    age = db.Column(
        db.String(50),
        # db.CheckConstraint(Pet.age in ["baby", "young", "adult", "senior"]),
        nullable=False,
    )

    notes = db.Column(
        db.Text,
        nullable=False,
        default=''
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )