import subprocess

order='adb devices' #获取连接设备

p = subprocess.Popen(order,shell=True,stdout=subprocess.PIPE)

print (p.stdout.read()) #打印结果