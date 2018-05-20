# -*- coding: utf-8 -*-
from common.sctn import CreateSelectTN

data = CreateSelectTN(r'D:\hena')
fie = data.read_file(r'D:\hena\00')

db_name = 't_001'
sql_ = ""
sql = u"""insert into %s values %s"""
# for i in fie:
#     print(i)
try:
    for i in range(7600):
         sql_ += "," + str(tuple(next(fie)))
    print(sql % (db_name, sql_))
except StopIteration:
    print(sql % (db_name, sql_))