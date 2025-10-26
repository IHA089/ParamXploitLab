import os
import secrets
from PIL import Image
from flask import render_template, flash, redirect, url_for, abort, request, current_app
from flask_login import login_required, current_user
from functools import wraps
from app.extensions import db 
from app.management import bp 
from app.models import Car
from app.forms import CarForm

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.config['UPLOAD_FOLDER'], picture_fn)

    output_size = (800, 600)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

def staff_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_staff:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/inventory')
@login_required
@staff_required
def inventory():
    cars = Car.query.all()
    return render_template('management/view_inventory.html', title='Manage Inventory', cars=cars)

@bp.route('/add_car', methods=['GET', 'POST'])
@login_required
@staff_required
def add_car():
    form = CarForm()
    if form.validate_on_submit():
        
        picture_file = 'default_car.jpg' 
        if form.image.data:
            picture_file = save_picture(form.image.data)
        
        car = Car(
            model=form.model.data, 
            year=form.year.data, 
            price=form.price.data,
            description=form.description.data,
            image_file=picture_file,
            
            engine=form.engine.data,
            zero_to_sixty=form.zero_to_sixty.data,
            range=form.range.data,
            transmission=form.transmission.data,
            color=form.color.data
        )

        db.session.add(car)
        db.session.commit()
        flash('New car has been added!', 'success')
        return redirect(url_for('management.inventory'))
        
    return render_template('management/add_car_form.html', title='Add New Car', form=form)