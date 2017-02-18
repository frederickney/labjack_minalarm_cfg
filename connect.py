__author__ = 'Frederick NEY'
from labjack import ljm

"""
    Global constants used to detect devices
    ANY: String used to detect specific or any devices connected throw USB, ETHERNET and WIFI
    CT: String array used to detect any devices using specific protocol
    DEVICE: String containing the name of the device
"""
ANY = "ANY"
CT = ["USB", "ETHERNET", "WIFI", "TCP"]
T7_DEVICE = "T7"

"""
    Global constants used while connecting to specific device
    CD_INDEX: Index of the result of ljm.listAll() or lvm.listAllS() corresponding to the number of detected devices
    DT_INDEX: Index of the result of ljm.listAll() or lvm.listAllS() corresponding to the device type
    CT_INDEX: Index of the result of ljm.listAll() or lvm.listAllS() corresponding to the connection type
    SN_INDEX: Index of the result of ljm.listAll() or lvm.listAllS() corresponding to the serial number of the device
"""
CD_INDEX = 0
DT_INDEX = 1
CT_INDEX = 2
SN_INDEX = 3


def ld_connect(dt, ct):
    """
    function used to detect LabJack device(s) using specific protocol(s)
    dt: device type DEVICE and ANY allowed
    ct: connection type CT values and ANY allowed
    return: list of connection to devices and list of connection information in case of loosing connection for
            trying to restore the connection to de device
    >>> dev = ld_connect(ANY, ANY)   #it will connect to any labjack devices using any protocols
    >>> dev = ld_connect(DEVICE_T7, CT[3]) #it will connect to labjack t7 devices using tcp protocols
    >>> dev = ld_connect(DEVICE_T7, ANY)   #it will connect to labjack t7 devices using any protocols
    >>> dev = ld_connect(DEVICE_T7, CT[2])   #it will connect to labjack t7 devices using only wifi
    >>> dev = ld_connect(DEVICE_T7, CT[1])   #it will connect to labjack t7 devices using only ethernet
    >>> dev = ld_connect(DEVICE_T7, CT[0])   #it will connect to labjack t7 devices using only usb
    """
    connection_info = []
    handle = []
    labjack_devices = ljm.listAllS(dt, ct)
    for index in range(labjack_devices[CD_INDEX]):
        try:
            handle.append(
                ljm.open(
                    labjack_devices[DT_INDEX][index],
                    labjack_devices[CT_INDEX][index],
                    labjack_devices[SN_INDEX][index]
                )
            )
            connection_info.append(
                [
                    labjack_devices[DT_INDEX][index],
                    labjack_devices[CT_INDEX][index],
                    labjack_devices[SN_INDEX][index]
                ]
            )
        except ljm.ljm.LJMError as LjmError:
            print(
                LjmError._errorString + ": Unable to connect to device " + str(
                    [
                        labjack_devices[DT_INDEX][index],
                        labjack_devices[CT_INDEX][index],
                        labjack_devices[SN_INDEX][index]
                    ]
                )
            )

    return handle, connection_info