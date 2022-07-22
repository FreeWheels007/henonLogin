from flask import Blueprint, render_template, session, redirect, url_for
import json

views = Blueprint('views', __name__)


# Decorator to determine if user is logged in via session cookie
# if not, redirect to guest
def loggedin_required(function):
	def wrapper(*args, **kwargs):
		if 'user' in session:
			return function()
		else:
			return redirect(url_for('views.guest'))

	wrapper.__name__ = function.__name__
	return wrapper


# Guest welcome page
@views.route('/')
def guest():
	return render_template('guest.html', user=None)


# logged in home page
@views.route('/home')
@loggedin_required
def home():
	user = session.get('user')
	return render_template('home.html', user=user)


@views.route('/second')
@loggedin_required
def second():
	user = session.get('user')
	return render_template('second_page.html', user=user)