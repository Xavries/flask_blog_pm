import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))

class Config:
    DEBUG = True
    # SQLite3 #### SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.sqlite')
    SQLALCHEMY_DATABASE_URI = 'postgresql://thhnotdmgcunwz:415d6dc5b0c3955c85c96ce04d2393b1257f77b0dd1277c8646ebc5466b9523e@ec2-3-230-61-252.compute-1.amazonaws.com:5432/da47drr0meiv51'
    # DEV##### SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost'
    #database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(dbuser=os.environ['DBUSER'], dbpass=os.environ['DBPASS'], dbhost=os.environ['DBHOST'], dbname=os.environ['DBNAME'])
    # EXAMPLE https://github.com/Azure-Samples/flask-postgresql-app/blob/master/app/app.py
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = SECRET_KEY = os.urandom(16).hex()#'super-secret'
    #SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT", '146585145368132386173505678016728509634')
    #SECURITY_PASSWORD_HASH = 
    #SECURITY_TRACKABLE = True
    JWT_TOKEN_LOCATION = ['headers', 'query_string', 'cookies'] #'headers', 'query_string', 
    JWT_COOKIE_SECURE = False
    JWT_COOKIE_CSRF_PROTECT = False # should be set to TRUE to be more secure and JWT_ACCESS_CSRF_HEADER_NAME uncommented
    #JWT_ACCESS_CSRF_HEADER_NAME = "X-CSRF-TOKEN-ACCESS"
    TRACK_USAGE_COOKIE = True
    #MONGODB_HOST = 'mongodb+srv://Xavries:AEZmCnF9OpvnXNmd@flaskblogpm.pqoao.mongodb.net/FlaskBlog?retryWrites=true&w=majority'
    #MONGODB_PORT = 27017
