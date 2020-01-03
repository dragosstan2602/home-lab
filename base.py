import constants as c
import yaml
import subprocess
from napalm import get_network_driver as gnd
from pprint import pprint


class Device:
    def __init__(self, ip, username, password, en_pass, napalm_driver):
        self.ip = ip
        self.username = username
        self.password = password
        self.en_pass = en_pass
        self.napalm_driver = napalm_driver

    def test_init(self):
        print(self.ip)
        print(self.username)

    def ping_test(self):
        status = subprocess.call(
            ['ping', '-c', '1', self.ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        if status == 0:
            return True
        else:
            return False

    def get_napalm_info(self):
        driver = gnd(self.napalm_driver)
        device = driver(
            hostname=self.ip,
            username=self.username,
            password=self.password,
            optional_args={"secret": self.en_pass},
        )
        try:
            device.open()
            #print(device.get_facts())
            pprint(device.get_interfaces())
            pprint(device.get_interfaces_ip())
            pprint(device.get_lldp_neighbors())
            pprint(device.get_bgp_neighbors())
            print("########################################")
            device.close()
        except Exception as err:
            print(err, self.ip)
