from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role')

class Officer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.String(50), nullable=False)
    license_type = db.Column(db.String(50), nullable=False)
    expiration_date = db.Column(db.String(50), nullable=False)
    closest_major_city = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    dps_id = db.Column(db.String(50), nullable=False)
    equipment_inventory = db.Column(db.Text, nullable=False)

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    license_number = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    mailing_address = db.Column(db.String(100), nullable=False)
    point_of_contact = db.Column(db.String(100), nullable=False)

class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employment_type = db.Column(db.String(50), nullable=False)
    license_level = db.Column(db.String(50), nullable=False)
    date_of_job = db.Column(db.String(50), nullable=False)
    hours_from = db.Column(db.String(50), nullable=False)
    hours_to = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    venue_type = db.Column(db.String(50), nullable=False)
    pay_rate_per_hour = db.Column(db.String(50), nullable=False)
    pay_by = db.Column(db.String(100), nullable=False)
    pay_schedule = db.Column(db.String(50), nullable=False)
    job_type = db.Column(db.String(50), nullable=False)
    required_equipment = db.Column(db.Text, nullable=False)
    attire = db.Column(db.Text, nullable=False)
