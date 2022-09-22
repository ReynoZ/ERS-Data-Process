# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:56:43 2022

@author: ZhangXY
"""

import numpy as np
import matplotlib.pyplot as plt

def read_refdata(filepaths):
    ref_reflect = np.zeros((2151,1))
    adptd_files_path = []
    for filepath in filepaths:
        path = np.loadtxt(filepath,skiprows=1)
        path = np.reshape(path,(2151,1))
        path[path<0] = 0 
        indice = path[0:1500].sum(axis=0)
        if indice[0]>50:
            ref_reflect = np.column_stack((ref_reflect,path))
            adptd_files_path.append(filepath)

    ref_reflect = np.delete(ref_reflect, [0], axis=1)       
    
    return ref_reflect,adptd_files_path
  
def cal_euclidean(obj1_reflect,obj2_reflect,ref_reflect):
    ob1_distance = np.sqrt(((obj1_reflect-ref_reflect)**2).sum(axis=0))
    ob2_distance = np.sqrt(((obj2_reflect-ref_reflect)**2).sum(axis=0))
    
    ob1_index = np.argmin(ob1_distance)
    ob2_index = np.argmin(ob2_distance)
    
    return ob1_index,ob2_index

def plot_figure(wvlen,obj_reflect,ref_reflect,obj_index,samplename):
    fig = plt.figure(figsize=(10,8),dpi=150)

    plt.scatter(wvlen,obj_reflect[0:1500])
    tgt_reflect = np.reshape(ref_reflect[:,obj_index],(2151,))
    plt.scatter(wvlen,tgt_reflect[0:1500],color='red')

    plt.ylabel('Reflectance')
    plt.xlabel('Wavelength')
    plt.title(samplename,fontsize = 25)
    plt.legend([samplename,'USGS reference'],loc='lower right',fontsize = 20)
    
    
