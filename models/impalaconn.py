__author__ = "allenz"
from conf.settings import DB_INFOS
from logger.mplog import log
from impala.dbapi import connect as impala_connect

import traceback

class ImpalaConnect(object):
    def __init__ (self,  sql_content, host=None, port=21050, user=None, password=None, timeout= 5):
        self.sql_content = sql_content
        self.host = host if host else DB_INFOS["impala"]["host"]
        self.port = host if port else DB_INFOS["impala"]["port"]
        self.user = user if user else DB_INFOS["impala"]["user"]
        self.password = password if password else DB_INFOS["impala"]["password"]
        self.timeout = timeout
        self.conn = self.init_conn()

    def init_conn(self):
        try:
            conn = impala_connect(host=self.host, port=self.port, user=self.user, password=self.password,
                          connect_timeout=self.timeout, database="")
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
    pass