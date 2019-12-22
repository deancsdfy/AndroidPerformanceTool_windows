from matplotlib import pyplot
# import random
# # %matplotlib inline
# # 中文显示问题-- 下载中文字体，安装字体-修改配置文件下面手动修改配置
# # from pylab import mpl
# # mpl.rcParams["font.sans-serif"] = ["SimHei"]
# # mpl.rcParams["axes.unicode_minus"] = False # 解决保存图像是负号'-'显示为方块的问题
 
# # 准备数据
# x = range(60)
# y_sh = [random.uniform(26,31) for i in x]
# y_bj = [random.uniform(27, 35) for i in x]
 
# # 创建画布
# plt.figure(figsize=(16,8), dpi=60)
 
# # 同一坐标内--绘制多条折线图  （新增）
# plt.plot(x, y_sh, label="sh")
# plt.plot(x, y_bj, label="bj", linestyle="--", color="y")  # 线条颜色，线条样式设置 见下图
 
# # 自定义x, y轴 刻度 & 刻度标签 (新增)
# x_ticks = range(0, 60, 5)
# y_ticks = range(20, 40, 5)
 
# x_ticks_label = ["11点{}分".format(i) for i in x_ticks]
 
# plt.xticks(x_ticks, x_ticks_label)
# plt.yticks(y_ticks)
 
# # 添加辅助描述信息-- x，y轴标签 & 图形标题
# plt.xlabel("时间")
# plt.ylabel("温度")
 
# plt.title("两地同一时间温度变化图")
 
# # 添加网格线 - alpha:透明度   （新增）
# plt.grid(True, linestyle="--", alpha=0.6)
 
# # 显示图例 -- loc：位置设置,详见下图  （新增）
# plt.legend(loc="best")
# # 显示图象
# print('1')
# # plt.show()
print('1')