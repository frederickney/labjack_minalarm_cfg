__author__ = 'Frederick NEY'
import sys
import tty
import termios
import threading
import Globals


class MonitorEsc(threading.Thread):

    def __init__(self, key='\x1b'):
        """
        key: the key code to detect for exiting the thread and updating global variable exit
        to true for exiting some other process default is ESC key
        """
        threading.Thread.__init__(self)
        self.escape_key = key

    def run(self):
        """
            Global variables exit and lock need to be set before starting thread
            exit is a simple boolean set to false, it will be set to true when the exit key is pressed
            lock is a thread locker to ensure atomic access to variable exit
        """
        while not Globals.exiting:
            if self.__getch__() == self.escape_key:
                Globals.lock.acquire()
                Globals.exiting = True
                Globals.lock.release()
                break
        return

    def __getch__(self):
        """

        return: keypressed
        """
        # POSIX system. Create and return a getch that manipulates the tty.
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
