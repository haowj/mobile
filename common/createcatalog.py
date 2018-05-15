# -*- coding: utf-8 -*-

import os
from common.reads import ReadFile


class MobileStatistical(ReadFile):
    def __init__(self, catalog):
        super(MobileStatistical, self).__init__(catalog)
        if os.path.basename(catalog) == 'ALARM':
            self.ALARM = '004'
            self.PERIODIC = '002'
            self.PROGRAMINFO = '003'

    def write_data(self):
        d = os.path.splitdrive(r'C:\Users\wj\Desktop\henan_20180506\PERIODIC')
        d = d[1].split('\\')
        base_dir = d[-1]
        
        self.file_00()


class SoloBoot:
    """
    创建多级目录继续日志文件拆分
    一级目录：省份
    二级目录：时刻-24个时间段划分
    三级目录：日志类型（001-资源原始数据，002-运行周期原始数据，003-收视原始数据，004-告警原始数据）
    四级目录：日期
    """
    def __init__(self, city, catalog, catalog_one, catalog_tow, catalog_three):
        self.BASE_DIR = os.path.join(catalog, city)
        self.BASE_ONE = os.path.join(self.BASE_DIR, catalog_one)
        self.BASE_TOW = os.path.join(self.BASE_ONE, catalog_tow)
        self.BASE_THREE = os.path.join(self.BASE_TOW, catalog_three)

    def file_create(self):
        if not self.__is_city(self.BASE_DIR):
            os.makedirs(self.BASE_DIR)
        if not self.__is_city(self.BASE_ONE):
            os.makedirs(self.BASE_ONE)
        if not self.__is_city(self.BASE_TOW):
            os.makedirs(self.BASE_TOW)
        if not self.__is_city(self.BASE_THREE):
            os.makedirs(self.BASE_THREE)

    def __is_city(self, path):
        return os.path.isdir(path)

