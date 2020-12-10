from django.shortcuts import render, redirect
from .forms import CmdForm
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Host
from napalm import get_network_driver
from netmiko import ConnectHandler
from django.core.files import File
import  json
import re
from rest_framework import status
from django.template import RequestContext


# Create your views here.



def index(request: HttpRequest)-> HttpResponse:
    devices = Host.objects.all()
    context = {
        'title': 'Welcome',
        'devices': devices
    }
    return render(request, 'mclag/index.html', context)

    
   

def get_config(request: HttpRequest, device_id) -> HttpResponse:
    device = Host.objects.get(pk=device_id)
    if request.method == 'GET':
        driver = get_network_driver(device.napalm_driver)
        with driver(device.host, device.username, device.password, optional_args={'port': 2231, 'global_delay_factor': 4,} ) as device_conn:
            interfaces = device_conn.get_config()
            with open('/home/aurora/Documents/output.cfg', 'w') as f:
                myfile = File(f)
                myfile.write(str(interfaces))
                myfile.close()

            with open('/home/aurora/Documents/output.cfg', 'r') as f:
                myfile = f.read()
            # configuration = device_conn.send_command("show running-config")
        context = {
                'device': device,
                'interfaces': interfaces,
                'myfile' : myfile,

        }
        return render( request, 'mclag/config.html',context, content_type=json)
        
    


    # elif request.method == 'POST':
    #     form = CmdForm(request.POST)
    #     if form.is_valid():
    #             device = {}
    #             device['device_type'] = 'cisco_xr'
    #             device['ip'] = '10.10.20.70'
    #             device['username'] = 'admin'
    #             device['password'] = 'admin'
    #             device["port"] = 2221
    #             conn = ConnectHandler(**device)
    #             output = conn.send_command("show running-config")

    #             file = open('/home/aurora/Documents/output.cfg', 'w')
    #             file.write(str(output))
                

    #             file = open('/home/aurora/Documents/Netmiko/output.cfg', 'r')
    #             file_contents = file.read()
    # #      
    # #
    # #           return HttpResponse(file_contents,content_type=json, status=status.HTTP_200_OK)  
                
               

    #             return HttpResponse(file_contents, content_type=json)
    else:
            form = CmdForm()
    return render(request, 'mclag/index.html', {'form' : form})


    
    

        