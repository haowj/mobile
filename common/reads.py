# -*- coding: utf-8 -*-
import os
import gzip


class ReadFile(object):
    def __init__(self, catalog):
        self.catalog = catalog

    def disassembly_file(self):
        filename_list = os.listdir(self.catalog)
        for i in range(len(filename_list)):
            if filename_list[i][-2:] == 'gz':
                path = os.path.join(self.catalog, filename_list[i])
                if os.path.isfile(path):
                    yield self.__read_file(path)

    def file_00(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'00':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_01(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'01':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_02(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'02':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_03(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'03':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_04(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'04':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_05(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'05':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_06(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'06':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_07(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'07':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_08(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'08':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_09(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'09':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_10(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'10':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_11(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'11':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_12(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'12':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_13(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'13':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_14(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'14':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_15(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'15':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_16(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'16':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_17(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'17':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_18(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'18':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_19(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'19':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_20(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'20':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_21(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'21':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_22(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'22':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_23(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    if line[11:13] == b'23':
                        try:
                            yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                        except EOFError:
                            yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def file_24(self):
        for data in self.__catalog_file():
            if getattr(data, '__iter__', None):
                for line in data:
                    try:
                        yield line.decode(encoding='utf-8').rstrip('\n').split('|')
                    except EOFError:
                        yield line.decode(encoding='gbk').rstrip('\n').split('|')
            else:
                print('data value is none')

    def __catalog_file(self):
        filename_list = os.listdir(self.catalog)
        for i in range(len(filename_list)):
            if filename_list[i][-2:] == 'gz':
                path = os.path.join(self.catalog, filename_list[i])
                if os.path.isfile(path):
                    yield self.__read_file(path)

    def __read_file(self, path):
        if os.path.exists(path):
            with gzip.open(path, 'r') as f:
                try:
                    for line in f:
                        yield line
                except EOFError:
                    pass
        else:
            print('the path [{}] is not exist!'.format(path))




