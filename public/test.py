import sys
import os
print(sys.path) #查看当前解项目的环境变量
sys.path.append(os.path.dirname(os.path.abspath(__file__)))#加环境变量
print(sys.path)#再查看