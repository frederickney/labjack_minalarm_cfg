#!/bin/python2.7
__author__ = 'Frederick NEY'
from connect import *
from config import *
from Monitoring import *


def main():
    handles = ld_connect(T7_DEVICE, CT[3])
    """
    #TODO configure digital and analog I/O
    #TODO run Monitoring
    """
    return

if __name__ == "__main__":
    main()

