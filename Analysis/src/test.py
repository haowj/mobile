# -*- coding: utf-8 -*-
from common.tools import CommonTool

data = CommonTool(r'E:\数据\hubei_20180425\PERIODIC')
data_file = data.file_sn_list()


def test_yi():
    for d in range(9):
        yield d
d = test_yi()


def tb():
    while 1:
        try:
            print(next(d))
        except StopIteration:
            break


if __name__ == "__main__":
    tb()