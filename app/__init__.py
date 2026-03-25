from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 1. Create the app instance
app = Flask(__name__)

# 2. Add your configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 4. VERY IMPORTANT: Import your models at the bottom
# This prevents "circular imports" but ensures Flask-Migrate sees your tables
from app import models