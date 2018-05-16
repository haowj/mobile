# -*- coding: utf-8 -*-

from common.tools import CommonTool
catalog = r'E:\数据\河南\001'

db = CommonTool(catalog)
data = db.file_list()
for i in data:
    print(i)