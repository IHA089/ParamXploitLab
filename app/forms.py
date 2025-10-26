from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired
# Import the model
from wtforms.fields import DateField
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already in use. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class CarForm(FlaskForm):
    model = StringField('Model', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    
    # --- ADD THESE NEW FIELDS ---
    engine = StringField('Engine Type (e.g., "Electric Motor" or "3.0L V6")', validators=[DataRequired()])
    zero_to_sixty = FloatField('0-60 MPH (e.g., 3.5)', validators=[DataRequired()])
    range = StringField('Range (e.g., "300 Miles" or "N/A")', validators=[DataRequired()])
    transmission = StringField('Transmission', validators=[DataRequired()], default='Automatic')
    color = StringField('Color (e.g., "Metallic Black")', validators=[DataRequired()])
    
    image = FileField('Car Image', validators=[
        FileRequired(), 
        FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Images only!')
    ])
    submit = SubmitField('Add Car')

class TestDriveForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    preferred_date = DateField('Preferred Date', format='%Y-%m-%d', validators=[DataRequired()])
    preferred_time = StringField('Preferred Time (e.g., "10:00 AM")', validators=[DataRequired()])
    submit = SubmitField('Request Test Drive')