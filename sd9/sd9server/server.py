# DJANGO MODELS
from django.conf import settings
import os
import django
django.setup()

from sd9server.models import SD9
from django.forms.models import model_to_dict
import json
# END DJANGO

# CONFIG
IP_ADDRESS = "192.168.1.201"
SEND_PORT = 6050
RECEIVER_PORT = 5050
# END CONFIG


from OSC import OSCServer
# import client
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
# changeAuxValue(1,2, 0)

server = OSCServer( (IP_ADDRESS, RECEIVER_PORT) )
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
	channel = path.split("/Input_Channels/")[1].split("/Aux_Send/")[0]
	auxSend = path.split("/Input_Channels/")[1].split("/Aux_Send/")[1].split("/fader")[0]
	volume = args[0]
	changeAuxValue(auxsend, channel, value)
	print ("Channel: ", channel, ", auxSend: ", auxSend, ", volume: ", volume)

def inputNameCallback(path, tags, args, source):
	channel = path.split("/Input_Channels/")[1].split("/Channel_Input/name")[0]
	name = args[0]
	changeInputName(channel, name)
	print ("Channel: ", channel, ", name: ", name)	


server.addDefaultHandlers()
for x in range(1,40):
	server.addMsgHandler("/Input_Channels/"+str(x)+"/Channel_Input/name", inputNameCallback)
	for y in range(1,12):
		server.addMsgHandler("/Input_Channels/"+str(x)+"/"+str(y)+"/fader", auxVolumeCallback)
# server.addMsgHandler( "/Input_Channels/24/Aux_Send/1/fader", callback )

# sendMessage("/Input_Channels/24/Aux_Send/1/send_level", -150.0)

def serverStuff():
	# clear timed_out flag
	server.timed_out = False
	# handle all pending requests then return
	while not server.timed_out:
		server.handle_request()

# client.connect(IP_ADDRESS, SEND_PORT)
def clientStuff():
	a = ""

	
print "Initialising Complete"
print "---------------------"
print "Server running on " + IP_ADDRESS
print "TX: " + str(SEND_PORT)
print "RX: " + str(RECEIVER_PORT)
print "---------------------"
while run:
	# receive from SD9 (server stuff)
	serverStuff()
	# send to SD9 (client stuff)



server.close()