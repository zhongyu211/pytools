__author__ = "allenz"
import os
import sys
import logging
import datetime
from mpfhandler import MultProcTimedRotatingFileHandler
from logging.handlers import TimedRotatingFileHandler
#coding :utf-8
__author__ = "allenz"
from conf.settings import DB_INFOS
from logger.mplog import log

from MySQLdb import connect as mysql_connect
import MySQLdb

import traceback

class MysqlConnect(object):
    def __init__ (self,  sql_content, host=None, port=None, user=None, password=None, timeout= 2):
        self.sql_content = sql_content
        self.host = host if host else DB_INFOS["mysql"]["host"]
        self.port = host if port else DB_INFOS["mysql"]["port"]
        self.user = user if user else DB_INFOS["mysql"]["user"]
        self.password = password if password else DB_INFOS["mysql"]["password"]
        self.timeout = timeout
        self.conn = self.init_conn()

    def init_conn(self):
        try:
            conn = mysql_connect(host=self.host, port=self.port, user=self.user, password=self.password,
                          connect_timeout=self.timeout, database="task_scheduler")
            return conn
        except Exception as ex:
            log.error(traceback.format_exc())
            log.error(ex.args)
            return None



    def excute(self):

        try:
            if self.conn:
                cursor = self.conn.cursor()
                cursor.execute(self.sql_content)
                cursor.close()
                self.conn.commit()
                self.conn.close()
        except Exception as ex:
            #log.error(traceback.format_exc())
            log.error(traceback.format_exc())
            log.error(ex.args)
    #
    def query(self):
        try:
            if self.conn:
                cursor =self.conn.cursor()
                cursor.execute(self.sql_content)
                result = cursor.fetchall()
                cursor.close()
                self.conn.commit()
                self.conn.close()
                return result
        except Exception as ex:
            log.error(traceback.format_exc())
            log.error(ex.args)


if __name__ == "__main__":
    sql = 'select * from task_scheduler.trigger_log;'
    conn = MysqlConnect(sql)
    print conn.query()