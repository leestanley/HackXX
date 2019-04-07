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


def messagenumber(address, phonenumber):
    phonenumber = "+1" + str(phonenumber)
    number = "+16262728111"
    client.messages.create(to=number, from_="+16264062098", body="Person needs help:" + "Address: " + address + "Number: " + phonenumber)


def get_url(string):
    address = "https://maps.googleapis.com/maps/api/geocode/json?address=" + string + "&key=AIzaSyBeu3-8-4hldPWilLmmvw2HoL0_3cyMdBs"
    return address


def get_addr_from_url(url):
    import requests
    response = requests.get(url)
    text = response.text
    addressLists = json.loads(text)
    formatted_address = addressLists['results'][0]['formatted_address']
    location = addressLists['results'][0]['geometry']['location']
    location = (location['lat'], location['lng'])
    return (formatted_address, location)


def getAddress(filename):
    with open(filename, 'r') as y:
        dataList = y.read()
        addressLists = json.loads(dataList)
        # print(addressLists['results'][0])
        formatted_address = addressLists['results'][0]['formatted_address']
        location = addressLists['results'][0]['geometry']['location']
        print(formatted_address, location)


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
    address = get_addr_from_url(get_url(address))[0]
    print(address)
    phonenumber = request.form['phonenumber']
    messagenumber(address, phonenumber)
    return render_template('redirect.html', name=name, address=address, phonenumber=phonenumber)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
