import os
import cloudinary.uploader

# os.environ.get('')

SQLALCHEMY_DATABASE_URI = 'MYSQL URI'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SESSION_TYPE = 'sqlalchemy'
SECRET_KEY = 'SECRET KEY'

# cloudinary.config(
#     cloud_name=os.environ.get('CLOUD_NAME'),
#     api_key=os.environ.get('API_KEY'),
#     api_secret=os.environ.get('API_SECRET')
# )
cloudinary.config(
    cloud_name='cloud_name',
    api_key='api_key',
    api_secret='api_secret'
)
