import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'  # Change to a random string in production
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  # SQLite file in instance/ folder
    SQLALCHEMY_TRACK_MODIFICATIONS = False