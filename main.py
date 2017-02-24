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
    ain_config, dio_conf, settling_conf, resolution_config = None, None, None, None
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
        settling_addr = [SETTLING_ADDR[0], SETTLING_ADDR[6]]
        resolution_addr = [RES_ADDR[0], RES_ADDR[1]]
        ain_range = 1
        ain_config = ld_ain_config(handles, ain_addr, aio_dir=1, ain_range=ain_range)
        dio_conf = ld_dio_config(handles, 0, 0, 1)
        settling_conf = ld_settling_config(handles, settling_addr, SETTLING_LIST[0])
        resolution_config = ld_resolution_config(handles, resolution_addr, RES_LIST[12])
        Globals.add_global_handles(handles)
        Globals.add_global_information(information)
        if ain_config == 0 and settling_conf == 0 and resolution_config == 0 and dio_conf == 0:
            monitor_dio_ain(handles, information)
            print("Closing connection to devices")
        else:
            if dio_conf == 0:
                print("I/O configuration: Success.")
            else:
                print("I/O configuration: Failure.")
            if ain_config == 0:
                print("Analog configuration: Success.")
            else:
                print("Analog configuration: Failure.")
            if settling_conf == 0:
                print("Settling time configuration: Success.")
            else:
                print("Settling time configuration: Failure.")
            if resolution_config == 0:
                print("Resolution configuration: Success.")
            else:
                print("Resolution configuration: Failure.")
            print("Configuration unsuccessful. Closing connection")
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

