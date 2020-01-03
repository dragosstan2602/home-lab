import os


GNS3_DETAILS = {"username": "dragos",
                "password": "arista",
                "en_pass": "arista",
                "napalm_driver": "eos",
                "community": "HomeReadOnly"}

GNS3_DEVICES = ["172.16.2.2", "172.16.2.1", "172.16.1.1", "172.16.1.2", "172.16.1.3"]

DEFAULT_FACTS = {
    'uptime': "n/a",
    'vendor': 'n/a',
    'os_version': 'n/a',
    'serial_number': 'n/a',
    'model': 'n/a',
    'hostname': 'n/a',
    'fqdn': 'n/a',
    'interface_list': ['n/a'],
    'no_facts_reason': None
    }
