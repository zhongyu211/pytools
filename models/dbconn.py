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

import MySQLdb.connections as mysql_connect


class MysqlConnect(object):
    def __init__ (self,  sql_content, host=None, port=None, user=None, password=None, timeout= 60):
        self.sql_content = sql_content
        self.host = host if host else DB_INFOS["mysql"]["host"]
        self.port = host if port else DB_INFOS["mysql"]["port"]
        self.user = user if user else DB_INFOS["mysql"]["user"]
        self.password = password if password else DB_INFOS["mysql"]["password"]
        self.timeout = timeout

    # def dowork(self):
    #
    #     try:
    #         conn = mysql_connect(host =self.host, port =self.port, user = self.user, password = self.password, connection_timeout = self.timeout, database="task_scheduler")
    #         cursor = conn.cursor()
    #         for result in cursor.execute(self.sql_content, multi=self.is_multi):
    #             pass
    #         conn.commit()
    #         cursor.close()
    #         conn.close()
    #         log.info("excute mysql query successfully.")
    #        except mysql.connector.Error as err:
    #            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    #                log.error("Something is wrong with your user name or password")
    #            elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #                log.error("Database does not exist")
    #            else:
    #                log.error(err)
    #        except Exception as ex:
    #            log.error(ex)
    #
    # def query(self):
    #     conn = None
    #     try:
    #         conn = mysql_connect(host =self.host, port =self.port, user = self.user, password = self.password, connection_timeout = self.timeout, database="task_scheduler")
    #         cursor = conn.cursor()
    #         cursor.execute(self.sql_content)
    #         result = cursor.fetchall()
    #         cursor.close()
    #         conn.close()
    #         return result
    #     except mysql.connector.Error as err:
    #         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    #             log.error("Something is wrong with your user name or password")
    #         elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #             log.error("Database does not exist")
    #         else:
    #             log.error(err)
    #     except mysql.connector.Error as err:
    #         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    #             log.error("Something is wrong with your user name or password")
    #         elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #             log.error("Database does not exist")
    #         else:
    #             log.error(err)

if __name__ == "__main__":

    log.info("hello word")