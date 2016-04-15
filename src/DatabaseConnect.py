'''
Created on 15-Apr-2016

@author: siddhanthgupta
'''
import sqlite3


class DatabaseHandler:
    '''
    classdocs
    '''

    sqlite_file = 'windows_log.sqlite'    # name of the sqlite database file
    table_name1 = 'evtx_count'  # name of the table to be created
    filename_field = 'filename'  # name of the column
    filename_field_type = 'TEXT'  # column data type

    count_field = 'count'  # name of the column
    count_field_type = 'INTEGER'  # column data type

    def __init__(self):
        '''
        Constructor
        '''
        self.conn = sqlite3.connect(DatabaseHandler.sqlite_file)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS {tn} ({fn} {fnt} PRIMARY KEY, {c} {ct})'.format(
                tn=DatabaseHandler.table_name1,
                fn=DatabaseHandler.filename_field,
                fnt=DatabaseHandler.filename_field_type,
                c=DatabaseHandler.count_field,
                ct=DatabaseHandler.count_field_type))
        self.conn.commit()
        return self

    def add_filecount_entry(self, filename, count):
        try:
            self.cursor.execute(
                "INSERT INTO {tn} VALUES ('{fn}', {ct})".format(
                    tn=DatabaseHandler.table_name1,
                    fn=filename,
                    ct=count))
        except sqlite3.IntegrityError:
            self.cursor.execute(
                "UPDATE {tn} SET {cf}={ct} where {fnf}= '{fn}'".format(
                    tn=DatabaseHandler.table_name1,
                    cf=DatabaseHandler.count_field,
                    ct=count,
                    fnf=DatabaseHandler.filename_field,
                    fn=filename))

    def get_filecount_entry(self, filename):
        self.cursor.execute(
            "SELECT {cf} FROM {tn} WHERE {fnf}='{fn}'".format(
                cf=DatabaseHandler.count_field,
                tn=DatabaseHandler.table_name1,
                fnf=DatabaseHandler.filename_field,
                fn=filename))
        value = self.cursor.fetchone()
        if(value):
            return value[0]
        else:
            return None

    def get_all_records(self):
        self.cursor.execute(
            "SELECT * FROM {tn}".format(tn=DatabaseHandler.table_name1))
        rows = self.cursor.fetchall()
        print rows

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()


# if __name__ == '__main__':
#     with DatabaseHandler() as d:
#         d.add_filecount_entry('test2', 4)
#     x = DatabaseHandler()
#     x.get_filecount_entry('test2')
