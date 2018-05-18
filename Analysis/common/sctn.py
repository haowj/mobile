# -*- coding: utf-8 -*-
import os
from common.tools import CommonTool
db = CommonTool.db_mysql_connect()


class CreateSelectTN:
    def __init__(self, catalog, data_list):
        self.catalog = catalog
        self.catalog = catalog
        if os.path.basename(catalog) == 'ALARM':
            self.BASE_TOW = '004'
        elif os.path.basename(catalog) == 'PERIODIC':
            self.BASE_TOW = '002'
        elif os.path.basename(catalog) == 'PROGRAMINFO':
            self.BASE_TOW = '003'
        else:
            self.BASE_TOW = '001'
        self.db = db
        self.cursor = self.db.cursor()
        self.data_list = data_list
        d = os.path.splitdrive(catalog)
        d = d[1].split('\\')
        self.base_city_date = d[-2].split('_')

    def obtain_sn_tn(self):
        tn = 'SN_' + self.BASE_TOW + '_' + self.base_city_date[0] + '_' + self.base_city_date[1]
        self.cursor.execute(u"""DROP TABLE IF EXISTS %s""" % tn)
        sql_t = None
        for v_l in range(len(self.data_list)):
            if sql_t == None:
                sql_t = """C_%s varchar(45)""" % v_l
            else:
                sql_t += """,C_%s varchar(45) """ % v_l
        sql = u"""CREATE TABLE %s (%s) ENGINE=InnoDB DEFAULT CHARSET=utf8;""" % (tn, sql_t)
        self.cursor.execute(sql)
        self.db.commit()
        return tn

