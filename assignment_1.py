# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:39:37 2022

@author: ZhangXY
"""

import os 
import numpy as np
import pandas as pd
from func import read_refdata,cal_euclidean,plot_figure

#定义路径，注意文件夹之间用“\\”最后要有个“\\”
path='F:\\0_Timothy\\work_desk\\ERS_assignment\\ERS Data Process\\ASCIIdata_splib07b_cvASD\\'

#获取所有文件的完整路径名
all_files_path=[]
for root, dirs, files in os.walk(path,topdown=False):
    if len(files)>0:
        each_foder_files=[os.path.join(root,x) for x in files]
        all_files_path.extend(each_foder_files)

#读取预处理好的样本reflectance数据        
sample_data = pd.read_csv('F:\\0_Timothy\\work_desk\\ERS_assignment\\ERS Data Process\\raw_spectral_data.csv')
obj1_reflect = np.array(list(sample_data['Sample_4']))
obj2_reflect = np.array(list(sample_data['Sample_5']))
obj1_reflect = np.reshape(obj1_reflect, (2151,1))
obj2_reflect = np.reshape(obj2_reflect, (2151,1))

#读取USGS数据库文件
adptd_files_path = []
ref_reflect,adptd_files_path = read_refdata(all_files_path)

#计算测样数据与USGS样本的欧几里得距离并获取距离最小样本索引
obj1_index,obj2_index = cal_euclidean(obj1_reflect[0:1500], obj2_reflect[0:1500], ref_reflect[0:1500,:])

#输出结果
print('The sample 4 is most similar to',adptd_files_path[obj1_index])
print('The sample 5 is most similar to',adptd_files_path[obj2_index])

#绘制反射光谱
wvlen = np.array(list(sample_data.index))
plot_figure(wvlen[0:1500],obj1_reflect,ref_reflect,obj1_index,'Sample 4')
plot_figure(wvlen[0:1500],obj2_reflect,ref_reflect,obj2_index,'Sample 5')
