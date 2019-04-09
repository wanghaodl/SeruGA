#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 20:06:51 2018

@author: wanghao
"""
import numpy as np

def SeruDecoding(Chromesomes, Cells, SCt, Tnl, ril, myProTypes, myProSizes):
    Product_Worker_Time = ProcessTime(ril, Tnl)
    ChromeCellProductType = {}      #存储各个染色体，各个单元先后加工的产品种类
    TTPT = []   # 产品总流通时间
    TLH = []    # 工人总加工时间
    for k,v in Chromesomes.items():
        ChromeCellProductType[k] = {m:[] for m in range(1, len(Cells[k])+1)}
        CellProcessTime = [0 for m in range(0,len(Cells[k]))]
        TLH.append(0)

        for i in range(0,len(myProTypes)):
            seru = CellProcessTime.index(min(CellProcessTime))
            TBm = sum([Product_Worker_Time[myProTypes[i]][j-1] for j in Cells[k][seru]]) * myProSizes[i] / (len(Cells[k][seru]))**2
            ChromeCellProductType[k][seru+1].append(myProTypes[i])
            TLH[k-1] += TBm * len(Cells[k][seru])
            if (i>0 and myProTypes[i]==myProTypes[i-1]):
                CellProcessTime[seru] += TBm
            else:
                CellProcessTime[seru] += (TBm + SCt[myProTypes[i]])

        TTPT.append(max(CellProcessTime))
        
    return TTPT,  TLH, ChromeCellProductType


'''
Product_Worker_Time = {1:[T1，T2，T3...], 2:[], 3:[], 4:[], 5:[]}
返回产品1，2，3，4，5由各个工人执行的时间，如工人1组装产品1用时T1
'''
def ProcessTime(WorkerSkill, ProcedureTime):
    Product_Worker_Time = {}
    for k1,v1 in ProcedureTime.items():
        Product_Worker_Time[k1] = []
        for k2,v2 in WorkerSkill.items():
            Product_Worker_Time[k1].append(sum([v1[i]*v2[i] for i in range(0,len(v1))]))
    return Product_Worker_Time