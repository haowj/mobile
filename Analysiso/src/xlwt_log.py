# -*- coding: utf-8 -*-
import os
import xlwt
from common.tools import CommonTool


catalog = r'C:\Users\pactera\Desktop\xinjiang_20180503_PERIODIC'

vl_dict = dict()
vl_dict['设备SN'] = dict()
number = 1
db = CommonTool(catalog)
data = db.file_list()
for i in data:
    if i[-2] == '':
        i[-2] = 'null'
    if i[10] == '':
        i[10] = 0
    if i[11] == '':
        i[11] = 0
    # int(i[10]), int(i[11])
    # if not hasattr(vl_dict, i[-2]):
    #     vl_dict[i[-2]] = [int(i[10]), int(i[11]), int(1)]
    #
    # else:
    #     vl_dict[i[-2]] = [vl_dict[i[-2]][0] + int(i[10]), vl_dict[i[-2]][1] + int(i[11]), vl_dict[i[-2]][2] + 1]

    if i[3] not in vl_dict['设备SN'].keys():
        vl_dict['设备SN'][i[3]] = [int(i[10]), int(i[11]), number]
    else:
        vl_dict['设备SN'][i[3]] = [vl_dict['设备SN'][i[3]][0] + int(i[10]), \
                                   vl_dict['设备SN'][i[3]][1] + int(i[11]), \
                                   vl_dict['设备SN'][i[3]][2] + 1]

print(len(vl_dict['设备SN'].keys()))
workbook = xlwt.Workbook(encoding='utf-8')
worksheet2 = workbook.add_sheet(u'设备SN')
worksheet2.write(0, 0, u'设备SN')
worksheet2.write(0, 1, u'总播放次数')
worksheet2.write(0, 2, u'播放成功次数')
worksheet2.write(0, 3, u'统计日志条数')
worksheet2.write(0, 4, u'成功占比')

cone = 1
for vl in vl_dict['设备SN'].keys():

    worksheet2.write(cone, 0, vl)
    worksheet2.write(cone, 1, vl_dict['设备SN'][vl][0])
    worksheet2.write(cone, 2, vl_dict['设备SN'][vl][1])
    worksheet2.write(cone, 3, vl_dict['设备SN'][vl][2])
    # worksheet.write(con, 4, '=C%s/B%s' % (con, con))
    if vl_dict['设备SN'][vl][0] == 0:
        worksheet2.write(cone, 4, 0)
    else:
        worksheet2.write(cone, 4, vl_dict['设备SN'][vl][1] / vl_dict['设备SN'][vl][0])
    cone += 1

workbook.save(os.path.join(catalog, 'model1.xls'))
# workbook = xlwt.Workbook(encoding='utf-8')
# worksheet = workbook.add_sheet('My Worksheet')
# # style = xlwt.XFStyle() # 初始化样式
# # font = xlwt.Font() # 为样式创建字体
# # font.name = 'Times New Roman'
# # font.bold = True # 黑体
# # font.underline = True # 下划线
# # font.italic = True # 斜体字
# # style.font = font # 设定样式
# worksheet.write(0, 0, u'探针版本号')
# # worksheet.write(0, 1, u'设备类型')
# # worksheet.write(0, 2, u'设备SN')
# worksheet.write(0, 3, u'总播放次数')
# worksheet.write(0, 4, u'成功播放次数')
# worksheet.write(0, 5, u'统计条数')
#
# # for i in range(1, len(vl_dict)):
# #     worksheet.write(0, 0, u'探针版本号')
# #     worksheet.write(0, 1, u'设备类型')
# #     worksheet.write(0, 2, u'设备SN')
# #     worksheet.write(0, 3, u'总播放次数')
# #     worksheet.write(0, 4, u'成功播放次数')
# #     worksheet.write(0, 5, u'统计条数')
#
# i = 1
# for keys, value in vl_dict.items():
#     worksheet.write(i, 0, keys)
#     # worksheet.write(i, 1, u'设备类型')
#     # worksheet.write(i, 2, u'设备SN')
#     worksheet.write(i, 3, value[0])
#     worksheet.write(i, 4, value[1])
#     worksheet.write(i, 5, value[2])
#
#
# workbook.save('formatting.xls')
# row
# index
# was
# 65536, not allowed
# by