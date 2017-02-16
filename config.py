__author__ = 'Frederick NEY'
from labjack import ljm
import LabjackT7Lib as kernel


def ld_dio_update_config(handle, dio_dir, dio_state):
    fio_state_register = ljm.eReadAddress(handle, kernel.T7_FIO_STATE, kernel.T7_FIO_STATE_T)
    fio_dir_register = ljm.eReadAddress(handle, kernel.T7_FIO_DIR, kernel.T7_FIO_DIR_T)
    ljm.eWriteAddress(handle, kernel.T7_FIO_DIR, kernel.T7_FIO_DIR_T, fio_dir_register | dio_dir)
    ljm.eWriteAddress(handle, kernel.T7_FIO_STATE, kernel.T7_FIO_STATE_T, fio_state_register | dio_state)
    return


def ld_dio_erase_config(handle, dio_dir, dio_state):
    ljm.eWriteAddress(handle, kernel.T7_FIO_DIR, kernel.T7_FIO_DIR_T, dio_dir)
    ljm.eWriteAddress(handle, kernel.T7_FIO_STATE, kernel.T7_FIO_STATE_T, dio_state)
    return


def ld_aio_update_config(handle, mode):
    return


def ld_aio_erase_config(handle, mode):
    return


def ld_aio_update_resolution_config(handle, resolutions):
    ain_addrs = [
        kernel.T7_AIN0_RANGE,
        kernel.T7_AIN1_RANGE,
        kernel.T7_AIN2_RANGE,
        kernel.T7_AIN3_RANGE,
        kernel.T7_AIN4_RANGE,
        kernel.T7_AIN5_RANGE,
        kernel.T7_AIN6_RANGE,
        kernel.T7_AIN7_RANGE,
        kernel.T7_AIN8_RANGE,
        kernel.T7_AIN9_RANGE,
        kernel.T7_AIN10_RANGE,
        kernel.T7_AIN11_RANGE,
        kernel.T7_AIN12_RANGE,
        kernel.T7_AIN13_RANGE,
    ]
    for resolution, ain_addr in zip(resolutions, ain_addrs):
        if resolution != 0:
            ljm.eWriteAddress(handle, ain_addr, kernel.T7_AIN_RANGE_T, resolution)
    return


def ld_aio_erase_resolution_config(handle, resolutions):
    ain_addrs = [
        kernel.T7_AIN0_RANGE,
        kernel.T7_AIN1_RANGE,
        kernel.T7_AIN2_RANGE,
        kernel.T7_AIN3_RANGE,
        kernel.T7_AIN4_RANGE,
        kernel.T7_AIN5_RANGE,
        kernel.T7_AIN6_RANGE,
        kernel.T7_AIN7_RANGE,
        kernel.T7_AIN8_RANGE,
        kernel.T7_AIN9_RANGE,
        kernel.T7_AIN10_RANGE,
        kernel.T7_AIN11_RANGE,
        kernel.T7_AIN12_RANGE,
        kernel.T7_AIN13_RANGE,
    ]
    for resolution, ain_addr in zip(resolutions, ain_addrs):
        ljm.eWriteAddress(handle, ain_addr, kernel.T7_AIN_RANGE_T, resolution)
    return


def ld_dio_config(handles, dio_dir=0x00, dio_state=0, update_dio=0):
    if dio_dir != 0x00 or dio_state != 0:
        for handle in handles:
            if 1 == update_dio:
                ld_dio_update_config(handle, dio_dir, dio_state)
            else:
                ld_dio_erase_config(handle, dio_dir, dio_state)
    return


def ld_ain_config(handles, aio_dir=0, aio_values=[], aio_res=[], update_aio=0):
    if type([]) == type(aio_values):
        if aio_dir == 1:
            if 2 == len(aio_values) and aio_values:
                for handle in handles:
                    if 1 == update_aio:
                        ld_aio_update_config(handle, aio_values)
                    else:
                        ld_aio_erase_config(handle, aio_values)
            elif 0 < len(aio_values) and (2 != len(aio_values)):
                if len(aio_values) < 2:
                    print("Unable to configure analog output due to aio_values list is less than 2")
                else:
                    print("Unable to configure analog output due to aio_values list is greater than 2")
        elif aio_dir == 0:
            if 14 == len(aio_res) and aio_res:
                for handle in handles:
                    if 1 == update_aio:
                        ld_aio_update_resolution_config(handle, aio_res)
                    else:
                        ld_aio_erase_resolution_config(handle, aio_res)
            elif 0 < len(aio_res) and (14 != len(aio_res)):
                if len(aio_res) < 14:
                    print("Unable to configure analog output due to aio_values list is less than 14")
                else:
                    print("Unable to configure analog output due to aio_values list is greater than 14")
    else:
        print("Bad parameter type for aio_value, expected <class 'list'> found " + str(type(aio_values)))
    return