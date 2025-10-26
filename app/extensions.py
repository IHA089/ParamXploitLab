from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Create instances of extensions WITHOUT the app
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()

# Configure login_manager here
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'