#coding=utf-8

import time
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import random
from matplotlib.ticker import MultipleLocator,FormatStrFormatter

class ShowData(object):
    def __init__(self):
        self.mCpuAxes = None
        self.mMemAxes = None
        self.mMemFigObj = None
        self.mCpuFigObj = None

        self.__SHOW_VALUE_NUM = 60
        self._mXAxisData = []

        self._mCputUseRate = []
        self._mMemValue = []
    def SetXValue(self, value):
        if len(self._mXAxisData) >= self.__SHOW_VALUE_NUM:
            del self._mXAxisData[0]

        self._mXAxisData.append(value)
    def SetMemYValue(self, value):
        if len(self._mMemValue) >= self.__SHOW_VALUE_NUM:
           del self._mMemValue[0]
        self._mMemValue.append(value)
    def SetCpuYValue(self, value):
        if len(self._mCputUseRate) >= self.__SHOW_VALUE_NUM:
            del self._mCputUseRate[0]
        self._mCputUseRate.append(value)
    def Show(self):
        #Clear axis
        self.mCpuFigObj.cla()
        self.mMemFigObj.cla()
        #reset axis
        self._InitCpuFig()
        self._InitMemFig()
        self.mCpuFigObj.plot(self._mXAxisData, self._mCputUseRate, label="cpu", color="red", linewidth=2)
        self.mMemFigObj.plot(self._mXAxisData, self._mMemValue, label="mem", color="blue", linewidth=2)

        plt.pause(0.1)
        plt.show()

    def InitRealtimeFig(self):
        self._InitShowFig()
    def _InitShowFig(self):
        fig = plt.figure(figsize=(15, 7), dpi=100)


        self.mMemFigObj = fig.add_subplot(212)
        self.mCpuFigObj = fig.add_subplot(211)

        self.mMemAxes = plt.subplot(212)
        self.mCpuAxes = plt.subplot(211)

        # Adjust position
        plt.subplots_adjust(left = 0.045, right = 0.98, bottom = 0.05, top = 0.98, wspace = 0.2, hspace = 0.2)

        # Each own init
        self._InitMemFig()
        self._InitCpuFig()
    def _InitMemFig(self):
        plt.sca(self.mMemAxes)

        plt.ylabel("M", fontsize=10)
        # Set y limit
        #plt.ylim(0, 350)
        #s开启交互模式
        plt.ion()

        # Axis type
        #设置Y轴主刻度的值为10的倍数
        ymajorLocator = MultipleLocator(10)
        #设置y轴的数据显示格式
        ymajorFormatter = FormatStrFormatter('%1.1f')
        #设置Y轴幅刻度的值为5倍数
        yminorLocator = MultipleLocator(5)

        self.mMemAxes.yaxis.set_major_locator(ymajorLocator)
        self.mMemAxes.yaxis.set_major_formatter(ymajorFormatter)
        self.mMemAxes.yaxis.set_minor_locator(yminorLocator)

        # X axis type
        xmajorLocator = MultipleLocator(1)
        xmajorFormatter = FormatStrFormatter('%1d')
        xminorLocator = MultipleLocator(1)

        self.mMemAxes.xaxis.set_major_locator(xmajorLocator)
        self.mMemAxes.xaxis.set_major_formatter(xmajorFormatter)
        self.mMemAxes.xaxis.set_minor_locator(xminorLocator)

        #self.mMemFigObj.xaxis.grid(True, which='minor')
        #y轴使用幅刻度
        self.mMemFigObj.yaxis.grid(True, which='minor')
    def _InitCpuFig(self):
        plt.sca(self.mCpuAxes)

        plt.ylabel("cpu", fontsize=10)
        # Set y limit
        #plt.ylim(5, 80)
        plt.ion()

        # Y axis type
        ymajorLocator = MultipleLocator(5)
        ymajorFormatter = FormatStrFormatter('%1.1f')
        yminorLocator = MultipleLocator(3)

        self.mCpuAxes.yaxis.set_major_locator(ymajorLocator)
        self.mCpuAxes.yaxis.set_major_formatter(ymajorFormatter)
        self.mCpuAxes.yaxis.set_minor_locator(yminorLocator)

        # X axis type
        xmajorLocator = MultipleLocator(1)
        xmajorFormatter = FormatStrFormatter('%1d')
        xminorLocator = MultipleLocator(1)

        self.mCpuAxes.xaxis.set_major_locator(xmajorLocator)
        self.mCpuAxes.xaxis.set_major_formatter(xmajorFormatter)
        self.mCpuAxes.xaxis.set_minor_locator(xminorLocator)

        #self.mCpuAxes.xaxis.grid(True, which='minor')
        self.mCpuAxes.yaxis.grid(True, which='minor')

