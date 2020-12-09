from netmiko import ConnectHandler 
from pprint import pprint
# import napalm
# import click
# import json
# from jinja_helper import template_config

import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")



r1 = { 
	'device_type': 'cisco_xr', 
	'ip': '10.10.20.70', 
	'username': 'admin',
	'password': 'admin',
	"port": "2221",
   }

r2 = { 
	'device_type': 'cisco_xr', 
	'ip': '10.10.20.70', 
	'username': 'admin',
	'password': 'admin',
	"port": "2231",
   }

routers = [r1]
for routerslist in routers :
    net_connect = ConnectHandler(**routerslist)
    output = net_connect.send_command("show run")
	
    file = open('output.cfg', 'w')
    file.write(str(output))
    file.close()
    
print(output)


router = [r2]
for routerlist in router :
    net_connect = ConnectHandler(**routerlist)
    output1 = net_connect.send_command("show run")
	
    file = open('output1.cfg', 'w')
    file.write(str(output1))
    file.close()



# class iosxrapi(object):
#     def __init__(self, hostname=None, username=None, password=None, optional_args=None):
#         driver = napalm.get_network_driver('iosxr')
#         self.connection = driver(hostname=hostname, username=username, password=password, optional_args={'port':2231})


#     def connect(self):
#         self.connection.open()

#     def disconnect(self):
#         self.connection.close()

#     def get_facts(self):
#         self.connect()
#         facts = self.connection.get_facts()
#         self.disconnect()
#         return facts

#     def get_interfaces(self):
#         self.connect()
#         facts = self.connection.get_interfaces()
#         self.disconnect()
#         return facts

#     def get_interfaces_ip(self):
#         self.connect()
#         facts = self.connection.get_interfaces_ip()
#         self.disconnect()
#         return facts
 
#     def compare_interfaces(self):
#         self.connect()
#         facts = self.connection.load_merge_candidate(filename='output.cfg')
#         print('\nDiff:')
#         diff = self.connection.compare_config()
#         print(diff)
#         if len(diff) < 1:
#             print('\nNo Changes Required Closing...')
#             self.connection.discard_config()
#             self.disconnect()
#             exit()

#         try:
#             choice = input("\nWould you like to commit these changes? [yN]: ")
#         except NameError:
#             choice = input("\nWould you like to commit these changes? [yN]: ")
#         if choice == 'y':
#             print('Committing ...')
#             self.connection.commit_config()

#         else:
#             print('Discarding ...')
#             self.connection.discard_config()
#             self.disconnect()

# device = iosxrapi("10.10.20.70", "admin", "admin")

# @click.group()
# def cli():
#     pass

# @click.command()
# def facts():
#     click.secho("Retrieving Information")
#     fact = json.dumps(device.get_facts(), sort_keys=True, indent=4)
#     click.echo(fact)

# @click.command()
# def interfaces():
#     click.secho("Retrieving Information")
#     interface = json.dumps(device.get_interfaces(), sort_keys=True, indent=4)
#     click.echo(interface)

# @click.command()
# def interfaces_ip():
#     click.secho("Retrieving Information")
#     interface_ip = json.dumps(device.get_interfaces_ip(), sort_keys=True, indent=4)
#     click.echo(interface_ip)

# @click.command()
# def merge():
#     click.secho("Compare configurations")
#     compare_interfaces = json.dumps(device.compare_interfaces(), sort_keys=True, indent=4)
#     click.echo(merge)


# cli.add_command(facts)
# cli.add_command(interfaces)
# cli.add_command(interfaces_ip)
# cli.add_command(merge)


# if __name__ == "__main__":
#     cli()

     



