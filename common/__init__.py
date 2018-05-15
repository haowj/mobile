# -*- coding: utf-8 -*-
import yaml
from common.tools import CommonTool
from common.reads import ReadFile
from common.ReadLogCoun import ReadFile as _Read

path = r'C:\Users\pactera\Desktop\henan_20180506\PERIODIC'

file = ReadFile(path)
data = file.file_00()

ott = _Read(data)
ott.cpname_epg_data()

# fr = open('model', 'w', encoding="utf-8")
# yaml.dump(ptdata, fr)
# yaml.load()
# fr.close()
