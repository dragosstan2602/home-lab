class SnmpWalk:
    def __init__(self, device):
        self.device = device
        self.community = "HomeReadOnly"
        self.devices = {}