from __future__ import print_function

import napalm
from napalm import get_network_driver
import sys
import os
import json
import pprint

driver = napalm.get_network_driver("iosxr")

device = driver(
        hostname="10.10.20.70",
        username="admin",
        password="admin",
        optional_args={"port": 2221},
    )

print("Opening ...")
device.open()

pprint.pprint(device.cli(['show interface description', 'show ip interface brief']))



# cmds = ['show ip interface brief']
# input = device.cli(cmds)


# for i in input.keys():
#    input[i] = input[i].split('\n')

# print(json.dumps(input, sort_keys=True, indent=4))



