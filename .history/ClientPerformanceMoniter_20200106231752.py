# coding=utf-8
from public import publicfunction as util
from script import get_cpu_mem_info as info
import time
import datetime
import xlwt

class ClientPerformanceMoniter(object):
    def __init__(self):
        self._devicesName = info.getDevicesName()
        self._pkg_name = util.get_current_packagename()
        self._CurrentCpuUseRate = ""
        self._CurrentMemUse = ""

    def StartMonitor(self):
        count = 0
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding='utf-8')
        while True:
            top_info = info.top()
            cpuRate = top_info[0]
            mem = top_info[1]

            now = datetime.datetime.now()
            now = now.strftime("%H:%M:%S")

            if count % 30 == 0:
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
            worksheet.write(count+1, 1, label=cpuRate)
            worksheet.write(count+1, 2, label=mem)
            workbook.save('./Data/per_{}.xlsx'.format(self._devicesName))
            print("cpu is {}% mem is {}M".format(cpuRate, mem))
            # time.sleep(0.2)
            count += 1
            
if __name__ == '__main__':
    print("start------------------------")
    monitor = ClientPerformanceMoniter()
    monitor.StartMonitor()