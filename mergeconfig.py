#
# Note: this script is as simple as possible: it assumes that you have
# followed the lab setup in the quickstart tutorial, and so hardcodes
# the device IP and password.  You should also have the
# 'new_good.conf' configuration saved to disk.
from __future__ import print_function

import napalm
import sys
import os
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")


def main(config_file):
    """Load a config for the device."""

    if not (os.path.exists(config_file) and os.path.isfile(config_file)):
        msg = "Missing or invalid config file {0}".format(config_file)
        raise ValueError(msg)

    print("Loading config file {0}.".format(config_file))

    # Use the appropriate network driver to connect to the device:
    driver = napalm.get_network_driver("iosxr")

    

    # Connect:
    device = driver(
        hostname="10.10.20.70",
        username="admin",
        password="admin",
        optional_args={"port": 2231},
    )

    print("Opening ...")
    device.open()

    print("Loading merge candidate ...")
    device.load_merge_candidate(filename=config_file)

    # Note that the changes have not been applied yet. Before applying
    # the configuration you can check the changes:
    print("\nDiff:")
    print(device.compare_config())

    # You can commit or discard the candidate changes.

    if len(device.compare_config())>0:
    # # try:
    #     choice = raw_input("\nWould you like to commit these changes? [y/N]: ")
    # # except NameError:
        choice = input("\nWould you like to commit these changes? [y/N]: ")
        if choice == "y":
            print("Committing ...")
            device.commit_config()
        else:
            print("Discarding ...")
            device.discard_config()
    else:
        print("No difference")

    # close the session with the device.
    device.close()
    print("Done.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please supply the full path to "new_good.conf"')
        sys.exit(1)
    config_file = sys.argv[1]
    main(config_file)