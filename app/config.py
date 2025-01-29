import os

class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_key'

    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'super_jwt_secret_key'
