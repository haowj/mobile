# -*- coding: utf-8 -*-
"""
Created on 2018-5-8

@author: wj

"""
import os
import gzip
import pymysql


class CommonTool:
    def __init__(self, catalog):
        # 探针版本--,设备类型,设备SN
        self.catalog = catalog
        self.equipment = None

    def file_list(self):
        for data in self.__get_summary_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                    # yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

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
                for line in f:
                    yield line
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
        return pymysql.connect("localhost", "root", "root", "app_relation", charset="utf8")

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