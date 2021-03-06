#coding=utf-8
import datetime
from functools import wraps


class TimeCount():
    def __init__(self, fn=None):
        wraps(fn)(self)

    def __call__(self, *args, **kwargs):
        start = datetime.datetime.now()
        ret = self.__wrapped__(*args, **kwargs)
        cost = datetime.datetime.now() - start
        print(cost)
        return ret