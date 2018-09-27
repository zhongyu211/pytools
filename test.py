__author__ = "allenz"
import os
import sys

from logger.mplog import log
for i in xrange(1,10):
    log.info("this is test")
import confluent_kafka as ck
