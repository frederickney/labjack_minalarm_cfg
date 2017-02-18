__author__ = 'Frederick NEY'
import threading
import signal


def init():
    global exiting
    exiting = False
