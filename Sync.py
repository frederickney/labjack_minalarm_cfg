__author__ = 'Frederick NEY'

from labjack import ljm
import LabjackT7Lib as Kernel
import sys
import Globals
import sched
import threading
import time


def clamp(x, min_v, max_v):
    return min(max_v, max(min_v, x))


class Devices(object):
    """
    docstring for devices.
    """
    def __init__(self, handles, nb_pic, thread_time):

        super(Devices, self).__init__()
        self.data = []
        for i in range(len(handles)):
            self.data.append([])
        self.thread = Thread(thread_time, handles, self.data)
        self.pic_number = nb_pic
        self.handles = handles
        self.first_mesure = 0.0
        self.last_mesure = 0.0
        self.time = thread_time

    """
    Function to synchronise input output stream between labjacks and minalarms.
    """
    def sync(self):
        """

        :param nbScan:
        :return:
        """
        self.thread.start()
        """while True:"""
        time.sleep(10)
        for i in range(len(self.handles)):
            for j in range(len(self.data[i])):
                print(self.data[i][j])
                val1 = clamp(j - 1, 0, len(self.data[i]) - 1)
                val2 = clamp(j + 1, 0, len(self.data[i]) - 1)
        if self.thread.is_alive():
           print ("stoping")
           self.thread.join()
        return


class Thread(threading.Thread):

    def __init__(self, thread_timer, handles, data):
        super(Thread, self).__init__()
        self.time = thread_timer
        self.handles = handles
        self.data = data
        self.s = sched.scheduler(time.time, time.sleep)

    def run(self):
        self.s.enter(self.time, 1, self.sync_monitor)
        self.s.run()

    def sync_monitor(self):
        try:
            self.data[0].append(str(ljm.eReadAddress(self.handles[0], Kernel.T7_AIN1, Kernel.T7_AIN_T)))
        except ljm.ljm.LJMError:
            print("exiting")
            sys.exit(-1)
        self.s.enter(self.time, 1, self.sync_monitor)
