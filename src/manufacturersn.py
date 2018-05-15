# -*- coding: utf-8 -*-
import csv
import time
import os


class StatisticalV01:
    def __init__(self, data, catalog):
        self.data = data
        self.catalog = catalog

    def manufacturer_sn_v01(self):
        vl_dict = {}
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

            # if vl_dict == {}:
            #     vl_dict[i[32]] = dict()
            #     vl_dict[i[32]][i[3]] = [int(i[10]), int(i[11]), 1, int(i[21]), int(i[22]), i[33]]
            #     print(vl_dict)
            #     break
            # elif i[32] in vl_dict.keys() and i[3] in vl_dict[i[32]].keys():
            #     vl_dict[i[32]][i[3]] = [
            #         vl_dict[i[32]][i[3]][0] + int(i[10]),
            #         vl_dict[i[32]][i[3]][1] + int(i[11]),
            #         vl_dict[i[32]][i[3]][2] + 1,
            #         vl_dict[i[32]][i[3]][3] + int(i[21]),
            #         vl_dict[i[32]][i[3]][4] + int(i[22]),
            #         i[33]
            #     ]
            #     print(vl_dict)
            # else:
            #     vl_dict[i[32]] = dict()
            #     vl_dict[i[32]][i[3]] = [int(i[10]), int(i[11]), 1, int(i[21]), int(i[22]), i[33]]
            #     print(vl_dict)

            if i[32] not in vl_dict.keys():
                vl_dict[i[32]] = dict()
                vl_dict[i[32]][i[3]] = [int(i[10]), int(i[11]), 1, int(i[21]), int(i[22]), i[33]]

            elif i[3] in vl_dict[i[32]].keys():
                vl_dict[i[32]][i[3]] = [
                    vl_dict[i[32]][i[3]][0] + int(i[10]),
                    vl_dict[i[32]][i[3]][1] + int(i[11]),
                    vl_dict[i[32]][i[3]][2] + 1,
                    vl_dict[i[32]][i[3]][3] + int(i[21]),
                    vl_dict[i[32]][i[3]][4] + int(i[22]),
                    i[33]
                ]

            else:
                vl_dict[i[32]][i[3]] = [int(i[10]), int(i[11]), 1, int(i[21]), int(i[22]), i[33]]

        filename = os.path.join(self.catalog, '分析报告%s.csv' % time.strftime("%Y%m%d%H%M%S", time.localtime()))
        with open(filename, 'w', newline='') as fin:
            data_read = csv.writer(fin, delimiter=',')
            data_read.writerow(['厂商', 'SN', '播放次数', '播放成功次数', '播放成功率', 'EPG请求次数', 'EPG请求成功次数',
                                'EPG请求成功率', '牌照方', '统计日志条数'])
            for key, value in vl_dict.items():
                for i, j in value.items():
                    if j[0] > 150 and (j[1] / j[0]) < 0.5:
                        if j[3] == 0:
                            proportion = None
                        else:
                            proportion = j[4] / j[3]
                        data_read.writerow([key, i, j[0], j[1], j[1] / j[0], j[3], j[4], proportion, j[5], j[2]])