# DJANGO MODELS
from django.conf import settings
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sd9.settings")
django.setup()

from sd9server.models import SD9
from django.forms.models import model_to_dict
import json
# END DJANGO

import ServerSettings

from OSC import OSCServer
import client
import sys
from time import sleep

def changeAuxValue(auxnumber, channel, value):
	data = model_to_dict(SD9.objects.get(pk=1))
	jsonData = json.loads(data["aux"+str(auxnumber)+"Values"])
	jsonData[channel-1] = value
	data["aux"+str(auxnumber)+"Values"] = json.dumps(jsonData)
	SD9(**data).save()

def changeInputName(channel, name):
	data = SD9.objects.get(pk=1)
	jsonData = json.loads(data.inputNames)
	jsonData[channel-1] = name
	data.inputNames = json.dumps(jsonData)
	data.save()

server = OSCServer( (ServerSettings.IP_ADDRESS, ServerSettings.RECEIVER_PORT) )

server.timeout = 0
run = True

# this method of reporting timeouts only works by convention
# that before calling handle_request() field .timed_out is 
# set to False
def handle_timeout(self):
	self.timed_out = True

# funny python's way to add a method to an instance of a class
import types
server.handle_timeout = types.MethodType(handle_timeout, server)

def auxVolumeCallback(path, tags, args, source):
	channel = int(path.split("/Input_Channels/")[1].split("/Aux_Send/")[0])
	auxSend = int(path.split("/Input_Channels/")[1].split("/Aux_Send/")[1].split("/send_level")[0])
	volume = float(args[0])
	changeAuxValue(auxSend, channel, volume)
	print ("Channel: ", channel, ", auxSend: ", auxSend, ", volume: ", volume)

def inputNameCallback(path, tags, args, source):
	channel = int(path.split("/Input_Channels/")[1].split("/Channel_Input/name")[0])
	name = str(args[0])
	changeInputName(channel, name)
	print ("Channel: ", channel, ", name: ", name)	


server.addDefaultHandlers()
for x in range(1,49):
	server.addMsgHandler("/Input_Channels/"+str(x)+"/Channel_Input/name", inputNameCallback)
	for y in range(1,12):
		server.addMsgHandler("/Input_Channels/"+str(x)+"/Aux_Send/"+str(y)+"/send_level", auxVolumeCallback)


def serverStuff():
	# clear timed_out flag
	server.timed_out = False
	# handle all pending requests then return
	while not server.timed_out:
		server.handle_request()

count = 0
def clientStuff():
	global localdata
	global count
	for z in range(1,13):
		data = model_to_dict(SD9.objects.get(pk=1))
		auxArray = data["aux"+str(z)+"Values"]
		localAuxArray = localdata["aux"+str(z)+"Values"]

		if (auxArray != localAuxArray):
			auxArrayJSON = json.loads(auxArray)
			localAuxArrayJSON = json.loads(localAuxArray)
		
			for i in range(0, len(auxArrayJSON)):
				if (auxArrayJSON[i] != localAuxArrayJSON[i]):
					location = "/Input_Channels/"+ str(i+1) + "/Aux_Send/" + str(z) + "/send_level"
					client.sendMessage(location, float(auxArrayJSON[i]))

	if (count > 3):
		localdata = model_to_dict(SD9.objects.get(pk=1))
		count = 0
	else:
		count += 1

print "--------------------------------"
print "Server Connected"
client.connect(ServerSettings.DESK_IP_ADDRESS, ServerSettings.SEND_PORT)
print "Client Connected"
print "--------------------------------"
print "Initialising Complete"
print "--------------------------------"
print "Server running on " + ServerSettings.IP_ADDRESS
print "TX: " + str(ServerSettings.SEND_PORT)
print "RX: " + str(ServerSettings.RECEIVER_PORT)
print "--------------------------------"

localdata = model_to_dict(SD9.objects.get(pk=1))

while run:
	# receive from SD9 (server stuff)
	serverStuff()
	# send to SD9 (client stuff)
	clientStuff()


server.close()