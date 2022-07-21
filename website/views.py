from flask import Blueprint, render_template, session
import json

views = Blueprint('views', __name__)

@views.route('/')
def home():
	user = session.get('user')
	if not user:
		return render_template('guest.html', user=user)

	return render_template('home.html', user=user)