__author__ = 'Frederick NEY'
import threading


def init():
    """
        initialising global exiting variable
    :return:
    """
    global exiting
    exiting = False


def add_global_handles(handles_list):
    """
    :param handles_list: to add into global handles
    :return:
    """
    global handles
    handles = handles_list
    return


def add_global_information(information_list):
    """
    :param information_list: to add into global information
    :return:
    """
    global information
    information = information_list
    return