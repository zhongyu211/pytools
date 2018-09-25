__author__ = "allenz"
import os
import sys

import os
import sys

#log configuration
LOG_FILE_NAME = 'merge.log'
LOG_LEVEL = "INFO"

#db configuration
DB_INFOS = {
    "impala": {
        "host": "ip-172-32-0-159.us-west-1.compute.internal",
        "port": 21050,
        "user": 'admin',
        "password": None
    },
    "mysql": {
        #"host": "172.32.0.143",
        "host":"54.183.171.241",
        "port": 3306,
        "user": "root",
        "password": "Viewfin2018"
    },
    "redshift": {
        "host": "viewfin.cw9jfoph5mfr.us-west-1.redshift.amazonaws.com",
        "port": 5439,
        "user": "root",
        "password": "Viewfin2018!"
    }
}