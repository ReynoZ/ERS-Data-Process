# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 14:04:06 2022

@author: ZhangXY
"""

import numpy as np
import pandas as pd

veg = pd.read_table(r'F:\0_Timothy\work_desk\ERS_assignment\ERS Data Process\Landsat 8 data\vegetation.txt',skiprows=(3),header=None,sep='  ')
wtr = pd.read_table(r'F:\0_Timothy\work_desk\ERS_assignment\ERS Data Process\Landsat 8 data\water.txt',skiprows=(3),header=None,sep='  ')
uba = pd.read_table(r'F:\0_Timothy\work_desk\ERS_assignment\ERS Data Process\Landsat 8 data\urban_area.txt',skiprows=(3),header=None,sep='  ')
cld = pd.read_table(r'F:\0_Timothy\work_desk\ERS_assignment\ERS Data Process\Landsat 8 data\cloud.txt',skiprows=(3),header=None,sep='  ')

