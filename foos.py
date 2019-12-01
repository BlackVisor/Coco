# -*- coding: utf-8 -*-
# @Author: Cheng JiangDong


from matplotlib import pyplot as plt
import re


logFilePath = r'D:\Downloads\360Downloads\mem.log'
with open(logFilePath, 'r') as f:
    logFile = f.readlines()
    monitorTime = []
    freeMemory = []
    freeHugePageMemory = []
    timeStart = 0
    for i in range(len(logFile)):
        if "mem_free" in logFile[i]:
            # 递增的时间，作为x轴
            monitorTime.append(timeStart)
            if "G" in logFile[i+1]:
                # 如果free memory是G为单位的就换算成MB
                freeMemory.append(1024 * float(logFile[i+1][:-2]))
            elif "M" in logFile[i+1]:
                freeMemory.append(float(logFile[i+1][:-2]))
            else:
                freeMemory.append(float(logFile[i+1][:-2]) / 1024)

            if "Huge" in logFile[i+2]:
                freeHugePageMemory.append(float(re.findall(r'\d+', logFile[i+2])[0]))
            timeStart = timeStart + 0.5
            i = i + 3

plt.plot(monitorTime, freeMemory)
plt.show()
plt.plot(monitorTime, freeHugePageMemory)
plt.show()
