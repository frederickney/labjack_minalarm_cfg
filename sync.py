__author__ = 'admin_master'

import threading
import time
import stream
from labjack import ljm
import sys


def clamp(x, min_v, max_v):
    return min(max_v, max(min_v, x))


class Devices:

    def __init__(self, handles, rate, io_name, request_num, scan_rate):
        super(Devices, self).__init__()
        self.data = []
        for i in range(len(handles)):
            self.data.append([])
        self.thread = Thread(handles, self.data, rate, io_name, request_num, scan_rate)
        self.rate = rate
        self.handles = handles
        self.first_mesure = 0.0
        self.last_mesure = 0.0
        self.request_num = request_num
        self.scan_rate = scan_rate

    """
    Function to synchronise input output stream between labjacks and minalarms.
    """
    def sync(self):
        self.thread.start()
        sync_array = []
        """while True:"""
        for i in range(len(self.handles)):
            sync_array.append([])
        if len(self.handles) != 0:
            time.sleep(10)
        for i in range(len(self.handles)):
            for j in range(len(self.data[i])):
                print(self.data[i][j])
                val1 = clamp(j - 1, 0, len(self.data[i]) - 1)
                val2 = clamp(j + 1, 0, len(self.data[i]) - 1)
                if self.data[i][val1] <= self.data[i][j] and self.data[i][j] >= self.data[i][val2]:
                    """
                        the index of the max value of the scan
                    """
                    sync_array[i].append(j)
        if self.thread.is_alive():
            print("stopping sync")
            self.thread.join()
        for k in range(len(self.handles)):
            for i in range(len(sync_array[k])):
                for j in range(len(sync_array[k])):
                    if abs(sync_array[k][j] - sync_array[k][i]) % self.request_num == 0:
                        return (sync_array[k][j] - sync_array[k][i]) / clamp(j * self.rate, 1, sys.maxsize)
        return 1000


class Thread(threading.Thread):
    def __init__(self, handles, data, rate, io_name, request_num, scan_rate):
        super(Thread, self).__init__()
        self.syncStream = stream.Stream(handles, rate)
        self.handles = handles
        self.data = data
        self.io_name = io_name
        self.request_num = request_num
        self.scan_rate = scan_rate
        self.io_addr = ljm.namesToAddresses(len(io_name), io_name)[0]

    def run(self):
        self.syncStream.syncStream(self.io_name, self.request_num, self.scan_rate, self.data)
