'''
Created on 13-Apr-2016

@author: siddhanthgupta
'''
import logging
import sys
import time
from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer
from src.WatcherEventHandler import WatcherEventHandler


class WatcherOnTheWall(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass

    def watchDirectory(self, directory):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        path = directory
        event_handler = WatcherEventHandler()
        observer = Observer()
        observer.schedule(event_handler, path, recursive=False)
        observer.start()
        try:
            while True:
                time.sleep(100)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()


if __name__ == '__main__':
    jon_snow = WatcherOnTheWall()
    jon_snow.watchDirectory('/tmp')