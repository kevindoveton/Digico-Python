from OSC import OSCClient, OSCMessage

client = OSCClient()

def connect(ipAddress, port):
	client.connect( (ipAddress, port) )

def sendMessage(address, params):
	msg = OSCMessage(address)
	msg.append(params);
	client.send(msg)