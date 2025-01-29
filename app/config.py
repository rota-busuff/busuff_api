import os

class Config:
    SQALCHEMY_TRACK_MODIFICATIONS = False
    SQLACHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_key'