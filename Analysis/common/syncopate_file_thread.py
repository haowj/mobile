# -*- coding: utf-8 -*-
import threading
from common.tools import CommonTool
from common.sctn import CreateSelectTN
# 互斥锁的声明
mutex_lock = threading.RLock()
data = CommonTool(r'C:\Users\wj\Desktop\hena_20180503\PERIODIC')
data_file = data.file_sn_list()
db_t = CreateSelectTN(r'C:\Users\wj\Desktop\hena_20180503\PERIODIC', next(data_file))
db_name = db_t.obtain_sn_tn()
db = CommonTool.db_mysql_connect()
cursor = db.cursor()


class SyncopateTools(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name

    def run(self):
        global data_file
        global db_name
        global cursor
        global db
        while 1:
            mutex_lock.acquire()
            sql_ = ""
            sql = u"""insert into %s values %s"""
            try:
                for i in range(7600):
                     sql_ += "," + str(tuple(next(data_file)))
                cursor.execute(sql % (db_name, sql_[1:]))
                db.commit()
            except StopIteration:
                cursor.execute(sql % (db_name, sql_[1:]))
                db.commit()
                break
            mutex_lock.release()
        mutex_lock.release()
        db.commit()


if __name__ == "__main__":
    threads = []
    import time
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    for i in range(0, 15):
        thread = SyncopateTools(i)
        threads.append(thread)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))