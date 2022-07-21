from flask import Blueprint, render_template, session

views = Blueprint('views', __name__)

@views.route('/')
def home():
	return render_template('base.html', user=session.get('user'))