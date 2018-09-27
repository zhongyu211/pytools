__author__ ="allenz"
import pymongo
from  pymongo  import  MongoClient
from logger.mplog import log
from conf.settings import DB_INFOS


class MongoConn(object):
    def __init__(self):
        self.client = MongoClient("172.31.13.36",27017)
        self.db = self.client["viewfinIndex"]
        #self.collection = self.db["blockcc_ha_status"]


    def __del__(self):
        self.client.close()
