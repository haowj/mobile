# -*- coding: utf-8 -*-
from common.ChoiceVersion import Storage
from common.tools import CommonTool
from itertools import islice
from src.manufacturersn import StatisticalV01
from common.reads import ReadFile
import chardet
import pymysql
import csv
import time
import yaml
import os

filepath = r'C:\Users\pactera\Desktop'
# filepathr = r'C:\Users\pactera\Desktop\PERIODIC'
#filepathr = r'C:\Users\pactera\Desktop\xinjiang_20180503_PERIODIC'
# filepathr = r'C:\Users\pactera\Desktop\test\PERIODIC'
filepathr = r'E:\数据\henan_20180506\STBPERIODIC'
#
# filename = os.path.join(filepath, '分析报告%s.xls' % time.strftime("%Y%m%d%H%M%S", time.localtime()))
# print(filename)
# with open(filename, 'wb') as fin:
#     data_read = csv.writer(fin, delimiter=',')
#     data_read.writerow(['厂商', 'SN', '播放次数', '播放成功次数', '播放成功率', 'EPG请求次数', 'EPG请求成功次数',
#                         'EPG请求成功率', '牌照方', '统计日志条数'])

datafile = ReadFile(filepathr)
data = datafile.file_24()

read = StatisticalV01(data, filepath)
read.manufacturer_sn_v01()











# db = CommonTool(filepathr)
# data = db.file_list()
#
# data_storage = Storage(data, filepath)
# if 'V2.' or '20' in (list(islice(data, 1))[0][1]):
#     data_storage.v_2_out_excel()
# else:
#     data_storage.v_1_out_excel()
# 3-SN, 2-city, 30-接入方式, 64-终端, 64-软探针版本号, 33-牌照方编码, 36-用户信息

# for i in data:
#     print(i)
#     # i[1], i[3], i[2], i[30], i[64], i[63], i[32], i[33], i[36], i[31]
#
#     print(i[1], i[2], i[30])

# for i in data:
#     if 'V2.' in i[1] or '20' in i[1]:
#         data_storage.v_2_out_excel()
#         break
#     if 'V1.' in i[1] or '10' in i[1]:
#         data_storage.v_1_out_excel()
#         break
# if '20' in str(next(data)[1]) or 'V2.' in str(next(data)[1]):
#     print(1)
# else:
#     print(2)
# if 'V2.' or '20' in next(data)[1]:
#     data_storage.v_2_out_excel()
# else:
#     data_storage.v_1_out_excel()