__author__ = "allenz"
import os
import sys
import logging
import datetime
#need to pip install mpfhandler
from mpfhandler import MultProcTimedRotatingFileHandler
from logging.handlers import TimedRotatingFileHandler
'''
CRITICAL 50,ERROR 40,WARNING 30,INFO 20,DEBUG 10,NOTSET 0
'''
import os
import sys
from conf.settings import *
# Basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
Basedir = os.path.abspath(os.path.dirname(__file__))

log_level_map = {
    "INFO":logging.INFO,
    "WARNING":logging.WARNING,
    "ERROR":logging.ERROR,
    "CRITICAL":logging.CRITICAL,
    "DEBUG":logging.DEBUG
}

class NullHandler(logging.Handler):

    def emit(self, record):
        pass


class GlobalLogging:
    log = None

    @staticmethod
    # def getInstance():
    def getLog():
        if GlobalLogging.log == None:
            GlobalLogging.log = GlobalLogging()
        return GlobalLogging.log

    def __init__(self):
        self.logger = None
        self.handler = None
        self.level = log_level_map["LOG_LEVEL"]
        self.logger = logging.getLogger("GlobalLogging")
        self.formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s")

        self.logger.setLevel(self.level)

        # fixme
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        parent_dir = os.path.abspath(os.path.join(Basedir, os.pardir))
        print parent_dir
        if not os.path.isdir(parent_dir + '/logs'):
            os.mkdir(parent_dir + '/logs')
        fname =  os.path.abspath(os.path.join(parent_dir,'logs',LOG_FILE_NAME))

        self.h= TimedRotatingFileHandler(fname,when='midnight',backupCount=20)
        self.h.setFormatter(self.formatter)
        self.logger.addHandler(self.h)

    def setLoggingToFile(self, file):
        fh = logging.FileHandler(file)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

    def setLoggingToConsole(self):
        ch = logging.StreamHandler()
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

    def setLoggingToHandler(self, handler):
        self.handler = handler

    def setLoggingLevel(self, level):
        self.level = level
        self.logger.setLevel(level)

    def debug(self, s):
        self.logger.debug(s)
        if not self.handler == None and self.level <= logging.DEBUG:
            self.handler('-DEBUG-:' + s)

    def info(self, s):

        self.logger.info(s)
        # print self.handler,self.level
        if not self.handler == None and self.level <= logging.INFO:
            self.handler('-INFO-:' + s)

    def warn(self, s):
        self.logger.warn(s)
        if not self.handler == None and self.level <= logging.WARNING:
            self.handler('-WARN-:' + s)

    def error(self, s):

        self.logger.error(s)
        if not self.handler == None and self.level <= logging.ERROR:
            self.handler('-ERROR-:' + s)

    def critical(self, s):
        self.logger.critical(s)
        if not self.handler == None and self.level <= logging.CRITICAL:
            self.handler('-CRITICAL-:' + s)

    def __del__(self):
        pass
log = GlobalLogging.getLog()