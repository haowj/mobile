# -*- coding: utf-8 -*-
"""
Created on 2018-5-8

@author: wj

"""
import os
import gzip
import pymysql
import logging
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class CommonTool:
    def __init__(self, catalog, base_dir=None):
        # 探针版本--,设备类型,设备SN
        self.catalog = catalog
        if os.path.basename(catalog) == 'ALARM':
            self.BASE_TOW = '004'
        elif os.path.basename(catalog) == 'PERIODIC':
            self.BASE_TOW = '002'
        elif os.path.basename(catalog) == 'PROGRAMINFO':
            self.BASE_TOW = '003'
        else:
            self.BASE_TOW = '001'

        self.BASE_DIR = base_dir
        d = os.path.splitdrive(catalog)
        d = d[1].split('\\')
        self.base_city_date = d[-2].split('_')

    def file_sn_list(self):
        for data in self.__get_summary_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    try:
                        yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                    except UnicodeDecodeError:
                        yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_list(self):
        pad = self.BASE_DIR + '\\' + self.base_city_date[0] + '\\' + self.BASE_TOW + '\\' + \
              self.base_city_date[1]

        if not os.path.isdir(pad):
            os.makedirs(pad)
        else:
            [os.remove(os.path.join(pad, f)) for f in os.listdir(pad)]
        for data in self.__get_summary_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    try:
                        filename = line[11:13].decode(encoding='utf-8')
                    except UnicodeDecodeError:
                        filename = line[11:13].decode(encoding='gbk')
                    if filename == '':
                        filename = 'eee'

                    with open(os.path.join(pad, filename), 'ab') as fin:
                        fin.write(line)
            else:
                print('data value is none')
        fin.close()

    def __get_summary_file(self):
        filename_list = os.listdir(self.catalog)
        for i in range(len(filename_list)):
            if filename_list[i][-2:] == 'gz':
                path = os.path.join(self.catalog, filename_list[i])
                if os.path.isfile(path):
                    yield self.__read_log_file(path)

    # 读取文件数据
    def __read_log_file(self, path):
        if os.path.exists(path):
            with gzip.open(path, 'r') as f:
                try:
                    for line in f:
                        yield line
                except EOFError:
                    pass
        else:
            print('the path [{}] is not exist!'.format(path))

    # 读取文件数据
    @staticmethod
    def get_gz_file(path):
        if os.path.exists(path):
            with gzip.open(path, 'r') as f:
                for line in f:
                    yield line
        else:
            print('the path [{}] is not exist!'.format(path))

    @staticmethod
    def file_log_list(data):

        if getattr(data, '__iter__', None):
            for line in data:
                yield line.decode(encoding='utf-8').rstrip('\n').split('|')
        else:
            print('data value is none')

    @staticmethod
    def db_mysql_connect():
        return pymysql.connect("192.168.1.222", "root", "cmcc123", "mobile_application", charset="utf8")

    @staticmethod
    def db_oracle_connect():
        return

    @staticmethod
    def str_numeric(data):
        if len(str(data)) <= 10:
            return str(0) * (10 - len(str(data))) + str(data)
        else:
            raise EOFError('Beyond the range of data length')

    @staticmethod
    def data_all_list(cursor):
        data_list = list()
        for i in cursor:
            towlist = []
            for t in i:
                towlist.append(t)
            data_list.append(towlist)
        return data_list

    @staticmethod
    def data_one_list(cursor):
        for i in cursor:
            yield int(i[0])