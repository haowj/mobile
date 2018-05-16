# -*- coding: utf-8 -*-
from common.reads import ReadFile

class ReadFile:
    def __init__(self, data, catalog=None, city=None):
        self.data = data
        self.catalog = catalog
        self.city = city

    def cpname_epg_data(self):
        vl_dict = dict()
        vl_dict['地市分布'] = dict()
        vl_dict['牌照方分布'] = dict()
        vl_dict['终端分布'] = dict()
        vl_dict['用户分布'] = dict()
        vl_dict['接入方式'] = dict()
        vl_dict['播放方式'] = dict()
        vl_dict['机顶盒厂家'] = dict()

        # if '20' in str(next(data)[1]) or 'V2.' in str(next(data)[1]):
        for i in self.data:
            if len(i) < 33:
                continue
            if i[10] == '':
                i[10] = 0
            if i[11] == '':
                i[11] = 0
            if i[21] == '':
                i[21] = 0
            if i[22] == '':
                i[22] = 0

            if i[2] not in vl_dict['地市分布'].keys():
                vl_dict['地市分布'][i[2]] = [int(i[10]), int(i[11]), 1, int(i[21]), int(i[22])]
            else:
                vl_dict['地市分布'][i[2]] = [
                                            vl_dict['地市分布'][i[2]][0] + int(i[10]),
                                            vl_dict['地市分布'][i[2]][1] + int(i[11]),
                                            vl_dict['地市分布'][i[2]][2] + 1,
                                            vl_dict['地市分布'][i[2]][3] + int(i[21]),
                                            vl_dict['地市分布'][i[2]][4] + int(i[22])
                                        ]

            if i[33] not in vl_dict['牌照方分布'].keys():
                vl_dict['牌照方分布'][i[33]] = [int(i[10]), int(i[11]), 1, int(i[21]), int(i[22])]
            else:
                vl_dict['牌照方分布'][i[33]] = [
                                            vl_dict['牌照方分布'][i[33]][0] + int(i[10]),
                                            vl_dict['牌照方分布'][i[33]][1] + int(i[11]),
                                            vl_dict['牌照方分布'][i[33]][2] + 1,
                                            vl_dict['牌照方分布'][i[33]][3] + int(i[21]),
                                            vl_dict['牌照方分布'][i[33]][4] + int(i[22])
                                        ]

            if i[30] not in vl_dict['接入方式'].keys():
                vl_dict['接入方式'][i[30]] = [int(i[10]), int(i[11]), 1, int(i[21]), int(i[22])]
            else:
                vl_dict['接入方式'][i[30]] = [
                                            vl_dict['接入方式'][i[30]][0] + int(i[10]),
                                            vl_dict['接入方式'][i[30]][1] + int(i[11]),
                                            vl_dict['接入方式'][i[30]][2] + 1,
                                            vl_dict['接入方式'][i[30]][3] + int(i[21]),
                                            vl_dict['接入方式'][i[30]][4] + int(i[22])
                                        ]

            if i[3] not in vl_dict['用户分布'].keys():
                vl_dict['用户分布'][i[3]] = [int(i[10]), int(i[11]), 1, int(i[21]), int(i[22])]
            else:
                vl_dict['用户分布'][i[3]] = [
                                            vl_dict['用户分布'][i[3]][0] + int(i[10]),
                                            vl_dict['用户分布'][i[3]][1] + int(i[11]),
                                            vl_dict['用户分布'][i[3]][2] + 1,
                                            vl_dict['用户分布'][i[3]][3] + int(i[21]),
                                            vl_dict['用户分布'][i[3]][4] + int(i[22])
                                        ]

            if i[32] not in vl_dict['机顶盒厂家'].keys():
                vl_dict['机顶盒厂家'][i[32]] = [int(i[10]), int(i[11]), 1, int(i[21]), int(i[22]), i[33]
                                            ]
            else:
                vl_dict['机顶盒厂家'][i[32]] = [
                                            vl_dict['机顶盒厂家'][i[32]][0] + int(i[10]),
                                            vl_dict['机顶盒厂家'][i[32]][1] + int(i[11]),
                                            vl_dict['机顶盒厂家'][i[32]][2] + 1,
                                            vl_dict['机顶盒厂家'][i[32]][3] + int(i[21]),
                                            vl_dict['机顶盒厂家'][i[32]][4] + int(i[22]),
                                            i[33]
                                        ]


class OsCreateCatalog(ReadFile):
    """
       创建多级目录继续日志文件拆分
       一级目录：省份
       二级目录：时刻-24个时间段划分
       三级目录：日志类型（001-资源原始数据，002-运行周期原始数据，003-收视原始数据，004-告警原始数据）
       四级目录：日期
    """
    def __init__(self, catalog, city, types, date):
        super(OsCreateCatalog, self).__init__(catalog)
        self.catalog = catalog
        self.city = city
        self.type = types
        self.date = date

    def read_file_00(self):
        pass