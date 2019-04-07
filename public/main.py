import numpy as np
import pandas as pd
import json
import requests
from bs4 import BeautifulSoup
from flask_wtf import FlaskForm, Form
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired
from flask import Flask, url_for, jsonify, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone'


class InputForm(Form):
    address = StringField('address', validators=[InputRequired()])
    phonenumber = IntegerField('phonenumber', validators=[InputRequired()])
    # gender = RadioField('gender')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        flash('You were successfully logged in')
    return render_template('index.html')


# @app.route('/redirect', methods=['GET', 'POST'])
# def redirect():
#     return render_template('redirect.html')


if __name__ == "__main__":
    app.run(port=8081, debug=True)
