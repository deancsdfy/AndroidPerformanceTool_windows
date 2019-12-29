#coding=utf-8
import datetime

class TimeCount():
    def __init__(self, fnc):
        self._fnc = fnc

    def __call__(self):
        start = datetime.datetime.now()
        self._fnc(*args, **kwargs)
        cost = (datetime.datetime.now() - start).total_seconds()
        print(cost)