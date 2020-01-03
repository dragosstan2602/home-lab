from base import Device
import constants as c
import yaml


if __name__ == '__main__':
    def get_hosts(devices_file):
        with open(devices_file, 'r') as read_devices:
            stream = read_devices
            read_devices_result = yaml.load(stream, Loader=yaml.Loader)

        return read_devices_result

    host_dict = get_hosts('hostfile.yaml')['hosts']

    for host in host_dict.keys():
        device = Device(host_dict[host]['mgmt_ip'],
                        c.GNS3_DETAILS['username'],
                        c.GNS3_DETAILS['password'],
                        c.GNS3_DETAILS['en_pass'],
                        c.GNS3_DETAILS['napalm_driver'])

        #device.test_init()
        #print(device.driver)
        #print(device.password)

        if device.ping_test():
            #print(device.ip, " True")
            try:
                device.get_napalm_info()
            except Exception as err:
                print(err, device.ip)
        else:
            print(device.ip, " False")
