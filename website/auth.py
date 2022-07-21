from flask import Blueprint, render_template, redirect, session, url_for
from website import oauth

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
	return oauth.auth0.authorize_redirect(
        redirect_uri=url_for('auth.callback', _external=True)
    )

@auth.route('/callback', methods=['GET', 'POST'])
def callback():
	token = oauth.auth0.authorize_access_token()
	session["user"] = token
	return redirect("/")

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )