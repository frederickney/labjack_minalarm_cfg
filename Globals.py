__author__ = 'Frederick NEY'
import threading


def init():
    global exiting
    exiting = False


def add_global_handles(handle_list):
    global handles
    handles = handle_list
    return


def add_global_information(information_list):
    global information
    information = information_list
    return