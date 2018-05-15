# -*- coding: utf-8 -*-
import os
import time
import csv

from src.manufacturersn import StatisticalV01
from common.reads import ReadFile

filepath = r'C:\Users\pactera\Desktop'
filepathr = r'E:\数据\henan_20180425\PERIODIC'


datafile = ReadFile(filepathr)
data = datafile.file_24()


read = StatisticalV01(data, filepath)
read.manufacturer_sn_v01()


# filename = os.path.join(filepath, '分析报告%s.csv' % time.strftime("%Y%m%d%H%M%S", time.localtime()))
# print(filename)
# with open(filename, 'wb') as fin:
#     data_read = csv.writer(fin, delimiter=',')
#     data_read.writerow([bytes("厂商", encoding="utf8"),
#                         bytes("SN", encoding="utf8"),
#                         bytes("播放次数", encoding="utf8"),
#                         bytes("播放成功次数", encoding="utf8"),
#                         bytes("播放成功率", encoding="utf8"),
#                         bytes("EPG请求次数", encoding="utf8"),
#                         bytes("EPG请求成功次数", encoding="utf8"),
#                         bytes("EPG请求成功率", encoding="utf8"),
#                         bytes("牌照方", encoding="utf8"),
#                         bytes("统计日志条数", encoding="utf8")])

