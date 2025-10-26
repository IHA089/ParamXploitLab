# Import from app.extensions, NOT from app
from app.extensions import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# This is just a function, not a decorator
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
    
    test_drives = db.relationship('TestDrive', backref='customer', lazy=True)
    configurations = db.relationship('UserConfiguration', backref='customer', lazy=True) # <-- NEW

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False, default='BMW')
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_file = db.Column(db.String(100), nullable=True, default='default_car.jpg')
    
    engine = db.Column(db.String(100), nullable=True)
    zero_to_sixty = db.Column(db.String, nullable=True)
    range = db.Column(db.String(50), nullable=True)
    transmission = db.Column(db.String(100), nullable=True, default='Automatic')
    color = db.Column(db.String(100), nullable=True)
    
    test_drives = db.relationship('TestDrive', backref='car', lazy=True)

    def __repr__(self):
        return f'<Car {self.year} {self.make} {self.model}>'

class TestDrive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_requested = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default='Pending')
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)

    def __repr__(self):
        return f'<TestDrive {self.id} for Car {self.car_id}>'

# --- NEW CONFIGURATOR MODELS ---

class BaseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    base_price = db.Column(db.Float, nullable=False)
    image_file = db.Column(db.String(100), nullable=False, default='default_car.jpg')
    
    # Relationships
    colors = db.relationship('ExteriorColor', backref='base_model', lazy='dynamic')
    wheels = db.relationship('Wheel', backref='base_model', lazy='dynamic')
    interiors = db.relationship('Interior', backref='base_model', lazy='dynamic')

class ExteriorColor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0)
    image_file = db.Column(db.String(100), nullable=True) # Image of the car in this color
    model_id = db.Column(db.Integer, db.ForeignKey('base_model.id'), nullable=False)

class Wheel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0)
    image_file = db.Column(db.String(100), nullable=True) # Image of the wheel
    model_id = db.Column(db.Integer, db.ForeignKey('base_model.id'), nullable=False)

class Interior(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0)
    image_file = db.Column(db.String(100), nullable=True) # Image of the interior
    model_id = db.Column(db.Integer, db.ForeignKey('base_model.id'), nullable=False)

class UserConfiguration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Float, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    model_id = db.Column(db.Integer, db.ForeignKey('base_model.id'), nullable=False)
    color_id = db.Column(db.Integer, db.ForeignKey('exterior_color.id'), nullable=False)
    wheel_id = db.Column(db.Integer, db.ForeignKey('wheel.id'), nullable=False)
    interior_id = db.Column(db.Integer, db.ForeignKey('interior.id'), nullable=False)
    
    # Define relationships to easily fetch details
    model = db.relationship('BaseModel', lazy=True)
    color = db.relationship('ExteriorColor', lazy=True)
    wheel = db.relationship('Wheel', lazy=True)
    interior = db.relationship('Interior', lazy=True)