import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_csv('adc_comparison\ExternalADC_400HZ.csv')
data1=data1.drop(['Time'],axis=1)
index = data1.index
rownum = len(index)
x1=np.linspace(0,rownum,rownum)
std= np.std(data1)
print("stnadard deviation with adc is:",std)

##print(data)
data2 = pd.read_csv('adc_comparison\ExternalADC_400HZ.csv')
data2=data2.drop(['Time'],axis=1)
index = data2.index
rownum = len(index)
x2=np.linspace(0,rownum,rownum)
std= np.std(data2)
print("stnadard deviation without adc is:",std)

fig,pic = plt.subplots(2)
fig.suptitle('PLOT')
pic[0].plot(x1,data1,linewidth=1)
pic[1].plot(x2,data2,linewidth=1)

for ax in pic.flat:
    ax.set(xlabel='x-label', ylabel='y-label')



# plt.plot(x,data,'o', color='blue',markersize=2)
plt.grid()
plt.show()