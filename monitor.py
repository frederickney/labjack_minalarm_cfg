__author__ = 'admin_master'

import threading
from stream import *
from labjack import ljm


def clamp(x, min_v, max_v):
    return min(max_v, max(min_v, x))


class Devices:

    def __init__(self, handles, rate, io_name, request_num, scan_rate):
        super(Devices, self).__init__()
        self.data = []
        for i in range(len(handles)):
            self.data.append([])
        self.io_name = io_name
        self.rate = rate
        self.io_addr = ljm.namesToAddresses(len(io_name), io_name)[0]
        self.syncStream = Stream(handles, rate)
        self.handles = handles
        self.first_mesure = 0.0
        self.last_mesure = 0.0
        self.request_num = request_num
        self.scan_rate = scan_rate

    def run(self):
        if len(self.handles) != 0:
            self.syncStream.readSteam(self.io_name, self.request_num, self.scan_rate, self.data)

"""
class Thread(threading.Thread):
    def __init__(self, handles, data, rate, io_name, request_num, scan_rate):
        super(Thread, self).__init__()
        self.syncStream = Stream(handles, rate)
        self.handles = handles
        self.data = data
        self.io_name = io_name
        self.request_num = request_num
        self.scan_rate = scan_rate
        self.io_addr = ljm.namesToAddresses(len(io_name), io_name)[0]

    def run(self):
        self.syncStream.readSteam(self.io_name, self.request_num, self.scan_rate, self.data)
"""