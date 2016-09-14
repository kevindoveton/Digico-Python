from django.shortcuts import render
from django.http import HttpResponse
from sd9server.models import SD9
from django.forms.models import model_to_dict
import json
def changeAuxValue(auxnumber, channel, value):
	data = model_to_dict(SD9.objects.get(pk=1))
	jsonData = json.loads(data["aux"+str(auxnumber)+"Values"])
	jsonData[channel-1] = value
	data["aux"+str(auxnumber)+"Values"] = json.dumps(jsonData)
	SD9(**data).save()

def index(request):
	return render(request, 'index.html')

def aux(request, auxnumber):
	return render(request, 'aux.html')

def auxData(request, auxnumber):
	import json
	context = {}
	data = model_to_dict(SD9.objects.get(pk=1))
	json_data = '{ "values" : ' + data["aux"+auxnumber+"Values"] + ', "names" : '+data["inputNames"]+' }'
	return HttpResponse((json_data))

def auxUpdate(request):
	if request.method == 'GET':
		auxnumber = request.GET.get('aux')
		channel = request.GET.get('ch')
		volume = request.GET.get('vol')
		# if (volume > 10):
			# volume = 0
	changeAuxValue(int(auxnumber), int(channel), float(volume))
	return HttpResponse("")