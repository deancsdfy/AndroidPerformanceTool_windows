#! python3
#coding=utf-8

import sys,os,re,threading
sys.path.append('.')
from public import publicfunction as util
from public.timecount import TimeCount
PATH = lambda p: os.path.abspath(p)

#获取当前应用包名
package_name = util.get_current_packagename()
print('本次测试APP为:%s' %(package_name))

#获取men cpu 占用情况
@TimeCount
def top():
    pid = get_pid()
    if getSDKVersion() <= 23:
        top_info = util.shell('top -n 1 | grep %d' % (int(pid))).stdout.readlines()
        if(len(top_info)!=0):
            for x in top_info:
                temp_list = x.split()
                cpu = round(float(temp_list[2].decode().split('%')[0]),2)
                mem = round(float(temp_list[6].decode()[0:-1])/1024,1)
                return (cpu,mem)
        else:
            return 0.0
    else:
        cpu = getCpuInfo()
        mem_threading = threading.Thread(target=getMemInfo())
        mem_threading.start()
        mem_threading.join()
    return (cpu)

def getCpuNums():
    num_info = util.shell('cat /proc/cpuinfo|grep processor').stdout.readlines()
    # print("cpu nums is %d" %(len(num_info)))
    return len(num_info)

@TimeCount
def getCpuInfo():
    pid = get_pid()
    cpunums=getCpuNums()
    top_info = util.shell('top -n 1 | grep %d' % (int(pid))).stdout.readlines()
    if(len(top_info)!=0):
        for x in top_info:
            temp_list = x.split()
            cpu = round(float(temp_list[8])/cpunums,2)
            print(cpu)
            return cpu
    else:
        return 0.0

@TimeCount
def getMemInfo():
    pid=get_pid()
    mem_info = util.shell('dumpsys meminfo %d |grep TOTAL:' %(int(pid))).stdout.readlines()
    for x in mem_info:
        temp_list = x.split()
        mem=round(float(temp_list[1])/1024,1)
        print(mem)
    return mem

#获取机型名称
def getDevicesName():
    devicesName = util.shell('getprop ro.product.model').stdout.read().decode().strip()
    return devicesName

# 获取系统SDK版本
def getSDKVersion():
    SDKVersion = util.shell('getprop ro.build.version.sdk').stdout.read().decode().strip()
    return int(SDKVersion)

#获取pid
def get_pid():
    # 正则匹配出package和activity的pid
    pattern = re.compile(r"[a-zA-Z0-9\.]+=.[0-9\.]+")
    package = util.shell('dumpsys activity top| grep ACTIVITY').stdout.read()
    pid = pattern.findall(package.decode())[-1].split('=')[1]
    # print('pid为: %s' %(pid))
    return pid

#获取uid
def get_uid():
    cmd = 'cat  /proc/'+ get_pid() + '/status'
    uid_info = util.shell(cmd).stdout.readlines()
    uid = uid_info[6].split()[1]
    print('uid为:%s' %(uid))
    return str(uid)


#上传流量,暂时不可用，需查下其他方式获取上行流量
def get_flow_send():
    cmd = '"cat proc/net/xt_qtaguid/stats|grep '+'%s"'%get_uid()
    print(cmd)
    flow = util.shell(cmd).stdout.readlines()
    print(flow)

if __name__ == "__main__":
    #get_flow_send()
    top()
    # getCpuInfo()
    # getMemInfo()