import xlwt

class ClientPerformanceMoniter(object):
    def StartMonitor(self):
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding = 'utf-8')
        while 1:
            now = datetime.datetime.now()
            now = now.strftime("%H:%M:%S")
            if count == 0:
                # 创建一个worksheet
                worksheet = workbook.add_sheet('data')
                worksheet.write(0,0, label = '时间')
                worksheet.write(0,1, label = 'CPU占用率(%)')
                worksheet.write(0,2, label = '内存占用(M)')
            # 入excel
            # 参数对应 行, 列, 值
            worksheet.write(count+1,0, label = str(now))
            worksheet.write(count+1,1, label = round(float(self._CurrentCpuUseRate),2))
            worksheet.write(count+1,2, label = round(float(self._CurrentMemUse),1))
            workbook.save('./Data/PerformanceData.xlsx')