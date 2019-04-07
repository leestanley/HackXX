import json
import requests
from flask_wtf import FlaskForm, Form
from wtforms import StringField, IntegerField, SubmitField, FileField
from wtforms.validators import InputRequired
from flask import Flask, url_for, jsonify, render_template, request
from twilio.rest import Client
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from werkzeug.utils import secure_filename

# Use a service account
cred = credentials.Certificate("firm-mariner-236104-firebase-adminsdk-8nwb7-4ca7808749.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


client = Client("ACa563b9de6ab6d42cd338e61a45450ae2", "0526090669333dff604ed558b50d7372")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone'


def messagenumber(name, address, phonenumber):
    phonenumber = "+1" + str(phonenumber)
    number = "+16262728111"
    client.messages.create(to=number, from_="+16264062098", body=name + "needs help:" + "Address: " + address + "Number: " + phonenumber)
    client.messages.create(to=phonenumber, from_="+16264062098", body="You will recieve help soon.")


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
        return(formatted_address, location)

# putting in for help


class InputForm(Form):
    name = StringField('name', validators=[InputRequired()])
    address = StringField('address', validators=[InputRequired()])
    phonenumber = IntegerField('phonenumber', validators=[InputRequired()])
    file = FileField()
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = InputForm()
    return render_template('index.html', form=form)

# convert the housing form data to firebase then use firebase to create array of phone numbers


@app.route('/redirecthome', methods=['GET', 'POST'])
def redirecthome():
    name = request.form['name'].upper()
    address = request.form['address'].upper()
    address = get_addr_from_url(get_url(address))[0]
    phonenumber = request.form['phonenumber']

    doc_ref = db.collection(u'users').document(u'' + address)
    doc_ref.set({
        u'name': u'' + name,
        u'phonenumber': u'+1' + phonenumber
    })

    return render_template('redirecthome.html', name=name, address=address, phonenumber=phonenumber)


@app.route('/redirecthelp', methods=['GET', 'POST'])
def redirecthelp():
    name = request.form['name'].upper()
    address = request.form['address'].upper()
    address = get_addr_from_url(get_url(address))[0]
    phonenumber = request.form['phonenumber']

    # file = request.form['file']
    # filename = secure_filename(file.filename)
    # file.save(os.path.join(
    #     app.instance_path, 'photos', filename
    # ))

    # messagenumber(name, address, phonenumber)
    return render_template('redirecthelp.html', name=name, address=address, phonenumber=phonenumber)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
