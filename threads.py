__author__ = 'Frederick NEY'
import Globals
import threading
import time
from labjack import ljm



class Thread(threading.Thread):
    """
        object Thread used to create threads.
    """

    def __init__(self, connection_info, reconnection_attempt, second):
        """
            constructor of the Thread object with some useful information
        :param connection_info: it will be a list of len 3 with at index 0 the device type,
                                index 1 the connection type and at index 2 the serial number of the device
        :param reconnection_attempt: number of time it will try to reconnect to devices
        :param second: number of second between reconnection
        :return:
        """
        self.connection_info = connection_info
        self.reconnection_attempt = reconnection_attempt
        self.second = second
        self.error = None

    def run(self):
        """
            main algorithm threads used to reconnect to devices after losing it connection
        """
        for i in range(self.reconnection_attempt):
            time.sleep(self.second)
            try:
                handle = ljm.open(
                    self.connection_info[0],
                    self.connection_info[1],
                    self.connection_info[2]
                )
                if handle > 0:
                    Globals.handles.append(handle)
                    Globals.information.append(self.connection_info)
                    print("\nDevice " + str(self.connection_info) + " successfully reconnected.\n")
                    return 0
            except ljm.ljm.LJMError as LjmError:
                self.error = LjmError._errorString
        print(
            "\nUnable to reconnect to device " + str(self.connection_info)
            + " Error: " + LjmError._errorString
            + ". Removed permanently\n"
        )
        return -1