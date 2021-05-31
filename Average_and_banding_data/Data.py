import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Average_and_banding_data/Spiffs_6000Hz.csv')
data=data.drop(['Time'],axis=1)
index = data.index
rownum = len(index)
x=np.linspace(0,rownum,rownum)
std= np.std(data)
print(std)

##print(data)

plt.title('PLOT')
plt.xlabel('arbitary time')
plt.ylabel('reading')

plt.plot(x,data,'o', color='blue',markersize=2)
plt.grid()
# plt.show()


# finding moving average of the plot
window_size = 7
moving_average = []
moving_average_l=[]
moving_average_s=[]

i=0
while i < (rownum - window_size + 1): 
    this_window = data[i:i + window_size]
    ##print(this_window)
    window_average = np.sum(this_window)/window_size
    moving_average_l.append(window_average+std)
    moving_average_s.append(window_average-std)
    moving_average.append(window_average)
    i += 1
a=np.linspace(1,len(moving_average),len(moving_average))


# print(moving_average)
plt.plot(a,moving_average)
plt.plot(a,moving_average_l,'--',linewidth=1,color='red')
plt.plot(a,moving_average_s,'--',linewidth=1,color='red')
plt.show()


