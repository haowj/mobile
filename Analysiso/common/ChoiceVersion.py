# -*- coding: utf-8 -*-

"""
Created on 2018-5-8

@author: wj

"""

import os
import xlwt
import time


class Storage:
    def __init__(self, data, catalog):
        self.data = data
        self.catalog = catalog

    def v_2_out_excel(self):
        vl_dict = dict()
        vl_dict['软探针版本'] = dict()
        vl_dict['设备类型'] = dict()
        vl_dict['设备SN'] = dict()
        for i in self.data:
            if i[10] == '':
                i[10] = 0
            if i[11] == '':
                i[11] = 0
            if i[-2] == '':
                i[-2] = 'null'

            if i[-2] not in vl_dict['软探针版本'].keys():
                vl_dict['软探针版本'][i[-2]] = [int(i[10]), int(i[11]), 1, int(i[21]), int(i[22])]
            else:
                vl_dict['软探针版本'][i[-2]] = [
                                            vl_dict['软探针版本'][i[-2]][0] + int(i[10]), \
                                            vl_dict['软探针版本'][i[-2]][1] + int(i[11]), \
                                            vl_dict['软探针版本'][i[-2]][2] + 1, \
                                            vl_dict[u'软探针版本'][i[-2]][3] + int(i[21]), \
                                            vl_dict[u'软探针版本'][i[-2]][4] + int(i[22])
                                           ]
            if i[-1] not in vl_dict['设备类型'].keys():
                vl_dict['设备类型'][i[-1]] = [int(i[10]), int(i[11]), 1, int(i[21]), int(i[22])]
            else:
                vl_dict['设备类型'][i[-1]] = [
                                            vl_dict['设备类型'][i[-1]][0] + int(i[10]), \
                                            vl_dict['设备类型'][i[-1]][1] + int(i[11]), \
                                            vl_dict['设备类型'][i[-1]][2] + 1, \
                                            vl_dict['设备类型'][i[-1]][3] + int(i[21]), \
                                            vl_dict['设备类型'][i[-1]][4] + int(i[22])
                                            ]
            # if i[3] not in vl_dict['设备SN'].keys():
            #     vl_dict['设备SN'][i[3]] = [int(i[10]), int(i[11]), number, int(i[21]), int(i[22])]
            # else:
            #     vl_dict['设备SN'][i[3]] = [vl_dict['设备SN'][i[3]][0] + int(i[10]), \
            #                                vl_dict['设备SN'][i[3]][1] + int(i[11]), \
            #                                vl_dict['设备SN'][i[3]][2] + 1, \
            #                                vl_dict['设备SN'][i[3]][3] + int(i[21]), \
            #                                vl_dict['设备SN'][i[3]][4] + int(i[22])
            #                               ]

        # print(len(vl_dict['设备SN'].keys()))
        workbook = xlwt.Workbook(encoding='utf-8')

        worksheet = workbook.add_sheet(u'软探针版本')
        worksheet1 = workbook.add_sheet(u'设备类型')
        worksheet2 = workbook.add_sheet(u'设备SN')
        worksheet.write(0, 0, u'软探针版本号')
        worksheet.write(0, 1, u'总播放次数')
        worksheet.write(0, 2, u'播放成功次数')
        worksheet.write(0, 3, u'统计日志条数')
        worksheet.write(0, 4, u'成功占比')
        worksheet.write(0, 5, u'EPG请求总次数')
        worksheet.write(0, 6, u'EPG请求成功次数')
        worksheet.write(0, 7, u'EPG请求成功占比')
        worksheet1.write(0, 0, u'设备类型')
        worksheet1.write(0, 1, u'总播放次数')
        worksheet1.write(0, 2, u'播放成功次数')
        worksheet1.write(0, 3, u'统计日志条数')
        worksheet1.write(0, 4, u'成功占比')
        worksheet1.write(0, 5, u'EPG请求总次数')
        worksheet1.write(0, 6, u'EPG请求成功次数')
        worksheet1.write(0, 7, u'EPG请求成功占比')
        worksheet2.write(0, 0, u'设备SN')
        worksheet2.write(0, 1, u'总播放次数')
        worksheet2.write(0, 2, u'播放成功次数')
        worksheet2.write(0, 3, u'统计日志条数')
        worksheet2.write(0, 4, u'成功占比')
        worksheet2.write(0, 5, u'EPG请求总次数')
        worksheet2.write(0, 6, u'EPG请求成功次数')
        worksheet2.write(0, 7, u'EPG请求成功占比')

        con = 1
        for vl in vl_dict['软探针版本'].keys():

            worksheet.write(con, 0, vl)
            worksheet.write(con, 1, vl_dict['软探针版本'][vl][0])
            worksheet.write(con, 2, vl_dict['软探针版本'][vl][1])
            worksheet.write(con, 3, vl_dict['软探针版本'][vl][2])
            if vl_dict['软探针版本'][vl][0] == 0:
                worksheet.write(con, 4, None)
            else:
                worksheet.write(con, 4, vl_dict['软探针版本'][vl][1] / vl_dict['软探针版本'][vl][0])
            worksheet.write(con, 5, vl_dict['软探针版本'][vl][3])
            worksheet.write(con, 6, vl_dict['软探针版本'][vl][4])
            if vl_dict['软探针版本'][vl][3] == 0:
                worksheet.write(con, 7, None)
            else:
                worksheet.write(vl_dict['软探针版本'][vl][4] / vl_dict['软探针版本'][vl][3])
            con += 1

        cons = 1
        for vl in vl_dict['设备类型'].keys():
            # print(vl, vl_dict['设备类型'][vl][0])
            worksheet1.write(cons, 0, vl)
            worksheet1.write(cons, 1, vl_dict['设备类型'][vl][0])
            worksheet1.write(cons, 2, vl_dict['设备类型'][vl][1])
            worksheet1.write(cons, 3, vl_dict['设备类型'][vl][2])
            # worksheet.write(con, 4, '=C%s/B%s' % (con, con))
            if vl_dict['设备类型'][vl][0] == 0:
                worksheet1.write(cons, 4, None)
            else:
                worksheet1.write(cons, 4, vl_dict['设备类型'][vl][1] / vl_dict['设备类型'][vl][0])
            worksheet1.write(cons, 5, vl_dict['设备类型'][vl][3])
            worksheet1.write(cons, 6, vl_dict['设备类型'][vl][4])
            if vl_dict['设备类型'][vl][3] == 0:
                worksheet1.write(cons, 7, None)
            else:
                worksheet1.write(cons, 7, vl_dict['设备类型'][vl][4] / vl_dict['设备类型'][vl][3])

            cons += 1
        # cone = 1
        # for vl in vl_dict['设备SN'].keys():
        #
        #     worksheet2.write(cone, 0, vl)
        #     worksheet2.write(cone, 1, vl_dict['设备SN'][vl][0])
        #     worksheet2.write(cone, 2, vl_dict['设备SN'][vl][1])
        #     worksheet2.write(cone, 3, vl_dict['设备SN'][vl][2])
        #     # worksheet.write(con, 4, '=C%s/B%s' % (con, con))
        #     if vl_dict['设备SN'][vl][0] == 0:
        #         worksheet2.write(cone, 4, 0)
        #     else:
        #         worksheet2.write(cone, 4, vl_dict['设备SN'][vl][1] / vl_dict['设备SN'][vl][0])
        #     worksheet2.write(cone, 5, vl_dict['设备SN'][vl][3])
        #     worksheet2.write(cone, 6, vl_dict['设备SN'][vl][4])
        #     if vl_dict['设备SN'][vl][3] == 0:
        #         worksheet2.write(cone, 7, None)
        #     else:
        #         worksheet2.write(cone, 7, vl_dict['设备SN'][vl][4] / vl_dict['设备SN'][vl][3])
        #     cone += 1

        workbook.save(os.path.join(self.catalog, '分析报告%s.xls' % time.strftime("%Y%m%d%H%M%S", time.localtime())))

    def v_1_out_excel(self):
        vl_dict = dict()
        vl_dict['牌照方编码'] = dict()
        for i in self.data:
            if i[10] == '':
                i[10] = 0
            if i[11] == '':
                i[11] = 0
            if i[21] == '':
                i[21] = 0
            if i[22] == '':
                i[22] = 0
            if i[-1] == '':
                i[-1] = 'eeee'

            if i[-1] not in vl_dict['牌照方编码'].keys():
                vl_dict['牌照方编码'][i[-1]] = [int(i[10]), int(i[11]), 1, int(i[21]), int(i[22])]
            else:
                vl_dict['牌照方编码'][i[-1]] = [vl_dict['牌照方编码'][i[-1]][0] + int(i[10]), vl_dict['牌照方编码'][i[-1]][1] \
                                           + int(i[11]), vl_dict['牌照方编码'][i[-1]][2] + 1,
                                           vl_dict['牌照方编码'][i[-1]][3] + int(i[21]), \
                                           vl_dict['牌照方编码'][i[-1]][4] + int(i[22])]

            # if i[-1] not in vl_dict['牌照方编码'].keys():
            #     vl_dict['牌照方编码'][i[-1]] = [int(i[10]), int(i[11]), 1]
            # else:
            #     vl_dict['牌照方编码'][i[-1]] = [vl_dict['牌照方编码'][i[-1]][0] + int(i[10]), \
            #                                vl_dict['牌照方编码'][i[-1]][1] + int(i[11]), \
            #                                vl_dict['牌照方编码'][i[-1]][2] + 1]
        workbook = xlwt.Workbook(encoding='utf-8')

        worksheet = workbook.add_sheet(u'牌照方编码')
        worksheet.write(0, 0, u'牌照方编码')
        worksheet.write(0, 1, u'总播放次数')
        worksheet.write(0, 2, u'播放成功次数')
        worksheet.write(0, 3, u'统计日志条数')
        worksheet.write(0, 4, u'播放成功占比')
        worksheet.write(0, 5, u'EPG请求总次数')
        worksheet.write(0, 6, u'EPG请求成功次数')
        worksheet.write(0, 7, u'EPG请求成功占比')
        con = 1
        for vl in vl_dict['牌照方编码'].keys():

            worksheet.write(con, 0, vl)
            worksheet.write(con, 1, vl_dict['牌照方编码'][vl][0])
            worksheet.write(con, 2, vl_dict['牌照方编码'][vl][1])
            worksheet.write(con, 3, vl_dict['牌照方编码'][vl][2])
            # worksheet.write(con, 4, '=C%s/B%s' % (con, con))
            if vl_dict['牌照方编码'][vl][0] == 0:
                worksheet.write(con, 4, None)
            else:
                worksheet.write(con, 4, vl_dict['牌照方编码'][vl][1] / vl_dict['牌照方编码'][vl][0])
            worksheet.write(con, 5, vl_dict['牌照方编码'][vl][3])
            worksheet.write(con, 6, vl_dict['牌照方编码'][vl][4])
            if vl_dict['牌照方编码'][vl][3] == 0:
                worksheet.write(con, 7, None)
            else:
                worksheet.write(con, 7, vl_dict['牌照方编码'][vl][4] / vl_dict['牌照方编码'][vl][3])
            con += 1

        workbook.save(os.path.join(self.catalog, '分析报告%s.xls' % time.strftime("%Y%m%d%H%M%S", time.localtime())))