// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
// DANGER! This is insecure. See http://twil.io/secure
const accountSid = 'ACa563b9de6ab6d42cd338e61a45450ae2';
const authToken = '0526090669333dff604ed558b50d7372';
const client = require('twilio')(accountSid, authToken);

client.messages
  .create({
     body: 'This is the ship that made the Kessel Run in fourteen parsecs?',
     from: '+16264062098',
     to: '+16262728111'
   })
  .then(message => console.log(message.sid));
