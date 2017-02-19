#!/bin/python2.7
__author__ = 'Frederick NEY'
from connect import *
from config import *
from Monitoring import *
import signal


def main():
    """
        entry point of the program
    """
    print("Configuring system")
    print("\tSetting globals")
    Globals.init()
    print("\tSetting signals")
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGABRT, signal_handler)
    signal.signal(signal.SIGQUIT, signal_handler)
    signal.signal(signal.SIGTSTP, signal_handler)
    signal.signal(signal.SIGHUP, signal_handler)
    print("\tConnecting to devices")
    handles, information = ld_connect(T7_DEVICE, CT[3])
    if len(handles) != 0:
        print("\tFound " + str(len(handles)) + " device(s)")
        ain_addr = [AIN_ADDRS[0], AIN_ADDRS[1]]
        ain_range = 10.0
        if 0 == ld_ain_config(handles, ain_addr, aio_dir=1, ain_range=ain_range):
            # TODO configure digital and analog I/O
            monitor_dio_ain(handles, information)
            print("Closing connection to devices")
            for handle in Globals.handles:
                ljm.close(handle)
            print("Connections closed")
    else:
        print("\tUnable to detect any devices")
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    signal.signal(signal.SIGTERM, signal.SIG_DFL)
    signal.signal(signal.SIGQUIT, signal.SIG_DFL)
    signal.signal(signal.SIGTSTP, signal.SIG_DFL)
    signal.signal(signal.SIGHUP, signal.SIG_DFL)
    signal.signal(signal.SIGABRT, signal.SIG_DFL)
    print("Exiting")
    return

if __name__ == "__main__":
    main()

