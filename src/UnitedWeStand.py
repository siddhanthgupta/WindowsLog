'''
Created on 15-Apr-2016

@author: siddhanthgupta
'''

import os
import traceback

from DatabaseConnect import DatabaseHandler
from LogReader import log_dir_linux, log_dir_windows, LogReader


class UnitedWeStand(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.log_reader = LogReader()

    def send_record(self, filename, xml_record_str):
        # print 'Sending message for file=', filename, 'message=',
        # xml_record_str
        pass

    def generate_messages(self, filename, database_count):
        index = database_count + 1
        try:
            while(True):
                record = self.log_reader.getRecord(filename, index)
                index += 1
                self.send_record(filename, record)
        except RuntimeError:
            return index - 1

    def update_file_entry(self, filename):
        with DatabaseHandler() as d:
            entry = d.get_filecount_entry(filename)
            if(entry is None):
                entry = 0
#             count = self.log_reader.getEventCount(file)
            count = self.generate_messages(filename, entry)
            d.add_filecount_entry(filename, count)

    def intialize_database(self):
        if(os.name == 'posix'):
            log_dir = log_dir_linux
        else:
            log_dir = log_dir_windows
        for file in os.listdir(log_dir):
            filename, filetype = os.path.splitext(file)
            if(filetype == '.evtx'):
                print 'Initialization: updating entry for', file
                try:
                    self.update_file_entry(file)
                except Exception:
                    traceback.print_exc()
        x = DatabaseHandler()
        x.get_all_records()

if __name__ == '__main__':
    x = UnitedWeStand()
#     x.update_file_entry('Security.evtx')
#     y = DatabaseHandler()
#     y.get_all_records()
    x.intialize_database()
#     x.intialize_database()
