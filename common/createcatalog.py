# -*- coding: utf-8 -*-

import os
import time, threading
from common.reads import ReadFile


class MobileStatistical(ReadFile):
    """
      创建多级目录继续日志文件拆分
      一级目录：省份
      二级目录：时刻-24个时间段划分
      三级目录：日志类型（001-资源原始数据，002-运行周期原始数据，003-收视原始数据，004-告警原始数据）
      四级目录：日期
    """
    def __init__(self, catalog, base_dir):
        super(MobileStatistical, self).__init__(catalog)
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

    def write_file(self):
        pad = self.BASE_DIR + '\\' + self.base_city_date[0] + '\\' + '%s' + '\\' + self.BASE_TOW + '\\' + \
              self.base_city_date[1]

        if not os.path.isdir(pad):
            os.makedirs(pad)

        for data in self.disassembly_file():
            if getattr(data, '__iter__', None):
                for i in data:
                    print(i)
                    break
                    fin = open(os.path.join(pad % i[11:13], i[3]), 'a')
                    fin.write(i.replace('|', ','))
        fin.close()

    def write_file_00(self):
        pad = self.BASE_DIR + '\\' + self.base_city_date[0] + '\\' + '00' + '\\' + self.BASE_TOW + '\\' + \
              self.base_city_date[1]

        if not os.path.isdir(pad):
            os.makedirs(pad)

        for i in self.file_00():
            fin = open(os.path.join(pad, i[3]), 'a')
            fin.write(','.join(i))
            fin.write('\n')
            fin.close()

    def write_file_01(self):
        pass

    def write_file_02(self):
        pass

    def write_file_03(self):
        pass

    def write_file_04(self):
        pass

    def write_file_05(self):
        pass

    def write_file_06(self):
        pass

    def write_file_07(self):
        pass

    def write_file_08(self):
        pass

    def write_file_09(self):
        pass

    def write_file_10(self):
        pass

    def write_file_11(self):
        pass

    def write_file_12(self):
        pass

    def write_file_13(self):
        pass

    def write_file_14(self):
        pass

    def write_file_15(self):
        pass

    def write_file_16(self):
        pass

    def write_file_17(self):
        pass

    def write_data(self):
        d = os.path.splitdrive(self.catalog)
        d = d[1].split('\\')
        base_dir = d[-2].split('_')
        pad = r'E' + '\\' + base_dir[0] + '\\' + '%s' + '\\' + base_dir[1]

        def structural_storage(data, types):
            if not os.path.isdir(pad % types):
                os.makedirs(pad % types)
            for i in data:
                print(i)
                # if len(i) < 33:
                #     continue
                # if i[10] == '':
                #     i[10] = 0
                # if i[11] == '':
                #     i[11] = 0
                # if i[21] == '':
                #     i[21] = 0
                # if i[22] == '':
                #     i[22] = 0

        t1 = threading.Thread(target=structural_storage, args=(self.file_00(), '00'))
        t2 = threading.Thread(target=structural_storage, args=(self.file_01(), '01'))
        t3 = threading.Thread(target=structural_storage, args=(self.file_02(), '02'))
        t4 = threading.Thread(target=structural_storage, args=(self.file_03(), '03'))
        t5 = threading.Thread(target=structural_storage, args=(self.file_04(), '04'))
        t6 = threading.Thread(target=structural_storage, args=(self.file_05(), '05'))
        t7 = threading.Thread(target=structural_storage, args=(self.file_06(), '06'))
        t8 = threading.Thread(target=structural_storage, args=(self.file_07(), '07'))
        t9 = threading.Thread(target=structural_storage, args=(self.file_08(), '08'))
        t10 = threading.Thread(target=structural_storage, args=(self.file_09(), '09'))

        t11 = threading.Thread(target=structural_storage, args=(self.file_00(), '10'))
        t12 = threading.Thread(target=structural_storage, args=(self.file_01(), '11'))
        t13 = threading.Thread(target=structural_storage, args=(self.file_02(), '12'))
        t14 = threading.Thread(target=structural_storage, args=(self.file_03(), '13'))
        t15 = threading.Thread(target=structural_storage, args=(self.file_04(), '14'))
        t16 = threading.Thread(target=structural_storage, args=(self.file_05(), '15'))
        t17 = threading.Thread(target=structural_storage, args=(self.file_06(), '16'))
        t18 = threading.Thread(target=structural_storage, args=(self.file_07(), '17'))
        t19 = threading.Thread(target=structural_storage, args=(self.file_08(), '18'))
        t20 = threading.Thread(target=structural_storage, args=(self.file_09(), '19'))

        t21 = threading.Thread(target=structural_storage, args=(self.file_00(), '20'))
        t22 = threading.Thread(target=structural_storage, args=(self.file_01(), '21'))
        t23 = threading.Thread(target=structural_storage, args=(self.file_02(), '22'))
        t24 = threading.Thread(target=structural_storage, args=(self.file_03(), '23'))

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()
        t11.start()
        t12.start()
        t13.start()
        t14.start()
        t15.start()
        t16.start()
        t17.start()
        t18.start()
        t19.start()
        t20.start()
        t21.start()
        t22.start()
        t23.start()
        t24.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()
        t10.join()
        t11.join()
        t12.join()
        t13.join()
        t14.join()
        t15.join()
        t16.join()
        t17.join()
        t18.join()
        t19.join()
        t20.join()
        t21.join()
        t22.join()
        t23.join()
        t24.join()


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

