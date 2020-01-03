from pysnmp.entity.rfc3413.oneliner import cmdgen
from napalm import get_network_driver as gnd

import constants as c


def snmp_get(device):

    snmp_results = {
        "device": None,
        "err_indication": None,
        "snmp_result": None,
        "napalm_driver": None
    }

    generator = cmdgen.CommandGenerator()
    snmp_results["err_indication"], errorStatus, errorIndex, snmpResultVar = generator.getCmd(
        cmdgen.CommunityData(c.GNS3_DETAILS["community"]),
        cmdgen.UdpTransportTarget((device, 161)),
        '1.3.6.1.2.1.1.1.0')

    if snmp_results["err_indication"] == None:
        snmp_results["snmp_result"] = snmpResultVar[0].prettyPrint()

        if "Cisco IOS Software" in snmp_results["snmp_result"]:
            snmp_results["napalm_driver"] = "ios"
        elif "Arista" in snmp_results["snmp_result"]:
            snmp_results["napalm_driver"] = "eos"
    else:
        snmp_results["snmp_result"] = "n/a"
        snmp_results["napalm_driver"] = "n/a"

    return snmp_results


def gather_facts(device, snmp_dict):
    result = {'uptime': "n/a",
              'vendor': 'n/a',
              'os_version': 'n/a',
              'serial_number': 'n/a',
              'model': 'n/a',
              'hostname': 'n/a',
              'fqdn': 'n/a',
              'interface_list': ['n/a'],
              'no_facts_reason': None}

    if snmp_dict["napalm_driver"] in ['ios', 'eos']:
        driver = gnd(snmp_dict["napalm_driver"])
        dev = driver(device, c.GNS3_DETAILS['username'], c.GNS3_DETAILS['password'])
        try:
            dev.open()
            res = dev.get_facts()
            print(res)
            for k,v in res.items():
                result[k] = res[k]
        except Exception as err:
            print(device, ' ==>> ', err)
        finally:
            dev.close()
        return result

    else:
        result['no_facts_reason'] = "NO_NAPALM_DRIVER_FOUND"
        return result


if __name__ == '__main__':
    pass