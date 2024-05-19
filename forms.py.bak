from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class OfficerForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    dob = StringField('Date of Birth', validators=[DataRequired()])
    license_type = SelectField('License Type', choices=[('Level II', 'Level II'), ('Level III', 'Level III'), ('Level IV', 'Level IV')], validators=[DataRequired()])
    expiration_date = StringField('Expiration Date', validators=[DataRequired()])
    closest_major_city = StringField('Closest Major City', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    dps_id = StringField('DPS ID', validators=[DataRequired()])
    equipment_inventory = TextAreaField('Equipment Inventory', validators=[DataRequired()])
    submit = SubmitField('Add Officer')

class CompanyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    license_number = StringField('License Number', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    mailing_address = StringField('Mailing Address', validators=[DataRequired()])
    point_of_contact = StringField('Point of Contact', validators=[DataRequired()])
    submit = SubmitField('Add Company')

class JobPostingForm(FlaskForm):
    employment_type = SelectField('Employment Type', choices=[('Temporary', 'Temporary'), ('Part Time Employee', 'Part Time Employee'), ('Fulltime Employee', 'Fulltime Employee')], validators=[DataRequired()])
    license_level = SelectField('License Level', choices=[('Level II', 'Level II'), ('Level III', 'Level III'), ('Level IV', 'Level IV'), ('PI', 'PI')], validators=[DataRequired()])
    date_of_job = StringField('Date of Job', validators=[DataRequired()])
    hours_from = StringField('Hours From', validators=[DataRequired()])
    hours_to = StringField('Hours To', validators=[DataRequired()])
    street = StringField('Street', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired()])
    venue_type = StringField('Venue Type', validators=[DataRequired()])
    pay_rate_per_hour = StringField('Pay Rate per Hour', validators=[DataRequired()])
    pay_by = StringField('Pay By', validators=[DataRequired()])
    pay_schedule = StringField('Pay Schedule', validators=[DataRequired()])
    job_type = SelectField('Job Type', choices=[('1099', '1099'), ('W2', 'W2')], validators=[DataRequired()])
    required_equipment = TextAreaField('Required Equipment', validators=[DataRequired()])
    attire = TextAreaField('Attire', validators=[DataRequired()])
    submit = SubmitField('Add Job')

class UpdateProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update Profile')

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')
