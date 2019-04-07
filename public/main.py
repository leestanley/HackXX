import json
import requests
from flask_wtf import FlaskForm, Form
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired
from flask import Flask, url_for, jsonify, render_template, request
from twilio.rest import Client
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': project_id,
})

db = firestore.client()

# Use a service account
cred = credentials.Certificate('path/to/serviceAccount.json')
firebase_admin.initialize_app(cred)


client = Client("ACa563b9de6ab6d42cd338e61a45450ae2", "0526090669333dff604ed558b50d7372")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone'

#phonenumber should be array of housing numbers
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

#putting in for help
class InputForm1(Form):
    name = StringField('name', validators=[InputRequired()])
    address = StringField('address', validators=[InputRequired()])
    phonenumber = IntegerField('phonenumber', validators=[InputRequired()])
    submit = SubmitField('Submit')

#putting in for housing
class InputForm2(Form):
    name = StringField('name', validators=[InputRequired()])
    address = StringField('address', validators=[InputRequired()])
    phonenumber = IntegerField('phonenumber', validators=[InputRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form1 = InputForm1()
    form2 = InputForm2()
    if form1.validate_on_submit():
        return redirect1(url_for('redirect1'))
    if form2.valdiate_on_submit():
        return redirect2(url_for('redirect2'))
    return render_template('index.html', form2=form2)

#convert the housing form data to firebase then use firebase to create array of phone numbers
@app.route('/redirect1', methods=['GET', 'POST'])
def redirect1():
    name = request.form1['name'].upper()
    address = request.form1['address'].upper()
    address = get_addr_from_url(get_url(address))[0]
    print(address)
    phonenumber = request.form1['phonenumber']
    messagenumber(address, phonenumber)
    return render_template('redirect.html', name=name, address=address, phonenumber=phonenumber)

@app.route('/redirect2', methods=['GET', 'POST'])
def redirect2():
    name = request.form2['name'].upper()
    address = request.form2['address'].upper()
    address = get_addr_from-url(get_url(address))[0]
    print(address)
    phonenumber = request.form2['phonenumber']

doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

if __name__ == "__main__":
    app.run(port=8080, debug=True)
