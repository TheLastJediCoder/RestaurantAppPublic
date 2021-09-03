import os
import cloudinary.uploader


SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SESSION_TYPE = 'sqlalchemy'
SECRET_KEY = 'SECRET KEY'

cloudinary.config(
    cloud_name=os.environ.get('CLOUD_NAME'),
    api_key=os.environ.get('API_KEY'),
    api_secret=os.environ.get('API_SECRET')
)

