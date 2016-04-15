'''
Created on 13-Apr-2016

@author: siddhanthgupta
'''
from Evtx.Evtx import Evtx
from Evtx.Evtx import FileHeader
from Evtx.Views import evtx_file_xml_view
from Evtx.Views import evtx_record_xml_view
import argparse
import contextlib
import mmap
import os
import os.path
import sys


log_dir_linux = '/media/siddhanthgupta/78965695965653AA/Windows/System32/winevt/Logs/'
log_dir_windows = 'C:/Windows/Sysnative/winevt/Logs'


class LogReader(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass

    def readLogFile(self, filename):
        #         parser = argparse.ArgumentParser(
        #             description="Dump a binary EVTX file into XML.")
        #         parser.add_argument("--cleanup", action="store_true",
        #                             help="Cleanup unused XML entities (slower)"),
        #         parser.add_argument("evtx", type=str,
        #                             help="Path to the Windows EVTX event log file")
        #         args = parser.parse_args()

        if(os.name == 'posix'):
            log_dir = log_dir_linux
        else:
            log_dir = log_dir_windows
        with open(os.path.join(log_dir, filename), 'r') as f:
            with contextlib.closing(mmap.mmap(f.fileno(), 0,
                                              access=mmap.ACCESS_READ)) as buf:
                fh = FileHeader(buf, 0x0)
                print "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\" ?>"
                print "<Events>"
                count = 0
                for xml, record in evtx_file_xml_view(fh):
                    print xml
                    count += 1
                print "</Events>"
                print count, "events found"

    def getRecord(self, filename, record_number):
        #         parser = argparse.ArgumentParser(
        #             description="Write the raw data for a EVTX record to STDOUT")
        #         parser.add_argument("evtx", type=str,
        #                             help="Path to the Windows EVTX file")
        #         parser.add_argument("record", type=int,
        #                             help="The record number of the record to extract")
        #         args = parser.parse_args()
        if(os.name == 'posix'):
            log_dir = log_dir_linux
        else:
            log_dir = log_dir_windows
        with Evtx(os.path.join(log_dir, filename)) as evtx:
            record = evtx.get_record(record_number)

            if record is None:
                raise RuntimeError("Cannot find the record specified.")
#             sys.stdout.write(record.data())
            record_str = evtx_record_xml_view(record)
#             print record_str
            return record_str

    def getEventCount(self, filename):
        if(os.name == 'posix'):
            log_dir = log_dir_linux
        else:
            log_dir = log_dir_windows
        with open(os.path.join(log_dir, filename), 'r') as f:
            with contextlib.closing(mmap.mmap(f.fileno(), 0,
                                              access=mmap.ACCESS_READ)) as buf:
                fh = FileHeader(buf, 0x0)
                count = 0
                for chunk in fh.chunks():
                    for record in chunk.records():
                        count += 1
#                 print count, "events found"
                return count

# if __name__ == '__main__':
#     log_reader = LogReader()
#     log_reader.getEventCount('OAlerts.evtx')
# #     log_reader.readLogFile('OAlerts.evtx')
#     log_reader.getRecord('OAlerts.evtx', 1)
