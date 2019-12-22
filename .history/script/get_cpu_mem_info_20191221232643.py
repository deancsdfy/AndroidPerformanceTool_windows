#! python3
#coding=utf-8

import sys,os,re
#sys.path.append('E:\TestAndroid')
print(sys.path)
sys.path.append('.')
from public import publicfunction as util
PATH = lambda p: os.path.abspath(p)

#获取当前应用包名
package_name = util.get_current_packagename()
# print('本次测试APP为:%s' %(package_name))

#定义top次数,已不用了
times=20

#获取men cpu 占用情况
def top():
    print('Starting get mem cpu information...')
    pid=get_pid()
    print(pid)
    top_info = util.shell("top -n 1 | grep %d" %(int(pid))).stdout.readlines()
    for x in top_info:
        temp_list = x.split()
        #print(temp_list[8])
        cpu=float(temp_list[8])
        #cpu.append(float(temp_list[8]))
        #print(temp_list[9])
        mem=float(temp_list[9])
        #mem.append(float(temp_list[9]))
    print(cpu)
    print(mem)
    return (cpu,mem)
def getCpuNums():
    num_info = util.shell('cat /proc/cpuinfo|grep processor').stdout.readlines()
    # print("cpu nums is %d" %(len(num_info)))
    return len(num_info)
def getCpuInfo():
    # print('Starting get mem cpu information...')
    pid = get_pid()
    # print(pid)
    cpunums=getCpuNums()
    top_info = util.shell('top -n 1 | grep %d' % (int(pid))).stdout.readlines()
    if(len(top_info)!=0):
        for x in top_info:
            temp_list = x.split()
            # print(temp_list[8])
            if(temp_list[8]!=" "):
                cpu = float(temp_list[8])/cpunums
                print(cpu)
            else:
                cpu = 0.0
            return cpu
    else:
        return 0.0

def getMemInfo():
    # print('start get mem information....')
    pid=get_pid()
    # print(pid)
    mem_info = util.shell('dumpsys meminfo %d |grep TOTAL:' %(int(pid))).stdout.readlines()
    for x in mem_info:
        temp_list = x.split()
        mem=float(temp_list[1])/1024
        print(mem)
    return mem
#获取devices用作表格sheet
def devices():
    devices=util.get_devices()
    print('设备号为: %s' %(devices[0]))
    return devices[0]


#获取pid
def get_pid():
    # 正则匹配出package和activity的pid
    pattern = re.compile(r"[a-zA-Z0-9\.]+=.[0-9\.]+")
    package = util.shell('dumpsys activity top| grep ACTIVITY').stdout.read()
    pid = pattern.findall(package.decode())[-1].split('=')[1]
    # pid_info = util.shell('ps| grep %s' %(package_name)).stdout.readlines()
    # print(pid_info)
    # pid = pid_info[0].split()[1]
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
    print("Starting get top information...")
    #get_flow_send()
    #top()
    getCpuInfo()
    getMemInfo()