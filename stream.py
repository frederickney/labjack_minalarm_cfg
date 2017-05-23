__author__ = 'Frederick NEY'
from labjack import ljm
from KeyboardManager import *
import sys


class Stream:

    def __init__(self, handles, rate):
        """
            function to instance the streamer
        :param rate: scanner rate
        :param handles: connection to labjack devices
        :return:
        """
        self.rate = rate
        self.handles = handles

    def readStreamOn(self, io_name, request_num, scansPerRead):
        """
            Function use for consulting value on the streamer
        :param io_name: input output name to scan
        :param request_num: number of request on the streamer -1 will be an infinite loop
        :param scansPerRead: number of scan per read
        :return:
        """
        i = 0
        request = request_num
        if request_num == -1:
            request = 0
        totScans = 0
        index = 0
        array = []
        totSkip = 0 # Total skipped samples
        for handle in self.handles:
            scanRate = ljm.eStreamStart(handle, scansPerRead, len(io_name), io_name, self.rate)
            array.append([0, 0])
        try:
            while i <= request and not Globals.exiting:
                for handle in self.handles:
                    stream = ljm.eStreamRead(handle)

                    data = stream[0]
                    scans = len(data)/len(io_name)
                    totScans += scans

                    # Count the skipped samples which are indicated by -9999 values. Missed
                    # samples occur after a device's stream buffer overflows and are
                    # reported after auto-recover mode ends.
                    curSkip = data.count(-9999.0)
                    totSkip += curSkip
                    array[handle] = [array[handle][0] + data[0], array[handle][1] + data[1]]
                    if i % self.rate == 0 and i != 0:
                        ainStr = ""
                        for j in range(0, len(io_name)):
                            ainStr += "%s = %0.5f " % (io_name[j], array[handle][j] / self.rate)
                        print(ainStr)
                        array[handle] = [0, 0]
                    """print("\neStreamRead %i" % i)
                    ainStr = ""
                    for j in range(0, len(io_name)):
                        ainStr += "%s = %0.5f " % (io_name[j], data[j])
                    print(ainStr)"""
                    if request_num != -1:
                        i += 1
                    index += 1
                index = 0
        except ljm.LJMError:
            ljm_err = sys.exc_info()[1]
            print(ljm_err)
        except Exception:
            e = sys.exc_info()[1]
            print(e)

    def readSteam(self, io_name, request_num, scansPerRead, array):
        """
            Function use for consulting value on the streamer
        :param io_name: input output name to scan
        :param request_num: number of request on the streamer
        :param scansPerRead: number of scan per read
        :return:
        """
        io_addr = ljm.namesToAddresses(len(io_name), io_name)[0]
        i = 0
        index = 0
        arraymed = []
        for handle in self.handles:
            """
                start stream on all devices.
            """
            scanRate = ljm.eStreamStart(handle, scansPerRead, len(io_addr), io_addr, self.rate)
            arraymed.append([])
            for j in range(len(io_name)):
                arraymed[index].append(0)
            index += 1
        index = 0
        try:
            while i <= request_num and not Globals.exiting:
                j = 0
                for handle in self.handles:
                    """
                        append all data into an array of stream.
                        Example:
                        +---------+------+------------------------------+
                        | devices | scan | stream                       |
                        +---------+------+------------------------------+
                        |    0    |   0  | first scan out for a device  |
                        |         +------+------------------------------+
                        |         |   1  | second scan out for a device |
                        |         +------+------------------------------+
                        |         |   2  | third scan out for a device  |
                        |         +------+------------------------------+
                        |         |  ... | ............................ |
                        +---------+------+------------------------------+
                        |   ...   |  ... | ............................ |
                        +---------+------+------------------------------+
                    """
                    stream = ljm.eStreamRead(handle)
                    data = stream[0]
                    array[j].append(data)
                    for j in range(len(io_name)):
                        arraymed[index][j] = arraymed[index][j] + data[j]
                    if i % self.rate == 0 and i != 0:
                        print("\neStreamRead from %i to %i" % (i - self.rate, i))
                        ainStr = ""
                        for j in range(0, len(io_name)):
                            ainStr += "%s = %0.5f " % (io_name[j], arraymed[index][j] / self.rateself.rat * 2)
                        print(ainStr)
                        for j in range(0, len(arraymed[index])):
                            arraymed[index][j] = 0
                    """print("\neStreamRead %i" % i)
                    ainStr = ""
                    for j in range(0, len(io_name)):
                        ainStr += "%s = %0.5f " % (io_name[j], data[j])
                    print(ainStr)"""
                    j += 1
                    index += 1
                index = 0
                i += 1
        except ljm.LJMError:
            ljm_err = sys.exc_info()
            print(ljm.ljm.errorToString(1279))
            print(ljm_err)
        except Exception:
            e = sys.exc_info()
            print(e)
        """for i in range(len(self.handles)):
            for j in range(len(array[i])):
                print(array[i][j])"""