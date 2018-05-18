# -*- coding: utf8 -*-
# !/usr/bin/env python
import os
from common.tools import CommonTool
db = CommonTool.db_mysql_connect()


class ComputeTimeData:
    def __init__(self, catalog, datetime):
        self.catalog = catalog
        self.datetime = datetime
        self.db = db
        self.cursor = db.cursor()

    def compute_epg(self):
        table_name = os.path.splitdrive(self.catalog)[1]
        tn = table_name.split('\\')
        city_n = 'T0_' + tn[-3] + '_' + tn[-2] + '_' + tn[-1] + '_' + self.datetime
        self.__create_table_sql(next(self.__read_file_time()), city_n)
        vl_dict = dict()
        vl_dict['地市分布'] = dict()
        vl_dict['牌照方分布'] = dict()
        vl_dict['终端分布'] = dict()
        vl_dict['接入方式'] = dict()
        vl_dict['用户分布'] = dict()
        for i in self.__read_file_time():
            if len(i) > 33:
                if i[21] == '':
                    i[21] = 0
                if i[22] == '':
                    i[22] = 0

                if i[2] not in vl_dict['地市分布'].keys():
                    vl_dict['地市分布'][i[2]] = [1, int(i[21]), int(i[22])]
                    self.__insert_into_sql(i, city_n)
                else:
                    vl_dict['地市分布'][i[2]] = [
                        vl_dict['地市分布'][i[2]][0] + 1,
                        vl_dict['地市分布'][i[2]][1] + int(i[21]),
                        vl_dict['地市分布'][i[2]][2] + int(i[22])
                    ]
                    self.__insert_into_sql(i, city_n)

                if i[33] not in vl_dict['牌照方分布'].keys():
                    vl_dict['牌照方分布'][i[33]] = [1, int(i[21]), int(i[22])]
                else:
                    vl_dict['牌照方分布'][i[33]] = [
                        vl_dict['牌照方分布'][i[33]][0] + 1,
                        vl_dict['牌照方分布'][i[33]][1] + int(i[21]),
                        vl_dict['牌照方分布'][i[33]][2] + int(i[22])
                    ]

                if i[30] not in vl_dict['接入方式'].keys():
                    vl_dict['接入方式'][i[30]] = [1, int(i[21]), int(i[22])]

                else:
                    vl_dict['接入方式'][i[30]] = [
                        vl_dict['接入方式'][i[30]][0] + 1,
                        vl_dict['接入方式'][i[30]][1] + int(i[21]),
                        vl_dict['接入方式'][i[30]][2] + int(i[22])
                    ]

                if i[3] not in vl_dict['用户分布'].keys():
                    vl_dict['用户分布'][i[3]] = [1, int(i[21]), int(i[22])]
                else:
                    vl_dict['用户分布'][i[3]] = [
                        vl_dict['用户分布'][i[3]][0] + 1,
                        vl_dict['用户分布'][i[3]][1] + int(i[21]),
                        vl_dict['用户分布'][i[3]][2] + int(i[22])
                    ]

                if i[32] not in vl_dict['终端分布'].keys():
                    vl_dict['终端分布'][i[32]] = [1, int(i[21]), int(i[22])]
                else:
                    vl_dict['终端分布'][i[32]] = [
                        vl_dict['终端分布'][i[32]][0] + 1,
                        vl_dict['终端分布'][i[32]][1] + int(i[21]),
                        vl_dict['终端分布'][i[32]][2] + int(i[22])
                    ]

        self.__storage_data(vl_dict, city_n, tn)

    def compute_play(self):
        table_name = os.path.splitdrive(self.catalog)[1]
        tn = table_name.split('\\')

        vl_dict = dict()
        vl_dict['地市分布'] = dict()
        vl_dict['牌照方分布'] = dict()
        vl_dict['终端分布'] = dict()
        vl_dict['接入方式'] = dict()
        vl_dict['用户分布'] = dict()
        for i in self.__read_file_time():
            if len(i) > 33:
                if i[10] == '':
                    i[10] = 0
                if i[11] == '':
                    i[11] = 0

                if i[2] not in vl_dict['地市分布'].keys():
                    city_n = 'P0_' + tn[1] + '_' + tn[3] + '_' + self.datetime
                    vl_dict['地市分布'][i[2]] = [1, int(i[10]), int(i[11])]
                    self.__create_table_sql(i, city_n)
                    self.__insert_into_sql(i, city_n)
                else:
                    vl_dict['地市分布'][i[2]] = [
                        vl_dict['地市分布'][i[2]][0] + 1,
                        vl_dict['地市分布'][i[2]][1] + int(i[10]),
                        vl_dict['地市分布'][i[2]][2] + int(i[11])
                    ]
                    self.__insert_into_sql(i, city_n)

                if i[33] not in vl_dict['牌照方分布'].keys():
                    vl_dict['牌照方分布'][i[33]] = [1, int(i[10]), int(i[11])]
                else:
                    vl_dict['牌照方分布'][i[33]] = [
                        vl_dict['牌照方分布'][i[33]][0] + 1,
                        vl_dict['牌照方分布'][i[33]][1] + int(i[10]),
                        vl_dict['牌照方分布'][i[33]][2] + int(i[11])
                    ]

                if i[30] not in vl_dict['接入方式'].keys():
                    vl_dict['接入方式'][i[30]] = [1, int(i[10]), int(i[11])]

                else:
                    vl_dict['接入方式'][i[30]] = [
                        vl_dict['接入方式'][i[30]][0] + 1,
                        vl_dict['接入方式'][i[30]][1] + int(i[10]),
                        vl_dict['接入方式'][i[30]][2] + int(i[11])
                    ]

                if i[3] not in vl_dict['用户分布'].keys():
                    vl_dict['用户分布'][i[3]] = [1, int(i[10]), int(i[11])]
                else:
                    vl_dict['用户分布'][i[3]] = [
                        vl_dict['用户分布'][i[3]][0] + 1,
                        vl_dict['用户分布'][i[3]][1] + int(i[10]),
                        vl_dict['用户分布'][i[3]][2] + int(i[11])
                    ]

                if i[32] not in vl_dict['终端分布'].keys():
                    vl_dict['终端分布'][i[32]] = [1, int(i[10]), int(i[11])]
                else:
                    vl_dict['终端分布'][i[32]] = [
                        vl_dict['终端分布'][i[32]][0] + 1,
                        vl_dict['终端分布'][i[32]][1] + int(i[10]),
                        vl_dict['终端分布'][i[32]][2] + int(i[11])
                    ]
        self.__storage_data(vl_dict, city_n, tn)

    def compute_stutter(self):
        pass

    def __read_file_time(self):
        file_path = os.path.join(self.catalog, self.datetime)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as fin:
                for line in fin:
                    yield line.rstrip('\n').split('|')

    def __list_str_sql(self, data_list):

        return '|'.join(data_list).replace('|', """','""")

    def __inquiry_table_epg_name(self):
        table_name = os.path.splitdrive(self.catalog)[1]
        tn = table_name.split('\\')
        if tn[-3] == 'henan':
            return 't_mobile_ha_epg_%s' % self.datetime

    def __create_table_sql(self, data_list, tb_na):
        self.cursor.execute(u"""DROP TABLE IF EXISTS %s""" % tb_na)
        sql_t = None
        for v_l in range(len(data_list)):
            if sql_t == None:
                sql_t = """C_%s varchar(45)""" % v_l
            else:
                sql_t += """,C_%s varchar(45) """ % v_l
        sql = u"""CREATE TABLE %s (%s) ENGINE=InnoDB DEFAULT CHARSET=utf8;""" % (tb_na, sql_t)
        self.cursor.execute(sql)
        self.db.commit()

    def __insert_into_sql(self, data_list, tb_na):
        sql = u"""insert into %s values (%s)""" % (tb_na, str(data_list)[1:-1])
        self.cursor.execute(sql)
        self.db.commit()

    def __storage_data(self, dit, city_n, tn):
        for key, value in dit.items():
            if key == '地市分布':
                type_name = '0'
            elif key == '牌照方分布':
                type_name = '1'
            elif key == '终端分布':
                type_name = '2'
            elif key == '接入方式':
                type_name = '3'
            elif key == '用户分布':
                type_name = '4'
            else:
                type_name = 'eee'

            for keys, values in value.items():
                values[0] = int(values[0])
                values[1] = int(values[0])
                values[2] = int(values[0])

                if values[1] == 0:
                    proportion = None
                else:
                    proportion = values[2] / values[1]

                sql = u"""delete from %s where
                          RecordDate = date'%s'
                          and RecordCode = '%s'
                          and RecordType = %s""" % (self.__inquiry_table_epg_name(), tn[-1], keys, type_name)
                self.cursor.execute(sql)

                sql = u"""insert into %s values (%s, '%s', %s, '%s', %s, %s, %s, %s, Null)""" % \
                      (self.__inquiry_table_epg_name(), tn[-1], keys, type_name, city_n, values[0], \
                       values[1], values[2], proportion)
                self.cursor.execute(sql)
        self.db.commit()
        self.db.close()

