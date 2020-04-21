import matplotlib.pyplot as plt
import numpy as np
from pylab import plot, show, xticks, yticks, title, xlabel, ylabel, legend, savefig 

x=['Sept. 30, 2015','Oct. 31, 2015','Nov. 30, 2015','Dec. 31, 2015',
   'Jan. 31, 2016','Feb. 29, 2016','March 31, 2016','April 30, 2016','May 31, 2016','June 30, 2016','July 31, 2016','Aug. 31, 2016','Sept. 30, 2016','Oct. 31, 2016','Nov. 30, 2016','Dec. 31, 2016',
   'Jan. 31, 2017','Feb. 28, 2017','March 31, 2017','April 30, 2017','May 31, 2017','June 30, 2017','July 31, 2017','Aug. 31, 2017','Sept. 30, 2017','Oct. 31, 2017','Nov. 30, 2017','Dec. 31, 2017',
   'Jan. 31, 2018','Feb. 28, 2018','March 31, 2018','April 30, 2018','May 31, 2018','June 30, 2018','July 31, 2018','Aug. 31, 2018','Sept. 30, 2018','Oct. 31, 2018','Nov. 30, 2018','Dec. 31, 2018',
   'Jan. 31, 2019','Feb. 28, 2019','March 31, 2019','April 30, 2019','May 31, 2019','June 30, 2019','July 31, 2019','Aug. 31, 2019','Sept. 30, 2019','Oct. 31, 2019']
   


#IMPORT
y1=[971,771,931,853,539,998,465,741,413,743,540,723,715,472,854,1072,458.35,814.78,
    726.54,1055,768.72,824.17,1176,1395,1286,1374,1626,1719,1535,1358,1616,1407,
    1561,1535,2005,1478,1620,2120,1716,1714,2176,1677,1398,1154,1183,1193,1357,1319,1308,1383]



#EKSPORT
y2=[954,664,574,719,459,508,855,687,794,831,836,813,914,898,749,706,506,659,762,587,593,
    563,595,548,506,501,569,455,437,273,435,381,378,414,393,440,389,403,448,390,365,381,458,
    405,407,389,397,332,287,345]




plot(x,y1,y2,'r')
xticks(['Oct. 31, 2015','Oct. 31, 2016','Oct. 31, 2017','Oct. 31, 2018','Oct. 31, 2019'], fontsize='15', fontname='Arial') 
yticks([0,250,500,750,1000,1250,1500,1750,2000,2120],fontsize='15') 

title("Polski import oraz eksport węgla",fontsize='23', fontname='Arial') 
xlabel("Rok",fontsize='17', fontname='Arial')  
ylabel("Tys. ton",fontsize='17', fontname='Arial')
legend(['Import','Eksport'],fontsize='17')

