import os
from flask import Flask
from config import Config
from app.extensions import db, migrate, bcrypt, login_manager

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True) 
    app.config.from_object(config_class)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.models import load_user, User, Car, TestDrive, BaseModel, ExteriorColor, Wheel, Interior, UserConfiguration
    login_manager.user_loader(load_user)
    
    # --- Register Blueprints ---
    from app.main.routes import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth.routes import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/')

    from app.shopping.routes import bp as shopping_bp
    app.register_blueprint(shopping_bp, url_prefix='/cars')

    from app.management.routes import bp as management_bp
    app.register_blueprint(management_bp, url_prefix='/manage')
    
    from app.configurator.routes import bp as configurator_bp
    app.register_blueprint(configurator_bp, url_prefix='/configurator')
    
    # --- 6. Create DB tables and Seed Data ---
    with app.app_context():
        db.create_all()
        
        # --- THIS IS THE NEW LOGIC ---
        # Import the seeder function
        from app.utils import seed_data
        # Run the seeder (it will check if data exists first)
        seed_data()
        # --- END OF NEW LOGIC ---

    return app