# -*- coding: utf-8 -*-
from common.ChoiceVersion import Storage
from common.tools import CommonTool
from itertools import islice
import chardet
import pymysql
import csv
import yaml


filepath = r'C:\Users\pactera\Desktop'
# filepathr = r'C:\Users\pactera\Desktop\PERIODIC'
#filepathr = r'C:\Users\pactera\Desktop\xinjiang_20180503_PERIODIC'
# filepathr = r'C:\Users\pactera\Desktop\test\PERIODIC'
filepathr = r'C:\Users\pactera\Desktop\henan_20180506\PERIODIC'

db = CommonTool(filepathr)
data = db.file_list()

# data_storage = Storage(data, filepath)
# if 'V2.' or '20' in (list(islice(data, 1))[0][1]):
#     data_storage.v_2_out_excel()
# else:
#     data_storage.v_1_out_excel()
# 3-SN, 2-city, 30-接入方式, 64-终端, 64-软探针版本号, 33-牌照方编码, 36-用户信息
for i in data:
    print(i[3])
    # i[1], i[3], i[2], i[30], i[64], i[63], i[32], i[33], i[36], i[31]
    #
    # print(i[1], i[2], i[30])
    break
# for i in data:
#     if 'V2.' in i[1] or '20' in i[1]:
#         data_storage.v_2_out_excel()
#         break
#     if 'V1.' in i[1] or '10' in i[1]:
#         data_storage.v_1_out_excel()
#         break
#
