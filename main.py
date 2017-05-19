#!/bin/python2.7
__author__ = 'Frederick NEY'
from connect import *
from config import *
from Monitoring import *
import signal
import Sync
import sync

def main():
    """
        entry point of the program
    """
    print("Configuring system")
    ain_config, settling_conf, resolution_config = None, None, None
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
    handles, information = ld_connect(T7_DEVICE, CT[0])
    if len(handles) != 0:
        print("\tFound " + str(len(handles)) + " device(s)")
        ain_addr = [AIN_ADDRS[0], AIN_ADDRS[2], AIN_ADDRS[4], AIN_ADDRS[1], AIN_ADDRS[3], AIN_ADDRS[5]]
        settling_addr = [SETTLING_ADDR[0], SETTLING_ADDR[2], SETTLING_ADDR[4], SETTLING_ADDR[1], SETTLING_ADDR[3], SETTLING_ADDR[5]]
        resolution_addr = [RES_ADDR[0], RES_ADDR[2], RES_ADDR[4], RES_ADDR[1], RES_ADDR[3], RES_ADDR[5]]
        ain_range = [10.0, 10.0, 1.0, 10.0, 10.0, 10.0]
        gnd_ref_range = [NEGATIVE_REF_ADDR[0], NEGATIVE_REF_ADDR[2], NEGATIVE_REF_ADDR[4]]
        """ 1 is for AIN1, 3 for AIN3 and 5 for AIN5 """
        gnd_io_range = [1, 3, 5]
        ain_config = ld_ain_config(handles, ain_addr, aio_dir=1, ain_range=ain_range)
        settling_conf = ld_settling_config(handles, settling_addr, SETTLING_LIST[6])
        resolution_config = ld_resolution_config(handles, resolution_addr, RES_LIST[12])
        gnd_config = ld_gnd_ref_conf(handles, gnd_ref_range, gnd_io_range)
        Globals.add_global_handles(handles)
        Globals.add_global_information(information)
        if ain_config == 0 and settling_conf == 0 and resolution_config == 0 and gnd_config == 0:
            """
            sync = Sync.Devices(handles, 10, 1)

            sync.sync()
            """
            print("\tScanning device(s)")
            Sync = sync.Devices(handles, 500, ["AIN0", "AIN2", "AIN4", "AIN1", "AIN3", "AIN5"], 3000, 1)
            """
            Sync = sync.Devices(handles, 500, ["AIN0", "AIN2", "AIN4"], 3000, 1)
            """
            Sync.sync()
            """
            monitor_dio_ain(handles, information)
            print("Closing connection to devices")
            """
        else:
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
            if gnd_config == 0:
                print("Gnd references configuration: Success.")
            else:
                print("Gnd references configuration: Failure.")
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
