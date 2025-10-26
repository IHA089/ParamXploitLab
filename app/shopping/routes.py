from flask import render_template, abort, flash, redirect, url_for, request
from flask_login import login_required, current_user  
from app.shopping import bp
from app.models import Car, TestDrive 
from app.extensions import db           
from app.forms import TestDriveForm

@bp.route('/')
def car_list():
    cars = Car.query.all()
    return render_template('shopping/car_list.html', title='All Cars', cars=cars)

@bp.route('/<int:car_id>')
def car_detail(car_id):
    car = Car.query.get_or_404(car_id)
    return render_template('shopping/car_detail.html', title=car.model, car=car)

@bp.route('/book-test-drive/<int:car_id>', methods=['GET', 'POST'])
@login_required  
def book_test_drive(car_id):
    car = Car.query.get_or_404(car_id)
    form = TestDriveForm()
    
    if form.validate_on_submit():
        test_drive = TestDrive(
            date_requested=form.preferred_date.data,
            status='Pending',
            user_id=current_user.id,
            car_id=car.id
        )
        db.session.add(test_drive)
        db.session.commit()
        
        flash('Your test drive has been requested! Our team will contact you shortly.', 'success')
        return redirect(url_for('auth.dashboard'))
        
    return render_template('shopping/book_test_drive.html', title='Book Test Drive', form=form, car=car)