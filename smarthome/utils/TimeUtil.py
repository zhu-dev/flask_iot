# -*- coding: utf-8 -*-
# @Author  : zhu
import datetime
import time


def formatGMTime(timestamp):
    GMT_FORMAT = '%Y%m%dT%H%M%SZ'
    a = datetime.datetime.strptime(timestamp, GMT_FORMAT) + datetime.timedelta(hours=8)
    result = a.strftime("%Y-%m-%d %H:%M:%S")
    return result
