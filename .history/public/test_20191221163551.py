import subprocess

order='adb shell "top -n 1 | grep 13327"' #获取连接设备

pi= subprocess.Popen(order,shell=True,stdout=subprocess.PIPE)

print(pi.stdout.read())