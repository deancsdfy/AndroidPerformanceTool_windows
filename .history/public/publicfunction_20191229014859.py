#coding=utf-8
import os
import subprocess
import re
from timecount import TimeCount
serialno_num=''

#获取手机
def get_devices():
    devices=[]
    result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    for line in result[1:]:
        if 'device' in line.strip():
            devices.append(line.split()[0])
        else:
            break
    return devices

#adb shell命令
def shell(args):
    cmd = 'adb shell \"%s\"' %( str(args))
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@TimeCount
def get_current_packagename():
    #正则匹配出package和activity
    pattern = re.compile(r"[a-zA-Z0-9\.]+/.[a-zA-Z0-9\.]+")
    package = shell('dumpsys activity top| grep ACTIVITY').stdout.read()
    #用-1，是因为部分机型上，还会返回一些系统进程和包，比如小米8
    print(pattern.findall(package.decode())[-1].split('/')[0])
    return pattern.findall(package.decode())[-1].split('/')[0]

def get_current_activity():
    #正则匹配出package和activity
    pattern = re.compile(r"[a-zA-Z0-9\.]+/.[a-zA-Z0-9\.]+")
    package = shell('dumpsys activity top| grep ACTIVITY').stdout.read()
    return pattern.findall(package.decode())[-1].split('/')[1]

if __name__ == "__main__":
    get_current_activity()
    get_current_packagename()