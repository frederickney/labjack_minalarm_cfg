__author__ = 'Frederick NEY'
from labjack import ljm
import LabjackT7Lib as Kernel
from KeyboardManager import *
import time
from threads import Thread


def monitor_dio_ain(handles, information, display_sec=1, conn_attempt=5, conn_try_sec=3):
    """
        function to display values of some register
    :param handles: list of connections
    :param information: information of connections
    :param display_sec: time between each display
    :param conn_attempt: number of reconnection try
    :param conn_try_sec: time between each reconnection try
    :return:
    """
    Globals.add_global_handles(handles)
    Globals.add_global_information(information)
    threads = []
    while not Globals.exiting:
        time.sleep(display_sec)
        for handle in Globals.handles:
            try:
                print("getting information")
                print("AIN0: " + str(ljm.eReadAddress(handle, Kernel.T7_AIN0, Kernel.T7_AIN_T)))
                print("AIN1: " + str(ljm.eReadAddress(handle, Kernel.T7_AIN1, Kernel.T7_AIN_T)))
                print("FIO0: " + str(ljm.eReadAddress(handle, Kernel.T7_FIO0, Kernel.T7_FIO_T)))
                print("FIO1: " + str(ljm.eReadAddress(handle, Kernel.T7_FIO1, Kernel.T7_FIO_T)))
            except ljm.ljm.LJMError:
                index = Globals.handles.index(handle)
                info = Globals.information[index]
                print("Device " + str(info) + " is disconnected")
                thread = Thread(info, conn_attempt, conn_try_sec)
                threads.append(thread)
                Globals.information.remove(Globals.information[index])
                Globals.handles.remove(handle)
                print("Device " + str(info) + " removed from list of devices")
                print("Trying to reconnect to " + str(info))
                thread.start()
    for thread in threads:
        if thread.is_alive():
            thread.exit(0)
    for handle in Globals.handles:
        ljm.close(handle)
    return

