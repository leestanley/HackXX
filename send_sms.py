import json
from twilio.rest import Client
#client signed up for twilio
client = Client("ACa563b9de6ab6d42cd338e61a45450ae2", "0526090669333dff604ed558b50d7372")

#we need a function that will call this when person presses button
#json has info on housing ppl but only their phone numbers
#for loop, get phone numbers from the database//housers and send a text message to them

#json objects are stored in key:value pairs where key = address of house and value = phone number
#for each json.key, extract json.value since key is location of housing and value is going to be phone number
#store the value into an aray called phoneNumberList

#iterate through the data and for each object, extract the value(phone number) and store it into a var that will be stored into another array
#return this array
#def getNumberList(data):
 # a = open("data").read()
 # phoneList = json.loads(a);
#  for x in phoneList.getValues():
    #    client.messages.create(to="x",
    #                           from_="+12023351278",
        #                       body="person needs help")


def getNumberList2(filename):
    with open(filename, 'r') as f:
        data = f.read()
        phoneLists = json.loads(data)
    for phoneList in phoneLists:
        number = phoneList['phone']
        client.messages.create(to=number, from_="+16264062098", body="person needs help")

'''
{
"address": "9500 Gilman Drive",
"phone": "+19494137602"
}
'''
