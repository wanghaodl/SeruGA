#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 20:00:12 2018

@author: wanghao
"""

#import SERUAssembleLine
import SERUEncoding
import SERUCrossOver
import SERUMutation
import SERUDecoding
import SERUDelRepetition
import SERUFitness
import SERUSelection
import copy
import matplotlib.pyplot as plt
import time
import pandas as pd

def ParaInitial(Worker, Product, Population, SCt, Tnl, ril, Gen):
    '''生成初始种群'''
    INIT_Chromes, INIT_Cells = SERUEncoding.SeruEncoding(Worker, Product, Population)
    INIT_TTPT, INIT_TLH, INIT_CellProductBatchSize = SERUDecoding.SeruDecoding(INIT_Chromes, INIT_Cells, SCt, Tnl, ril, myProTypes, myProSizes)
    Chromes = copy.deepcopy(INIT_Chromes)
    Cells = copy.deepcopy(INIT_Cells)    
    '''开始进化'''
    for i in range(0, Gen):
        if (i+1)%10 == 0:
            print('第{}代'.format(i+1))
        
        '''交叉'''
        C_Chromes, C_Cells = SERUCrossOver.SeruCrossOver( Chromes, Cells, Worker, probability = 0.8)
        '''变异'''
        C_Chromes, C_Cells = SERUMutation.SeruMutation(C_Chromes, C_Cells, Worker, Probability=0.2)
        '''父代、子代合并'''
        for k in Chromes.keys():
            C_Chromes[k+len(Chromes.keys())] = copy.deepcopy(Chromes[k])
            C_Cells[k+len(Chromes.keys())] = copy.deepcopy(Cells[k])
        '''去重'''
        C_Chromes, C_Cells = SERUDelRepetition.DelRep(C_Chromes, C_Cells, Worker)
        #print(len(C_Cells))
        '''解码'''        
        TTPT, TLH, ChromeCellProductType = SERUDecoding.SeruDecoding(C_Chromes, C_Cells, SCt, Tnl, ril, myProTypes, myProSizes)
        '''适应度计算'''
        F, Crowd, TTPT, TLH = SERUFitness.SeruFitness(TTPT, TLH)
        '''选择'''
        Chromes, Cells = SERUSelection.SeruSelection(F, Crowd, C_Chromes, C_Cells, Population)  
  
    '''解码'''        
    TTPT, TLH, CellProductBatchSize = SERUDecoding.SeruDecoding(Chromes, Cells, SCt, Tnl, ril, myProTypes, myProSizes)
    '''适应度计算'''
    F, Crowd, TTPT, TLH = SERUFitness.SeruFitness(TTPT, TLH)    


    return Chromes, Cells, TTPT, TLH, CellProductBatchSize, F, INIT_TTPT, INIT_TLH, INIT_CellProductBatchSize
'''20个工人，20个工序的情况'''
ril = {1:[1.00, 1.02, 1.05, 1.02, 1.04, 1.08, 1.00, 1.04, 1.05, 1.06, 1.03, 1.12, 1.00, 1.03, 1.02, 1.00, 1.11, 1.16, 1.01, 1.02],
       2:[1.06, 1.10, 1.00, 1.03, 1.07, 1.02, 1.07, 1.03, 1.11, 1.00, 1.10, 1.08, 1.01, 1.02, 1.04, 1.01, 1.08, 1.00, 1.00, 1.07],
       3:[1.04, 1.03, 1.00, 1.07, 1.06, 1.09, 1.08, 1.04, 1.07, 1.00, 1.09, 1.04, 1.05, 1.03, 1.01, 1.08, 1.03, 1.04, 1.07, 1.02],
       4:[1.04, 1.05, 1.10, 1.00, 1.08, 1.00, 1.05, 1.14, 1.02, 1.05, 1.19, 1.05, 1.02, 1.14, 1.08, 1.06, 1.02, 1.12, 1.00, 1.03],
       5:[1.10, 1.17, 1.05, 1.01, 1.00, 1.07, 1.10, 1.03, 1.02, 1.13, 1.12, 1.14, 1.04, 1.03, 1.01, 1.04, 1.00, 1.00, 1.02, 1.07],
       6:[1.08, 1.09, 1.03, 1.13, 1.05, 1.00, 1.09, 1.03, 1.08, 1.06, 1.01, 1.08, 1.05, 1.00, 1.03, 1.13, 1.09, 1.13, 1.02, 1.03],
       7:[1.10, 1.13, 1.10, 1.11, 1.03, 1.17, 1.00, 1.03, 1.06, 1.03, 1.12, 1.00, 1.02, 1.00, 1.02, 1.05, 1.06, 1.02, 1.00, 1.01],
       8:[1.03, 1.15, 1.01, 1.09, 1.01, 1.07, 1.03, 1.00, 1.00, 1.06, 1.04, 1.06, 1.01, 1.00, 1.12, 1.07, 1.03, 1.03, 1.07, 1.05],
       9:[1.03, 1.15, 1.04, 1.12, 1.07, 1.06, 1.06, 1.11, 1.04, 1.01, 1.00, 1.06, 1.04, 1.00, 1.07, 1.00, 1.07, 1.08, 1.04, 1.08],
       10:[1.08, 1.06, 1.09, 1.04, 1.02, 1.05, 1.00, 1.01, 1.05, 1.05, 1.00, 1.09, 1.11, 1.11, 1.07, 1.09, 1.07, 1.09, 1.04, 1.03],
       11:[1.05, 1.05, 1.12, 1.08, 1.05, 1.00, 1.00, 1.07, 1.00, 1.06, 1.08, 1.00, 1.16, 1.03, 1.00, 1.15, 1.14, 1.13, 1.01, 1.00],
       12:[1.13, 1.03, 1.05, 1.05, 1.14, 1.15, 1.08, 1.11, 1.02, 1.08, 1.07, 1.12, 1.09, 1.11, 1.11, 1.05, 1.08, 1.01, 1.06, 1.01],
       13:[1.06, 1.11, 1.12, 1.12, 1.13, 1.04, 1.08, 1.05, 1.09, 1.04, 1.12, 1.09, 1.03, 1.10, 1.04, 1.11, 1.06, 1.00, 1.08, 1.14],
       14:[1.00, 1.15, 1.13, 1.15, 1.09, 1.10, 1.06, 1.03, 1.12, 1.03, 1.05, 1.05, 1.10, 1.02, 1.00, 1.01, 1.02, 1.05, 1.04, 1.09],
       15:[1.10, 1.08, 1.12, 1.06, 1.15, 1.18, 1.08, 1.04, 1.03, 1.00, 1.02, 1.06, 1.03, 1.03, 1.03, 1.09, 1.00, 1.00, 1.07, 1.10],
       16:[1.19, 1.06, 1.07, 1.15, 1.07, 1.11, 1.10, 1.04, 1.00, 1.12, 1.10, 1.00, 1.06, 1.02, 1.05, 1.04, 1.10, 1.04, 1.06, 1.00],
       17:[1.10, 1.05, 1.05, 1.08, 1.15, 1.00, 1.06, 1.00, 1.03, 1.03, 1.04, 1.03, 1.04, 1.06, 1.05, 1.04, 1.09, 1.08, 1.02, 1.08],
       18:[1.15, 1.11, 1.15, 1.15, 1.19, 1.10, 1.07, 1.00, 1.08, 1.10, 1.08, 1.11, 1.00, 1.07, 1.00, 1.00, 1.00, 1.03, 1.08, 1.00],
       19:[1.04, 1.00, 1.12, 1.09, 1.12, 1.04, 1.05, 1.06, 1.12, 1.08, 1.04, 1.07, 1.03, 1.06, 1.13, 1.05, 1.00, 1.00, 1.06, 1.12],
       20:[1.04, 1.12, 1.10, 1.01, 1.04, 1.13, 1.03, 1.17, 1.00, 1.10, 1.09, 1.00, 1.00, 1.02, 1.00, 1.01, 1.07, 1.02, 1.00, 1.02]}

'''5种产品，6个工序'''
Tnl = {1:[1.4, 1.8, 1.5, 1.6, 1.4, 1.6],
       2:[1.4, 1.6, 1.6, 1.5, 1.4, 1.8],
       3:[1.4, 1.5, 1.6, 1.8, 1.7, 1.4],
       4:[1.7, 1.4, 1.5, 1.6, 1.6, 1.8],
       5:[1.7, 1.6, 1.5, 1.4, 1.5, 1.7]}

'''5种产品，10个工序'''
#Tnl = {1:[1.4, 1.8, 1.5, 1.6, 1.4, 1.6, 1.4, 1.6, 1.5, 1.4],
#       2:[1.4, 1.6, 1.6, 1.5, 1.4, 1.8, 1.4, 1.5, 1.5, 1.4],
#       3:[1.4, 1.5, 1.6, 1.8, 1.7, 1.4, 1.4, 1.8, 1.6, 1.5],
#       4:[1.7, 1.4, 1.5, 1.6, 1.6, 1.8, 1.5, 1.4, 1.5, 1.7],
#       5:[1.7, 1.6, 1.5, 1.4, 1.5, 1.7, 1.5, 1.6, 1.5, 1.4]}

'''5种产品，20个工序'''
#Tnl = {1:[1.4, 1.8, 1.5, 1.6, 1.4, 1.6, 1.4, 1.6, 1.5, 1.4, 1.6, 1.6, 1.4, 1.6, 1.8, 1.4, 1.7, 1.8, 1.5, 1.6],
#       2:[1.4, 1.6, 1.6, 1.5, 1.4, 1.8, 1.4, 1.5, 1.5, 1.4, 1.8, 1.7, 1.4, 1.8, 1.4, 1.5, 1.4, 1.8, 1.7, 1.6],
#       3:[1.4, 1.5, 1.6, 1.8, 1.7, 1.4, 1.4, 1.8, 1.6, 1.5, 1.6, 1.4, 1.4, 1.5, 1.5, 1.7, 1.6, 1.7, 1.5, 1.4],
#       4:[1.7, 1.4, 1.5, 1.6, 1.6, 1.8, 1.5, 1.4, 1.5, 1.7, 1.8, 1.8, 1.5, 1.8, 1.5, 1.4, 1.7, 1.8, 1.4, 1.5],
#       5:[1.7, 1.6, 1.5, 1.4, 1.5, 1.7, 1.5, 1.6, 1.5, 1.4, 1.4, 1.7, 1.5, 1.8, 1.4, 1.7, 1.6, 1.8, 1.8, 1.5]}

Product = {1: 205, 2: 489, 3: 247, 4: 203, 5: 327}
myProTypes = [1, 2, 1, 2, 2, 5, 1, 2, 3, 3, 2, 2, 4, 2, 5, \
              4, 3, 1, 5, 2, 5, 2, 4, 2, 5, 3, 5, 3, 4, 5]
myProSizes = [61, 52, 47, 56, 38, 42, 55, 43, 49, 53, 49, 52, 46, 57, 54, \
              49, 48, 42, 41, 59, 60, 39, 60, 44, 42, 51, 44, 46, 48, 44]

SLt = {1:2.3, 2:2.4, 3:2.2, 4:2.6, 5:2.1} #流水线中产品转换时间 
SCt = {1:1.3, 2:1.4, 3:1.2, 4:1.6, 5:1.1}    # 单元中流水转换时间
Tn = 1.8    #节拍时间
Worker = len(Tnl[1])
Population = 150
Gen = 80


#LTTPT, LTLH = SERUAssembleLine.LineProcessTime(SLt, Tn, myProTypes, myProSizes, Tnl)
print('开始FCFS')
print('初始种群：{}'.format(Population))
print('进化代数：{}'.format(Gen))

Begin = time.time()

Chromes, Cells ,TTPT, TLH, CellProductBatchSize, F, INIT_TTPT, INIT_TLH, INIT_CellProductBatchSize = ParaInitial(Worker, Product, Population, SCt, Tnl, ril, Gen)

End = time.time()

print('用时{}s'.format(End-Begin))

x = []
y = []
l = []
pos = []
for k in F[1]:
    pos.append(k)
    x.append(TTPT[k])
    y.append(TLH[k])
    l.append(len(Cells[k+1]))

result = []
z = copy.deepcopy(x)
z.sort()
inst = copy.deepcopy(x)
for v in z:
    i = inst.index(v)
    inst[i] = -1
    result.append(i)
To_TTPT = {}
To_TLH = {}
To_Cells = {}
ProductCellBatchSize = {} 
for v in result:
    To_TTPT[v+1] = round(TTPT[v],2)
    To_TLH[v+1] = round(TLH[v],2)
    To_Cells[v+1] = Cells[v+1]
    print('{}:  TTPT:{}    TLH:{}'.format(v+1, round(TTPT[v],2),round(TLH[v],2)))

df = pd.DataFrame([To_TTPT, To_TLH, To_Cells, ProductCellBatchSize]).T
df.to_excel('result_FCFS.xlsx')

m = min(l)
n = max(l)
for i in range(m,n+1):
    print('{}:{}'.format(i,l.count(i)))
print('FCFS')
x.sort()
y.sort(reverse = True)    
plt.xlabel('TTPT')
plt.ylabel('TLH')
plt.plot(x,y,marker = 'o')
plt.scatter(TTPT, TLH, marker = 'v', c='y')
