#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

import numpy as np 
import matplotlib.pyplot as plt
import os 
from scipy import optimize 

Pfad='./'
charge='m35'
jpg='.jpg'

Path0='/imports/dodo.work/priscel/SIO2/plus20/Confined/'
Path1=Path0+'T'
Path2='K/ISFNoCOM_D/Daten/'
Ende='.dat'
dataPath='./scripts_w/TauData/'
Savepath=Path0+dataPath
Auswahl=np.array([3900,4100,4500,4900,7000])

Farbenauswahl=['r','orange','k','olive','maroon','pink',]
Symbolauswahl=['D','<','H','8','d','p','h','+','2','3','4','8','p','D','d','x','h','H']
laengeF=len(Farbenauswahl)
laengeS=len(Symbolauswahl)

#labelinY=r"$<\ |\ \vec{r}(t)-\vec{r}(0)\ |^2\ >$" + ' / '+"$\AA ^2$"
labelinY="$ISF$"
labelinX="$t$ / ps"
ticksize=16
titlesize=20
ysize=18
xsize=ysize

Legendsize=12

AxisDown1      = -0.65
AxisHeightDelt = 0.06
AxisHeight     = 0.5*(0.945 - AxisDown1 - AxisHeightDelt)
AxisDown2      = AxisDown1 + AxisHeight + AxisHeightDelt
AxisLeft1      = 0.09
AxisLeft2      = 0.5*(0.98 - AxisLeft1) + AxisLeft1
AxisWidth      = AxisLeft2 - AxisLeft1


Rmax=20.1
Rstep=0.1
R0=0.0
rl=int((Rmax-R0)/Rstep)
lc=len(Farbenauswahl)

k=-1
fig = plt.figure(figsize=(25,14))
plt.rcParams['axes.linewidth'] = 3
plt.axes((AxisLeft1, AxisDown2, AxisWidth-0.025, AxisHeight))
plt.rc('legend',**{'fontsize':27})
for i in range(len(Auswahl)):  
    T=Auswahl[i]
    Temp=str(T)
    print T
    NameZ=Path1+Temp+Path2+'IntermediaereStreufunktion_Int_Counter'+Ende
    NameW=Path1+Temp+Path2+'IntermediaereStreufunktion_Basis-Daten'+Ende
    print NameZ  
    k=k+1
    Farbe1a= Farbenauswahl[k%lc]+Symbolauswahl[k%lc]
    Farbe1b= Farbenauswahl[k%lc]+'-' 
    if ( os.path.exists ( NameZ ) ) :
       datenZ=np.loadtxt(NameZ)
       datenW=np.loadtxt(NameW)
       CounterO=datenZ[:,2]
       Nshifts=np.double(datenW[4])
    hdlp01=plt.plot(datenZ[:,1]/10.0, datenZ[:,2]/(1*Nshifts*21), color=Farbenauswahl[k%lc], marker=Symbolauswahl[k%lc], markersize = 20, linewidth=0,label = Temp+ ' K')
       #hdlp02=plt.plot(datenX,func1(Startparameter[0],Startparameter[1],Startparameter[2],datenX), Farbe1b, linewidth = 8)
plt.xlabel(r"$d$"+' / '+'nm',fontsize=30)
plt.ylabel(r"Distribution"+'',fontsize=30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.ticklabel_format(axis='y', style='sci', scilimits=(-4,4),fontsize = 100)
plt.title('O', y=1.01, fontsize=35)  
plt.grid()
plt.xlim((0, 1.0))
plt.legend(loc='upper right')
plt.text(0.61,2.4, r"$q/q_0 = 1.21$" , fontsize=35)
plt.text(0.61,2, '(b)' , fontsize=35)
plt.ylim((0, 4))
ax = plt.gca()
ax.tick_params(width=5, pad=12)

k=-1
plt.axes((AxisLeft2+0.025, AxisDown2, AxisWidth-0.025, AxisHeight))
for i in range(len(Auswahl)):  
    T=Auswahl[i]
    Temp=str(T)
    print T
    NameZ=Path1+Temp+Path2+'IntermediaereStreufunktion_Int_Counter'+Ende
    NameW=Path1+Temp+Path2+'IntermediaereStreufunktion_Basis-Daten'+Ende
    print NameZ  
    k=k+1
    Farbe1a= Farbenauswahl[k%lc]+Symbolauswahl[k%lc]
    Farbe1b= Farbenauswahl[k%lc]+'-' 
    if ( os.path.exists ( NameZ ) ) :
       datenZ=np.loadtxt(NameZ)
       datenW=np.loadtxt(NameW)
       CounterO=datenZ[:,3]
       Nshifts=np.double(datenW[4])
    hdlp01=plt.plot(datenZ[:,1]/10.0, datenZ[:,2]/(1*Nshifts*25), color=Farbenauswahl[k%lc], marker=Symbolauswahl[k%lc], markersize = 20,linewidth=0, label = Temp+ ' K')
       #hdlp02=plt.plot(datenX,func1(Startparameter[0],Startparameter[1],Startparameter[2],datenX), Farbe1b, linewidth = 8)
plt.xlabel(r"$d$"+' / '+'nm',fontsize=30)
#plt.ylabel(r"N"+'',fontsize=30)
plt.xticks(fontsize = 30)
plt.yticks(fontsize = 30)
plt.ticklabel_format(axis='y', style='sci', scilimits=(-4,4),fontsize = 100)
plt.title('Si', y=1.01, fontsize=35)  
plt.text(1.41,70, '(d)' , fontsize=35)
plt.grid()
plt.xlim((0, 2.0))
#plt.legend(loc='upper right')
ax = plt.gca()
ax.tick_params(width=5, pad=12)
plt.savefig(Savepath+'./'+'Si_O_ISF_count'+jpg)
plt.show()
