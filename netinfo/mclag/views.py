from django.shortcuts import render, redirect
from .forms import CmdForm
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Host
from napalm import get_network_driver
from netmiko import ConnectHandler
from django.core.files import File
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
        with driver(device.host, device.username, device.password, optional_args={'port': 2221}) as device_conn:
            interfaces = device_conn.get_config()
            # with open('mclag/config/', 'w') as f:
            #     myfile = File(f)
            #     myfile.write(interfaces)
            # configuration = device_conn.send_command("show running-config")
        context = {
                'device': device,
                'interfaces': interfaces,
        }
        return render(request,  'mclag/config.html' , context)
    
    


    elif request.method == 'POST':
        form = CmdForm(request.POST)
        if form.is_valid():
                device = {}
                device['device_type'] = 'cisco_xr'
                device['ip'] = '10.10.20.70'
                device['username'] = 'admin'
                device['password'] = 'admin'
                device["port"] = 2221
                conn = ConnectHandler(**device)
                output = conn.send_command("show running-config")
        
                return render(request, 'mclag/index.html', {'output' : output})
    else:
            form = CmdForm()
    return render(request, 'mclag/index.html', {'form' : form})


    
    

        