IP_ADDRESS = "192.168.1.201"
SEND_PORT = 6050
RECEIVER_PORT = 5050

from OSC import OSCServer
import client
import sys
from time import sleep

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
    print ("Channel: ", channel, ", auxSend: ", auxSend, ", volume: ", volume) 

server.addDefaultHandlers()
for x in range(1,40):
    for y in range(1,12):
        server.addMsgHandler("/Input_Channels/"+str(x)+"/"+str(y)+"/fader", auxVolumeCallback)
# server.addMsgHandler( "/Input_Channels/24/Aux_Send/1/fader", callback )

# sendMessage("/Input_Channels/24/Aux_Send/1/send_level", -150.0)

def each_frame():
    # clear timed_out flag
    server.timed_out = False
    # handle all pending requests then return
    while not server.timed_out:
        server.handle_request()

# client.connect(IP_ADDRESS, SEND_PORT)

while run:
    # receive from SD9 (server stuff)
    each_frame()
    # send to SD9 (client stuff)



server.close()