from flask import render_template, request, flash, redirect, url_for
from app.main import bp
from app.models import BaseModel
from app.extensions import db

@bp.route('/')
@bp.route('/index')
def index():
    models = BaseModel.query.all()
    
    return render_template('main/index.html', title='Home', models=models)

@bp.route('/about')
def about():
    return render_template('main/about.html', title='About Us')

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    car_inquiry = ""
    if request.method == 'GET':
        car_model = request.args.get('car_model')
        car_year = request.args.get('car_year')
        if car_model and car_year:
            car_inquiry = f"I am inquiring about the {car_year} {car_model}..."
    
    if request.method == 'POST':
        flash('Thank you for your inquiry. We will get back to you soon.', 'success')
        return redirect(url_for('main.index'))
        
    return render_template('main/contact.html', title='Contact', car_inquiry=car_inquiry)