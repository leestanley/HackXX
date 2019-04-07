import json
from twilio.rest import Client
# client signed up for twilio
client = Client("ACa563b9de6ab6d42cd338e61a45450ae2", "0526090669333dff604ed558b50d7372")

# we need a function that will call this when person presses button
# json has info on housing ppl but only their phone numbers
# for loop, get phone numbers from the database//housers and send a text message to them

# json objects are stored in key:value pairs where key = address of house and value = phone number
# for each json.key, extract json.value since key is location of housing and value is going to be phone number
# store the value into an aray called phoneNumberList

# iterate through the data and for each object, extract the value(phone number) and store it into a var that will be stored into another array
# return this array
# def getNumberList(data):
# a = open("data").read()
# phoneList = json.loads(a);
#  for x in phoneList.getValues():
#    client.messages.create(to="x",
#                           from_="+12023351278",
#                       body="person needs help")

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
    print(formatted_address, location)

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
    getAddrFromUrl(getURL("9369 lower azusa"))

if __name__ == '__main__':
    main()

'''
{
"address": "9500 Gilman Drive",
"phone": "+19494137602"
}
'''
