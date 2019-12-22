import subprocess

order='adb shell "ps| grep com.taobao.taobao"' #获取连接设备

pi= subprocess.Popen(order,shell=True,stdout=subprocess.PIPE)

print(pi.stdout.read())