# -*- coding: utf-8 -*-

from common.tools import CommonTool
import time
db = CommonTool.db_mysql_connect()
cursor = db.cursor()
#
# sql = u"""
#     insert into T_MOBILE_CODE (CodeID, CodeName, CodeType) values (%s, %s, 1)
# """ % ()
sql = u"""
    insert into T_MOBILE_CITY_CODE (CityCode, CityName) values ("%s", "%s")
"""
# data = ['城市编码', '牌照方编码', '设备型号', '接入方式_无线', '接入方式_有线', '播放方式_直播', '播放方式_点播']
# for i, val in enumerate(data):
#     cursor.execute(sql % (i, val))
#
sql_2 = u"""
    select * from T_MOBILE_SN_CODE where SnCode = '%s'
"""
inquiry_sql = u"""
    select * from t_mobile_sn_code order by snid desc
"""

sql_1 = u"""
    select * from t_mobile_city_code where cityname like '%河%'
"""
sql = u"""
    insert into T_MOBILE_SN_CODE (SnCode, SNID) values ("%s", "%s")
"""


sn = "00470300000288000018F09CD70DA9C9"
# filepath = r'C:\Users\pactera\Desktop\ctiy.txt'
filepath = r'C:\Users\pactera\Desktop\henan_20180506\PERIODIC'
# dlist = list()
# with open(filepath, 'r', encoding='utf8') as fin:
#     for i in fin:
#         dlist.append(i.rstrip("\t\n").rstrip("\n").split(" "))
# for i in dlist:
#     while '' in i:
#         i.remove('')
# for i in dlist:
#     print(sql % (i[1], i[0]))
#     cursor.execute(sql % (i[1], i[0]))
cursor.execute(inquiry_sql)
data = CommonTool.data_one_list(cursor)
print(next(data))
# data = cursor.fetchall()
# print(data)
FileRead = CommonTool(filepath)
file = FileRead.file_list()
print(time.strftime("%Y%m%d%H%M%S", time.localtime()))
for i in file:

    if len(i) < 5:
        print(i)
    # if not CommonTool.data_all_list(sql_2 % i[3]):
    #
    #     cursor.execute(sql % (i[3]), CommonTool.str_numeric(next(data)+1))
    # print(sql % (i[3], CommonTool.str_numeric(0)))
    # cursor.execute(sql % (i[3], CommonTool.str_numeric(0)))
    # data = CommonTool.data_one_list(cursor)
    # if not data:
    #     print(data)

print(time.strftime("%Y%m%d%H%M%S", time.localtime()))
# db.commit()
# db.close()