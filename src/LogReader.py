'''
Created on 13-Apr-2016

@author: siddhanthgupta
'''
from Evtx.Evtx import FileHeader
from Evtx.Views import evtx_file_xml_view
import argparse
import contextlib
import mmap
import os.path

log_dir = '/media/siddhanthgupta/78965695965653AA/Windows/System32/winevt/Logs/'


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

    def getEventCount(self, filename):
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

if __name__ == '__main__':
    log_reader = LogReader()
    log_reader.readLogFile('OAlerts.evtx')
