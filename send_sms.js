// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
// DANGER! This is insecure. See http://twil.io/secure

//client signed up for twilio
const accountSid = 'ACa563b9de6ab6d42cd338e61a45450ae2';
const authToken = '0526090669333dff604ed558b50d7372';
const client = require('twilio')(accountSid, authToken);

//sends a message to this client
//we need a function that will call this when person presses button
//json has info on housing ppl but only their phone numbers
//for loop, get phone numbers from the database//housers and send a text message to them

//json objects are stored in key:value pairs where key = address of house and value = phone number
//host.getphoneNumber
// for each json.key, extract json.value since key is location of housing and value is going to be phone number
//store the value into an aray called phoneNumberList

//iterate through the data and for each object, extract the value(phone number) and store it into a var that will be stored into another array
//return this array
function getNumberList(json data){
  var finalJSON = {};
  for(var i in data)
        finalJSON.push(data[i]["Value"]);

finalJSON.forEach(function(value){
  client.messages
    .create({
       body: 'This person needs help',
       from: '+16264062098',
       to: value //change this with iteration
     })
    .then(message => console.log(message.sid));
});
}
