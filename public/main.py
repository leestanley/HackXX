import json
import requests
from flask_wtf import FlaskForm, Form
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired
from flask import Flask, url_for, jsonify, render_template, request
from twilio.rest import Client

client = Client("ACa563b9de6ab6d42cd338e61a45450ae2", "0526090669333dff604ed558b50d7372")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone'


def getNumberList2(filename):
    with open(filename, 'r') as f:
        data = f.read()
        phoneLists = json.loads(data)
    for phoneList in phoneLists:
        number = phoneList['phone']
        client.messages.create(to=number, from_="+16264062098", body="person needs help")


def testnumber(address, phonenumber):
    phonenumber = "+1" + str(phonenumber)
    number = "+16262728111"
    client.messages.create(to=number, from_="+16264062098", body="Person needs help:" + "Address: " + address + "Number: " + phonenumber)


class InputForm(Form):
    name = StringField('name', validators=[InputRequired()])
    address = StringField('address', validators=[InputRequired()])
    phonenumber = IntegerField('phonenumber', validators=[InputRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        return redirect(url_for('redirect'))
    return render_template('index.html', form=form)


@app.route('/redirect', methods=['GET', 'POST'])
def redirect():
    name = request.form['name'].upper()
    address = request.form['address'].upper()
    phonenumber = request.form['phonenumber']
    testnumber(address, phonenumber)
    return render_template('redirect.html', name=name, address=address, phonenumber=phonenumber)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
