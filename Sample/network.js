var net = require('net');
var HOST = '13.59.178.74';
var PORT = 6969;
var client = new net.Socket();
client.connect(PORT, HOST, function(){
	console.log('CONNECTED ' + HOST + ':' + PORT);
	client.write('Request');
});

client.on('data', function(data){
	console.log('DATA: '+ data);
	// client.destroy();
});

client.on('close', function() {
	console.log('Connection closed');
});
