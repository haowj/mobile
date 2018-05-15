# -*- coding: utf-8 -*-

from common.tools import CommonTool

path = r'E:\数据\河南\001'

db = CommonTool(path)
data = db.file_list()


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
