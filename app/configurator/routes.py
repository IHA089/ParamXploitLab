from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from app.configurator import bp
from app.extensions import db
from app.models import BaseModel, ExteriorColor, Wheel, Interior, UserConfiguration

@bp.route('/build')
def build_step1_model():
    models = BaseModel.query.all()
    return render_template('configurator/build_step1_model.html', 
                            title='Build Your BMW - Select Model', 
                            models=models)

@bp.route('/build/model/<int:model_id>/color')
def build_step2_color(model_id):
    model = BaseModel.query.get_or_404(model_id)
    colors = model.colors.all() 
    return render_template('configurator/build_step2_color.html', 
                            title='Build Your BMW - Select Color', 
                            model=model, 
                            colors=colors)

@bp.route('/build/model/<int:model_id>/color/<int:color_id>/wheels')
def build_step3_wheel(model_id, color_id):
    model = BaseModel.query.get_or_404(model_id)
    color = ExteriorColor.query.get_or_404(color_id)
    wheels = model.wheels.all()
    
    current_price = model.base_price + color.price
    
    return render_template('configurator/build_step3_wheel.html', 
                            title='Build Your BMW - Select Wheels', 
                            model=model, 
                            color=color, 
                            wheels=wheels,
                            current_price=current_price)

@bp.route('/build/model/<int:model_id>/color/<int:color_id>/wheels/<int:wheel_id>/interior')
def build_step4_interior(model_id, color_id, wheel_id):
    model = BaseModel.query.get_or_404(model_id)
    color = ExteriorColor.query.get_or_404(color_id)
    wheel = Wheel.query.get_or_404(wheel_id)
    interiors = model.interiors.all()
    
    current_price = model.base_price + color.price + wheel.price
    
    return render_template('configurator/build_step4_interior.html', 
                            title='Build Your BMW - Select Interior', 
                            model=model, 
                            color=color, 
                            wheel=wheel, 
                            interiors=interiors,
                            current_price=current_price)

@bp.route('/build/model/<int:model_id>/color/<int:color_id>/wheels/<int:wheel_id>/interior/<int:interior_id>/review')
def build_step5_review(model_id, color_id, wheel_id, interior_id):
    model = BaseModel.query.get_or_404(model_id)
    color = ExteriorColor.query.get_or_404(color_id)
    wheel = Wheel.query.get_or_404(wheel_id)
    interior = Interior.query.get_or_404(interior_id)
    
    total_price = model.base_price + color.price + wheel.price + interior.price
    
    return render_template('configurator/build_step5_review.html', 
                            title='Build Your BMW - Review', 
                            model=model, 
                            color=color, 
                            wheel=wheel, 
                            interior=interior,
                            total_price=total_price)

@bp.route('/build/save', methods=['POST'])
@login_required
def save_configuration():
    model_id = request.form.get('model_id')
    color_id = request.form.get('color_id')
    wheel_id = request.form.get('wheel_id')
    interior_id = request.form.get('interior_id')
    total_price = request.form.get('total_price')

    if not all([model_id, color_id, wheel_id, interior_id, total_price]):
        flash('Error saving configuration. Invalid data.', 'danger')
        return redirect(url_for('configurator.build_step1_model'))

    config = UserConfiguration(
        user_id=current_user.id,
        model_id=model_id,
        color_id=color_id,
        wheel_id=wheel_id,
        interior_id=interior_id,
        total_price=total_price
    )
    db.session.add(config)
    db.session.commit()
    
    flash('Your configuration has been saved to your dashboard!', 'success')
    return redirect(url_for('auth.dashboard'))