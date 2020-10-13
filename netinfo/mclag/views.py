from django.shortcuts import render

# Create your views here.


def index(request):
        from netmiko import ConnectHandler
        device = {}
        device['device_type'] = 'cisco_xr'
        device['ip'] = 'sbx-iosxr-mgmt.cisco.com'
        device['username'] = 'admin'
        device['password'] = 'C1sco12345'
        conn = ConnectHandler(**device)
        output = conn.send_command("show version | i uptime")
        print(output)
        return render(request, 'mclag/index.html', {'output' : output})