__author__ = 'Frederick NEY'
import threading


def init():
    global exiting, lock
    exiting = False
    lock = threading.Lock()