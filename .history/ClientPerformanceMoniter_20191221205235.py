# coding=utf-8
from signal import signal, SIGTERM, SIGINT
from public import publicfunction as util
from script import get_cpu_mem_info as info
# from script import ShowData
from collections import deque
import time
import datetime
import sys
import queue
import _thread
# sys.path.append(".//public")
# sys.path.append(".//script")


class ClientPerformanceMoniter(object):
    def __init__(self):
        self._pkg_name = util.get_current_packagename()
        self._CurrentCpuUseRate = ""
        self._CurrentMemUse = ""
        self._CpuUseRateQueue = deque()
        self._MemUseQueue = deque()
        pass

    def _GetPerformanceDataThread(self):
        while True:
           # cpuRate,mem = info.top()
            cpuRate = info.getCpuInfo()
            mem = info.getMemInfo()
            print(cpuRate)
            print("main function mem is %f" % (mem))
            self._CpuUseRateQueue.appendleft(cpuRate)
            self._MemUseQueue.appendleft(mem)
            time.sleep(0.8)

    def StartMonitor(self):
        self._DataFileFd = open("./Data/PerformanceData.txt", 'w')
        self._DataFileFd.writelines("Time CpuUseRate Memory\n")
        # 开启新线程获取cpu内存值
        _thread.start_new_thread(self._GetPerformanceDataThread, ())

        # dataShow = ShowData.ShowData()
        # dataShow.InitRealtimeFig()
        count = 0
        while 1:
            if len(self._MemUseQueue) == 0 and len(self._CpuUseRateQueue) == 0:
                print('the data queue is empty!')
                time.sleep(1)
                continue
            # show x axis
            # dataShow.SetXValue(count)
            # cpu use rate data
            if not len(self._CpuUseRateQueue) == 0:
                self._CurrentCpuUseRate = self._CpuUseRateQueue.popleft()
                # dataShow.SetCpuYValue(float(self._CurrentCpuUseRate))
            # Mem use
            if not len(self._MemUseQueue) == 0:
                self._CurrentMemUse = self._MemUseQueue.popleft()
                # dataShow.SetMemYValue(float(self._CurrentMemUse))

            self._DataFileFd.writelines(str(
                time.time())+" "+str(self._CurrentCpuUseRate)+" "+str(self._CurrentMemUse)+"\n")
            self._DataFileFd.flush()

            # dataShow.Show()
            time.sleep(0.2)
            count += 1

    def CleanMonitor(self):
        self._DataFileFd.close()


class CleanProcess(object):
    def __init__(self):
        self._PerformanceMonitorObj = None
        pass

    def CleanWhenKillProcess(self, a=None, b=None):
        if self._PerformanceMonitorObj != None:
            self._PerformanceMonitorObj.ClearMonitor()

    def SetPerformanceMonitorObj(self, obj):
        self._PerformanceMonitorObj = obj


if __name__ == '__main__':
    print("start------------------------")
    # clean obj
    cleanObj = CleanProcess()
    signal(SIGTERM, cleanObj.CleanWhenKillProcess)
    signal(SIGINT, cleanObj.CleanWhenKillProcess)
    monitor = ClientPerformanceMoniter()
    cleanObj.SetPerformanceMonitorObj(monitor)
    monitor.StartMonitor()
    print("finish-----------------------")