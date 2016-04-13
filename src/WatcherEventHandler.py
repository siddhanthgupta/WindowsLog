'''
Created on 13-Apr-2016

@author: siddhanthgupta
'''
import logging
import os
from watchdog.events import FileSystemEventHandler


class WatcherEventHandler(FileSystemEventHandler):
    '''
    classdocs
    '''

#     def on_moved(self, event):
#         super(WatcherEventHandler, self).on_moved(event)
#
#         what = 'directory' if event.is_directory else 'file'
#         logging.info("Moved %s: from %s to %s", what, event.src_path,
#                      event.dest_path)
#
#     def on_created(self, event):
#         super(WatcherEventHandler, self).on_created(event)
#
#         what = 'directory' if event.is_directory else 'file'
#         logging.info("Created %s: %s", what, event.src_path)
#
#     def on_deleted(self, event):
#         super(WatcherEventHandler, self).on_deleted(event)
#
#         what = 'directory' if event.is_directory else 'file'
#         logging.info("Deleted %s: %s", what, event.src_path)

    def on_modified(self, event):
        super(WatcherEventHandler, self).on_modified(event)
        what = 'directory' if event.is_directory else 'file'
#         logging.info("Modified %s: %s", what, event.src_path)
        filename, filetype = os.path.splitext(event.src_path)
#         print filename, filetype
        if(filetype == '.evtx'):
            print 'Log file', filename, 'updated'
