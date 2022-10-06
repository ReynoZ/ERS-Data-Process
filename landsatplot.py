# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 14:04:06 2022

@author: ZhangXY
"""

import pandas as pd
import matplotlib.pyplot as plt

veg = pd.read_table(r'F:\0_Timothy\work_desk\ERS_assignment\ERS Data Process\Landsat 8 data\vegetation2.txt',skiprows=(3),header=None,sep='  ')
wtr = pd.read_table(r'F:\0_Timothy\work_desk\ERS_assignment\ERS Data Process\Landsat 8 data\water.txt',skiprows=(3),header=None,sep='  ')
uba = pd.read_table(r'F:\0_Timothy\work_desk\ERS_assignment\ERS Data Process\Landsat 8 data\urban_area2.txt',skiprows=(3),header=None,sep='  ')
cld = pd.read_table(r'F:\0_Timothy\work_desk\ERS_assignment\ERS Data Process\Landsat 8 data\cloud2.txt',skiprows=(3),header=None,sep='  ')


veg[1]=veg[1]*0.0001
wtr[1]=wtr[1]*0.0001
uba[1]=uba[1]*0.0001
cld[1]=cld[1]*0.0001

veg[0]=veg[0]*1000
wtr[0]=wtr[0]*1000
uba[0]=uba[0]*1000
cld[0]=cld[0]*1000

fig = plt.figure(figsize=(10,8),dpi=150)
plt.plot(veg[0],veg[1])
plt.plot(wtr[0],wtr[1])
plt.plot(uba[0],uba[1])
plt.plot(cld[0],cld[1])
plt.legend(['vegetation','water','urban area','cloud'])
plt.title('Landsat 8 typical spectral reflectance profiles',fontsize=20)
plt.xlabel('Wavelength '+r'$(nm$)', fontsize=15)
plt.ylabel('Reflectance', fontsize=15)