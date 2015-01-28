import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import scipy
import datetime
import time
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation


theNames=[]
txts=pd.read_csv("/Users/vmac/PycharmProjects/pandasStock/symbol_list.txt",skiprows=0)
datas=np.zeros((3775,1))
#print txts["companies"][0]
for sz in range(0,len(txts["companies"])):
    strz="/Users/vmac/Downloads/"+str(txts["companies"][sz])+".csv"
    ab=pd.read_csv(strz, encoding="utf-8-sig")

    theDates=ab['Date']
    theVals=ab['Close']

    theDate2 = np.zeros(len(theDates))
    for i in range(0,len(theDate2)):
        totalString=theDates[i].split('-')
        day=totalString[0]
        month=totalString[1]
        year=totalString[2]
        if month=='Jan':
            theDay='01'
        elif month=='Feb':
            theDay='02'
        elif month=='Mar':
            theDay='03'
        elif month=='Apr':
            theDay='04'
        elif month=='May':
            theDay='05'
        elif month=='Jun':
            theDay='06'
        elif month=='Jul':
            theDay='07'
        elif month=='Aug':
            theDay='08'
        elif month=='Sep':
            theDay='09'
        elif month=='Oct':
            theDay='10'
        elif month=='Nov':
            theDay='11'
        elif month=='Dec':
            theDay='12'
        realDate=day+'/'+theDay+'/'+'20'+year
        theDate2[i]=time.mktime(datetime.datetime.strptime(realDate, "%d/%m/%Y").timetuple())

    #print theDate2
    #print txts["companies"][sz],len(theDate2)
    if len(theDate2)>=3775:
        datas=np.c_[datas,theVals[0:3775]]
        print txts["companies"][sz]
        theNames.append(txts["companies"][sz])
#print datas.shape

#print datas[0:10,1:].transpose()
fig2 = plt.figure()

fig2.add_axes([0.05,0.05,0.87,0.87],xticklabels=theNames, xticks=[1,2,3,4,5,6,7,8,9,10,11],yticklabels=theNames,yticks=[1,2,3,4,5,6,7,8,9,10,11], title="corr matrix (backwards time) 1/6/15 - 1/3/00 10 day sliding window")
i=0
imgs=[]
theRanges=np.arange(0,12)
theY=np.arange(0,12)
#print theRanges
#print theY

imgs.append((plt.pcolor(theRanges, theY, np.zeros((11,11)), norm=plt.Normalize(0, 1)),))
while i+10 <=3774:
    submat = datas[i:i+10,1:]
    i=i+1
    awz=np.corrcoef(submat.transpose())
    #print awz.shape
    imgs.append((plt.pcolor(theRanges, theY, awz*255, norm=plt.Normalize(0, 1)),))
imgs.append((plt.pcolor(theRanges, theY, np.zeros((11,11)), norm=plt.Normalize(0, 1)),))
im_ani = animation.ArtistAnimation(fig2, imgs, interval=150, repeat_delay=7000,
    blit=False)

plt.colorbar()
plt.show()

im_ani.save('sample_tech_stock_animation.mp4', fps=10)

#print submat.transpose()
