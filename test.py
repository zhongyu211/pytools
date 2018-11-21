__author__ = "allenz"
import os
import sys
from models.impalaconn import ImpalaConnect
sql = "select count(*) from ods_rightbtc.user_register;"
conn = ImpalaConnect(sql)
print conn.query()
