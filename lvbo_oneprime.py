import numpy as np
from matplotlib import pyplot as plt
from scipy import signal
#my_data = np.genfromtxt(r"C:\Users\27769\Desktop\Dataset\mox_temperature_modulation\20160930_203718.csv" ,delimiter=',')
my_data = np.genfromtxt(r"C:\Users\27769\Desktop\Dataset\volt_1000.txt" ,delimiter='')
#deal_data=my_data[1:]

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
list_s = []

plt.figure(1)
#plt.figure(figsize = (30,20))
for i in range(1,5):

    plt.subplot(2, 2, i)
    s = my_data[i-1]

    list_s = []
    plt.plot(s, label='原始数据')
    a = 0.95  # a取0-1之间，a越接近1越稳定，越接近0越灵敏

    for i in range(len(s) - 1):
        s[i + 1] = (1 - a) * s[i + 1] + a * s[i]
        list_s.append(s[i + 1])

    plt.plot(list_s, label='滤波后数据')
    plt.title('一阶滞后滤波算法')
    plt.legend()

plt.figure(2)
for i in range(1,5):

    plt.subplot(2, 2, i)
    s = my_data[i+3]

    list_s = []
    plt.plot(s, label='原始数据')
    a = 0.95  # a取0-1之间，a越接近1越稳定，越接近0越灵敏

    for i in range(len(s) - 1):
        s[i + 1] = (1 - a) * s[i + 1] + a * s[i]
        list_s.append(s[i + 1])

    plt.plot(list_s, label='滤波后数据')
    plt.title('一阶滞后滤波算法')
    plt.legend()
plt.figure(3)
for i in range(1,4):

    plt.subplot(2, 2, i)
    s = my_data[i+7]

    list_s = []
    plt.plot(s, label='原始数据')
    a = 0.95  # a取0-1之间，a越接近1越稳定，越接近0越灵敏

    for i in range(len(s) - 1):
        s[i + 1] = (1 - a) * s[i + 1] + a * s[i]
        list_s.append(s[i + 1])

    plt.plot(list_s, label='滤波后数据')
    plt.title('一阶滞后滤波算法')
    plt.legend()


plt.show()