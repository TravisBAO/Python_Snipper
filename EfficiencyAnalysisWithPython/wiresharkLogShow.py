import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot

#data source
SendDelay = ['200ms', '100ms', '50ms', '25ms']
RPM_resp_Count = [50, 60, 88, 20]
WP_resp_Count = [98, 75, 39, 21]
SendCount = [98, 98, 98, 98]
size = 4

x = np.arange(size)

a = SendCount
b = RPM_resp_Count
c = WP_resp_Count

pyplot.xlabel('SendDelay') # display label on x, y and title
pyplot.ylabel('ResponseCount')
pyplot.title('AX100 BACnet Performance')

total_width, n = 0.8, 3
width = total_width / n
x = x - (total_width - width) / 2

first = pyplot.bar(x, a,  width=width, label='SendFrames')
second = pyplot.bar(x + width, b, width=width, label='RPM_Resp_Cnt')
third = pyplot.bar(x + 2 * width, c, width=width, label='WP_Resp_Cnt')

plt.xticks(x + width, SendDelay)#显示x坐标轴的标签,即tick_label,调整位置，使其落在两个直方图中间位置

for aa, bb in zip(x, SendCount): #显示 sendcount 
    pyplot.text(aa - 0.1, bb + 0.1, '%i' % bb)
for aa, bb in zip(x, RPM_resp_Count): # 显示RPM Response count
    pyplot.text(aa + 0.2, bb + 0.1, '%i' % bb)
for aa, bb in zip(x, WP_resp_Count): # 显示 WP Response count
    pyplot.text(aa + 0.45, bb + 0.1, '%i' % bb)    

pyplot.legend()
pyplot.show()

# pyplot.savefig("AX100BACnetPerformance.png")


