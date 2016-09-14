from OSC import OSCClient, OSCMessage

client = OSCClient()

def connect(ipAddress, port):
	client.connect( (ipAddress, port) )

def sendMessage(address, params):
	msg = OSCMessage(address)
	msg.append(params);
	client.send(msg)

# def sendFilename():
# 	sendMessage("/Console/Session/Filename", "filename")

# def sendSnapshot():
# 	sendMessage("/Snapshots/Surface_Snapshot", -1)

# def sendAuxOutputModes():
# 	sendMessage("/Aux_Outputs/modes", [1, 1, 1, 1, 2, 2, 2, 2])

# def sendChannelCount():
# 	sendMessage("/Console/Input_Channels", 48)

# def sendAuxCount():
# 	sendMessage("/Console/Aux_Outputs", 8)

# def sendGroupCount():
# 	sendMessage("/Console/Group_Outputs", 6)

# def sendTalkbackCount():
# 	sendMessage("/Console/Talkback_Outputs", 1)

# def sendControlGroupCount():
# 	sendMessage("/Console/Control_Groups", 8)

# def sendMatrixCount():
# 	sendMessage("/Console/Matrix_Inputs", 12)

# def sendGraphicEQCount():
# 	sendMessage("/Console/Graphic_EQ", 12)

# def sendMultiCount():
# 	sendMessage("/Console/Multis", 0)

# def sendInputModes():
# 	sendMessage("/Console/Input_Channels/modes", [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1])

# def sendGroupOutputModes():
# 	sendMessage("/Console/Group_Output/modes", [1,1,1,2,2,2])

# def sendBankOne():
# 	sendMessage("/Layout/Layout/Banks", ["Music", "L", 0, 0, "Input_Channels", 1, "Input_Channels", 2, "Input_Channels", 3, "Input_Channels", 4, "Input_Channels", 5, "Input_Channels", 6, "Input_Channels", 7, "Input_Channels", 8, "Input_Channels", 9, "Input_Channels", 10, "Input_Channels", 11, "Input_Channels", 12])

# def sendName():
# 	sendMessage("/Console/Name", "SD9")
# 	print "called"

# def runAll():
# 	sendFilename()
# 	sendSnapshot()
# 	sendAuxOutputModes()
# 	sendChannelCount()
# 	sendAuxCount()
# 	sendGroupCount()
# 	sendTalkbackCount()
# 	sendControlGroupCount()
# 	sendMatrixCount()
# 	sendGraphicEQCount()
# 	sendMultiCount()
# 	sendInputModes()
# 	sendGroupOutputModes()
# 	sendBankOne()



