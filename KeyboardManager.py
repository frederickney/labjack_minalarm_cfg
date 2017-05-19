__author__ = 'Frederick NEY'
import Globals
import signal


def signal_handler(signum, frame):
    print('')
    Globals.exiting = True
    return