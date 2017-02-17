__author__ = 'Frederick NEY'
from labjack import ljm
import LabjackT7Lib as Kernel
from KeyboardManager import *


def monitor_dio_ain(handle):
    Globals.init()
    thread = MonitorEsc()
    thread.start()
    Globals.lock.acquire()
    while not Globals.exiting:
        Globals.lock.release()
        """
        #TODO wait timer
        #TODO read register
        #TODO print register content
        """
        Globals.lock.acquire()
    return