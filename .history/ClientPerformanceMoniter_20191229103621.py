# coding=utf-8
from signal import signal, SIGTERM, SIGINT
from public import publicfunction as util
from script import get_cpu_mem_info as info
from collections import deque
import time
import datetime
import sys
import queue
import _thread
import xlwt

class ClientPerformanceMoniter(object):
    def __init__(self):
        self._devicesName = info.getDevicesName()
        self._pkg_name = util.get_current_packagename()
        self._CurrentCpuUseRate = ""
        self._CurrentMemUse = ""
        self._CpuUseRateQueue = deque()
        self._MemUseQueue = deque()

    def _GetPerformanceDataThread(self):
        while True:
            cpuRate = info.top()[0]
            mem = info.top()[1]
            print("cpu is {}% mem is {}M".format(cpuRate, mem))
            self._CpuUseRateQueue.appendleft(cpuRate)
            self._MemUseQueue.appendleft(mem)
            # time.sleep(0.8)

    def StartMonitor(self):

        # 开启新线程获取cpu内存值
        _thread.start_new_thread(self._GetPerformanceDataThread, ())
        count = 0
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding='utf-8')
        while 1:
            if len(self._MemUseQueue) == 0 and len(self._CpuUseRateQueue) == 0:
                # print('the data queue is empty!')
                # time.sleep(0.5)
                continue
            # show x axis
            # cpu use rate data
            if not len(self._CpuUseRateQueue) == 0:
                self._CurrentCpuUseRate = self._CpuUseRateQueue.popleft()
            # Mem use
            if not len(self._MemUseQueue) == 0:
                self._CurrentMemUse = self._MemUseQueue.popleft()

            now = datetime.datetime.now()
            now = now.strftime("%H:%M:%S")

            if count % 20 == 0:
                print('-----------------------------{}'.format(count+1))
            if count == 0:
                # 创建一个worksheet
                worksheet = workbook.add_sheet(self._devicesName)
                worksheet.write(0, 0, label='时间')
                worksheet.write(0, 1, label='CPU占用率(%)')
                worksheet.write(0, 2, label='内存占用(M)')

            # 入excel
            # 参数对应 行, 列, 值
            worksheet.write(count+1, 0, label=str(now))
            worksheet.write(count+1, 1, label=self._CurrentCpuUseRate)
            worksheet.write(count+1, 2, label=self._CurrentMemUse)
            workbook.save('./Data/per_{}.xlsx'.format(self._devicesName))
            # time.sleep(0.2)
            count += 1
if __name__ == '__main__':
    print("start------------------------")
    monitor = ClientPerformanceMoniter()
    cleanObj.SetPerformanceMonitorObj(monitor)
    monitor.StartMonitor()
