# -*- coding: utf-8 -*-

from common.tools import CommonTool
from common.obj_compute import ComputeTimeData
# data = CommonTool(r'E:\数据\henan_20180506\PERIODIC', r'E:\bit')
#
# data.file_list()

data = ComputeTimeData(r'E:\bit\henan\002\20180506', '00')
data.compute_epg()



