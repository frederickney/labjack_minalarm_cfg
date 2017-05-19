__author__ = 'Frederick NEY'
from labjack import ljm
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
        totSkip = 0 # Total skipped samples
        for handle in self.handles:
            scanRate = ljm.eStreamStart(handle, scansPerRead, len(io_name), io_name, self.rate)
        try:
            while i <= request:
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

                    print("\neStreamRead %i" % i)
                    ainStr = ""
                    for j in range(0, len(io_name)):
                        ainStr += "%s = %0.5f " % (io_name[j], data[j])
                    print(ainStr)
                    if request_num != -1:
                        i += 1
        except ljm.LJMError:
            ljm_err = sys.exc_info()[1]
            print(ljm_err)
        except Exception:
            e = sys.exc_info()[1]
            print(e)

    def syncStream(self, io_name, request_num, scansPerRead, array):
        """
            Function use for consulting value on the streamer
        :param io_name: input output name to scan
        :param request_num: number of request on the streamer
        :param scansPerRead: number of scan per read
        :return:
        """
        io_addr = ljm.namesToAddresses(len(io_name), io_name)[0]
        i = 0
        for handle in self.handles:
            """
                start stream on all devices.
            """
            scanRate = ljm.eStreamStart(handle, scansPerRead, len(io_addr), io_addr, self.rate)
        try:
            while i <= request_num:
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
                    print("\neStreamRead %i" % i)
                    ainStr = ""
                    for k in range(0, len(io_name)):
                        ainStr += "%s = %f " % (io_name[k], data[k])
                    print(ainStr)
                    array[j].append(data)
                    j += 1
                i += 1
        except ljm.LJMError:
            ljm_err = sys.exc_info()
            print(ljm.ljm.errorToString(1279))
            print(ljm_err)
        except Exception:
            e = sys.exc_info()
            print(e)