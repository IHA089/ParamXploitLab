from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
# Import from app.extensions, NOT from app
from app.extensions import db, bcrypt 
from app.auth import bp # Import the blueprint
from app.models import User, TestDrive, UserConfiguration
from app.forms import LoginForm, RegistrationForm

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        
        if User.query.count() == 0:
            user.is_staff = True
            flash('First user created as Staff.', 'info')
            
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', title='Register', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('auth.dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
            
    return render_template('auth/login.html', title='Login', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/dashboard')
@login_required
def dashboard():
    test_drives = TestDrive.query.filter_by(user_id=current_user.id).order_by(TestDrive.date_requested.desc()).all()
    
    configurations = UserConfiguration.query.filter_by(user_id=current_user.id).all()
    
    return render_template('auth/dashboard.html', 
                            title='My Dashboard', 
                            test_drives=test_drives, 
                            configurations=configurations) 