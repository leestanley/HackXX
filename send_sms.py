import json
from twilio.rest import Client
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from werkzeug.utils import secure_filename

# Use a service account
cred = credentials.Certificate("./public/firm-mariner-236104-firebase-adminsdk-8nwb7-4ca7808749.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# client signed up for twilio
client = Client("ACa563b9de6ab6d42cd338e61a45450ae2", "0526090669333dff604ed558b50d7372")


def getURL(string):
    address = "https://maps.googleapis.com/maps/api/geocode/json?address=" + string + "&key=AIzaSyBeu3-8-4hldPWilLmmvw2HoL0_3cyMdBs"
    return address


def getAddrFromUrl(url):
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


def getNumberList2(filename):
    with open(filename, 'r') as f:
        data = f.read()
        phoneLists = json.loads(data)
    for phoneList in phoneLists:
        number = phoneList['phone']
        client.messages.create(to=number, from_="+16264062098", body="person needs help")


def main():
    # getAddress('googlemap_json.txt')
    addrtup = getAddrFromUrl(getURL("9369 lower azusa"))
    print(addrtup[0])


docs = db.collection(u'users').get()
phonenumbers = []
for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
    docdict = doc.to_dict()
    print(docdict['phonenumber'])
    phonenumbers.append(docdict['phonenumber'])

print(phonenumbers)
