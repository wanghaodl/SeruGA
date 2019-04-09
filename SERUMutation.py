#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 20:35:48 2018

@author: wanghao
"""
import copy
import random

def SeruMutation(P_Chromes, P_Cells, Worker, Probability=0.1):
    Chromes = copy.deepcopy(P_Chromes) 
    Cells = copy.deepcopy(P_Cells)
    for k,v in Chromes.items():
        if random.random() <= Probability:
            pos1, pos2 = random.sample(range(0,len(v)-1),2)
            rep = v[pos1]
            v[pos1] = v[pos2]
            v[pos2] = rep
            Cells[k] = [[]]   # 用于存储每个基因的各个单元        
            for j in range(0,len(Chromes[k])-1):
                if Chromes[k][j]//(Worker+1)==0:
                    Cells[k][-1].append(Chromes[k][j])
                if Chromes[k][j]//(Worker+1)==0 and Chromes[k][j+1]//(Worker+1)!=0:
                    Cells[k].append([])
            Cells[k].pop(-1)
    return Chromes, Cells