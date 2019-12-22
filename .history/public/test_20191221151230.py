import subprocess

order='adb devices' #获取连接设备

pi= subprocess.Popen(order,shell=True,stdout=subprocess.PIPE)

print pi.stdout.read() #打印结果