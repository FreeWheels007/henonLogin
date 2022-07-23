from os import environ as env
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask

ENV_FILE = find_dotenv()
if ENV_FILE:
	load_dotenv(ENV_FILE)

application = Flask(__name__)
application.secret_key = env.get('APP_SECRET_KEY')

oauth = OAuth(application)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

from .views import views
from .auth import auth

application.register_blueprint(views, url_prefix='/')
application.register_blueprint(auth, url_prefix='/auth/')