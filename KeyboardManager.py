__author__ = 'Frederick NEY'
import Globals
import signal


def signal_handler(signum, frame):
    print('')
    Globals.exiting = True
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    signal.signal(signal.SIGTERM, signal.SIG_DFL)
    signal.signal(signal.SIGQUIT, signal.SIG_DFL)
    signal.signal(signal.SIGTSTP, signal.SIG_DFL)
    signal.signal(signal.SIGHUP, signal.SIG_DFL)
    signal.signal(signal.SIGABRT, signal.SIG_DFL)
    return