var http = require('http'),
    express = require('express'),
    path = require('path');

var app = express();

app.use(express.static(__dirname));
app.get('/', function(req, res){
  res.sendFile(path.join(__dirname, 'index.html'));
})


var server = http.createServer(app);

server.listen(1500);
