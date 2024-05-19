from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from models import db, User, Officer, Company, JobPosting, Role
from auth import auth_blueprint
from forms import OfficerForm, CompanyForm, JobPostingForm, UpdateProfileForm, SearchForm
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///security_app.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth_blueprint, url_prefix='/auth')

@app.before_first_request
def create_roles():
    db.create_all()
    if Role.query.count() == 0:
        admin_role = Role(name='Admin')
        user_role = Role(name='User')
        db.session.add(admin_role)
        db.session.add(user_role)
        db.session.commit()

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role.name != 'Admin':
            flash('You do not have permission to access this page.', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm(obj=current_user)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('profile'))
    return render_template('profile.html', form=form)

@app.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/officers', methods=['GET', 'POST'])
@login_required
def officers():
    form = SearchForm()
    if form.validate_on_submit():
        search_query = form.search.data
        officers = Officer.query.filter(
            Officer.first_name.contains(search_query) | 
            Officer.last_name.contains(search_query)
        ).all()
    else:
        officers = Officer.query.all()
    return render_template('officers.html', officers=officers, form=form)

@app.route('/add_officer', methods=['GET', 'POST'])
@login_required
def add_officer():
    form = OfficerForm()
    if form.validate_on_submit():
        new_officer = Officer(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            dob=form.dob.data,
            license_type=form.license_type.data,
            expiration_date=form.expiration_date.data,
            closest_major_city=form.closest_major_city.data,
            address=form.address.data,
            city=form.city.data,
            zip_code=form.zip_code.data,
            email=form.email.data,
            phone=form.phone.data,
            dps_id=form.dps_id.data,
            equipment_inventory=form.equipment_inventory.data
        )
        db.session.add(new_officer)
        db.session.commit()
        flash('Officer added successfully!', 'success')
        return redirect(url_for('officers'))
    return render_template('add_officer.html', form=form)

@app.route('/edit_officer/<int:officer_id>', methods=['GET', 'POST'])
@login_required
def edit_officer(officer_id):
    officer = Officer.query.get_or_404(officer_id)
    form = OfficerForm(obj=officer)
    if form.validate_on_submit():
        officer.first_name = form.first_name.data
        officer.last_name = form.last_name.data
        officer.dob = form.dob.data
        officer.license_type = form.license_type.data
        officer.expiration_date = form.expiration_date.data
        officer.closest_major_city = form.closest_major_city.data
        officer.address = form.address.data
        officer.city = form.city.data
        officer.zip_code = form.zip_code.data
        officer.email = form.email.data
        officer.phone = form.phone.data
        officer.dps_id = form.dps_id.data
        officer.equipment_inventory = form.equipment_inventory.data
        db.session.commit()
        flash('Officer updated successfully!', 'success')
        return redirect(url_for('officers'))
    return render_template('edit_officer.html', form=form)

@app.route('/delete_officer/<int:officer_id>', methods=['POST'])
@login_required
def delete_officer(officer_id):
    officer = Officer.query.get_or_404(officer_id)
    db.session.delete(officer)
    db.session.commit()
    flash('Officer deleted successfully!', 'success')
    return redirect(url_for('officers'))

@app.route('/companies', methods=['GET', 'POST'])
@login_required
def companies():
    form = SearchForm()
    if form.validate_on_submit():
        search_query = form.search.data
        companies = Company.query.filter(
            Company.name.contains(search_query) |
            Company.point_of_contact.contains(search_query)
        ).all()
    else:
        companies = Company.query.all()
    return render_template('companies.html', companies=companies, form=form)

@app.route('/add_company', methods=['GET', 'POST'])
@login_required
def add_company():
    form = CompanyForm()
    if form.validate_on_submit():
        new_company = Company(
            name=form.name.data,
            license_number=form.license_number.data,
            phone=form.phone.data,
            email=form.email.data,
            mailing_address=form.mailing_address.data,
            point_of_contact=form.point_of_contact.data
        )
        db.session.add(new_company)
        db.session.commit()
        flash('Company added successfully!', 'success')
        return redirect(url_for('companies'))
    return render_template('add_company.html', form=form)

@app.route('/edit_company/<int:company_id>', methods=['GET', 'POST'])
@login_required
def edit_company(company_id):
    company = Company.query.get_or_404(company_id)
    form = CompanyForm(obj=company)
    if form.validate_on_submit():
        company.name = form.name.data
        company.license_number = form.license_number.data
        company.phone = form.phone.data
        company.email = form.email.data
        company.mailing_address = form.mailing_address.data
        company.point_of_contact = form.point_of_contact.data
        db.session.commit()
        flash('Company updated successfully!', 'success')
        return redirect(url_for('companies'))
    return render_template('edit_company.html', form=form)

@app.route('/delete_company/<int:company_id>', methods=['POST'])
@login_required
def delete_company(company_id):
    company = Company.query.get_or_404(company_id)
    db.session.delete(company)
    db.session.commit()
    flash('Company deleted successfully!', 'success')
    return redirect(url_for('companies'))

@app.route('/jobs', methods=['GET', 'POST'])
@login_required
def jobs():
    form = SearchForm()
    if form.validate_on_submit():
        search_query = form.search.data
        job_postings = JobPosting.query.filter(
            JobPosting.venue_type.contains(search_query)
        ).all()
    else:
        job_postings = JobPosting.query.all()
    return render_template('jobs.html', job_postings=job_postings, form=form)

@app.route('/add_job', methods=['GET', 'POST'])
@login_required
def add_job():
    form = JobPostingForm()
    if form.validate_on_submit():
        new_job = JobPosting(
            employment_type=form.employment_type.data,
            license_level=form.license_level.data,
            date_of_job=form.date_of_job.data,
            hours_from=form.hours_from.data,
            hours_to=form.hours_to.data,
            street=form.street.data,
            city=form.city.data,
            zip_code=form.zip_code.data,
            venue_type=form.venue_type.data,
            pay_rate_per_hour=form.pay_rate_per_hour.data,
            pay_by=form.pay_by.data,
            pay_schedule=form.pay_schedule.data,
            job_type=form.job_type.data,
            required_equipment=form.required_equipment.data,
            attire=form.attire.data
        )
        db.session.add(new_job)
        db.session.commit()
        flash('Job posting added successfully!', 'success')
        return redirect(url_for('jobs'))
    return render_template('add_job.html', form=form)

@app.route('/edit_job/<int:job_id>', methods=['GET', 'POST'])
@login_required
def edit_job(job_id):
    job = JobPosting.query.get_or_404(job_id)
    form = JobPostingForm(obj=job)
    if form.validate_on_submit():
        job.employment_type = form.employment_type.data
        job.license_level = form.license_level.data
        job.date_of_job = form.date_of_job.data
        job.hours_from = form.hours_from.data
        job.hours_to = form.hours_to.data
        job.street = form.street.data
        job.city = form.city.data
        job.zip_code = form.zip_code.data
        job.venue_type = form.venue_type.data
        job.pay_rate_per_hour = form.pay_rate_per_hour.data
        job.pay_by = form.pay_by.data
        job.pay_schedule = form.pay_schedule.data
        job.job_type = form.job_type.data
        job.required_equipment = form.required_equipment.data
        job.attire = form.attire.data
        db.session.commit()
        flash('Job posting updated successfully!', 'success')
        return redirect(url_for('jobs'))
    return render_template('edit_job.html', form=form)

@app.route('/delete_job/<int:job_id>', methods=['POST'])
@login_required
def delete_job(job_id):
    job = JobPosting.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    flash('Job posting deleted successfully!', 'success')
    return redirect(url_for('jobs'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
