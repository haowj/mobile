# -*- coding: utf-8 -*-
import threading
from common.tools import CommonTool


def thing_fun_sk(p_1, p_2):
    data = CommonTool(p_1, p_2)
    data.file_list()


def thing_fun_sn(p_1, p_2):
    data = CommonTool(p_1, p_2)
    data.file_list()


def run_fun(path):
    f00 = threading.Thread(target=thing_fun_sk, args=(path, '00'))
    f01 = threading.Thread(target=thing_fun_sk, args=(path, '01'))
    f02 = threading.Thread(target=thing_fun_sk, args=(path, '02'))
    f03 = threading.Thread(target=thing_fun_sk, args=(path, '03'))
    f04 = threading.Thread(target=thing_fun_sk, args=(path, '04'))
    f05 = threading.Thread(target=thing_fun_sk, args=(path, '05'))
    f06 = threading.Thread(target=thing_fun_sk, args=(path, '06'))
    f07 = threading.Thread(target=thing_fun_sk, args=(path, '07'))
    f08 = threading.Thread(target=thing_fun_sk, args=(path, '08'))
    f09 = threading.Thread(target=thing_fun_sk, args=(path, '09'))
    f10 = threading.Thread(target=thing_fun_sk, args=(path, '10'))
    f11 = threading.Thread(target=thing_fun_sk, args=(path, '11'))
    f12 = threading.Thread(target=thing_fun_sk, args=(path, '12'))
    f13 = threading.Thread(target=thing_fun_sk, args=(path, '13'))
    f14 = threading.Thread(target=thing_fun_sk, args=(path, '14'))
    f15 = threading.Thread(target=thing_fun_sk, args=(path, '15'))
    f16 = threading.Thread(target=thing_fun_sk, args=(path, '16'))
    f17 = threading.Thread(target=thing_fun_sk, args=(path, '17'))
    f18 = threading.Thread(target=thing_fun_sk, args=(path, '18'))
    f19 = threading.Thread(target=thing_fun_sk, args=(path, '19'))
    f20 = threading.Thread(target=thing_fun_sk, args=(path, '20'))
    f21 = threading.Thread(target=thing_fun_sk, args=(path, '21'))
    f22 = threading.Thread(target=thing_fun_sk, args=(path, '22'))
    f23 = threading.Thread(target=thing_fun_sk, args=(path, '23'))
    f00.start()
    f01.start()
    f02.start()
    f03.start()
    f04.start()
    f05.start()
    f06.start()
    f07.start()
    f08.start()
    f09.start()
    f10.start()
    f11.start()
    f12.start()
    f13.start()
    f14.start()
    f15.start()
    f16.start()
    f17.start()
    f18.start()
    f19.start()
    f20.start()
    f21.start()
    f22.start()
    f23.start()

    f00.join()
    f01.join()
    f02.join()
    f03.join()
    f04.join()
    f05.join()
    f06.join()
    f07.join()
    f08.join()
    f09.join()
    f10.join()
    f11.join()
    f12.join()
    f13.join()
    f14.join()
    f15.join()
    f16.join()
    f17.join()
    f18.join()
    f19.join()
    f20.join()
    f21.join()
    f22.join()
    f23.join()


