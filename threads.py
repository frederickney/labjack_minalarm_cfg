__author__ = 'Frederick NEY'
import Globals
import threading
import time
from labjack import ljm



class Thread(threading.Thread):

    def __init__(self, connection_info, reconnection_attempt, second):
        self.connection_info = connection_info
        self.reconnection_attempt = reconnection_attempt
        self.second = second
        self.error = None

    def run(self):
        for i in range(self.reconnection_attempt):
            try:
                handle = ljm.open(
                    self.connection_info[0],
                    self.connection_info[1],
                    self.connection_info[2]
                )
                if handle > 0:
                    Globals.handles.append(handle)
                    Globals.information.append(self.connection_info)
                    print("\tDevice " + str(self.connection_info) + " successfully reconnected\n")
                    return 0
            except ljm.ljm.LJMError as LjmError:
                self.error = LjmError._errorString
            time.sleep(self.second)
            print("\tUnable to reconnect to device " + str(self.connection_info) + ". Removed permanently\n")
        return -1