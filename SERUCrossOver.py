#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 20:34:25 2018

@author: wanghao
"""
import copy
import random

def SeruCrossOver(P_Chromes, P_Cells, Worker, probability = 0.8):
    Chromes = copy.deepcopy(P_Chromes)
    Cells = copy.deepcopy(P_Cells)
    chr_id = list(Chromes.keys())
    random.shuffle(chr_id)
    for i in range(0,len(chr_id),2):
        m = chr_id[i]
        n = chr_id[i+1]   
        if random.random()<=probability:
     
            l = len(Chromes[m])-1
            x = random.choice(range(1,len(Chromes[m])-1))
            y = random.choice(range(1,len(Chromes[m])-1))
            pos1 = min(x,y)
            pos2 = max(x,y)
            P_chr1 = Chromes[m][pos2:l]+Chromes[m][:pos1]+Chromes[m][pos1:pos2]
            P_chr2 = Chromes[n][pos2:l]+Chromes[n][:pos1]+Chromes[n][pos1:pos2]
            frag1 = Chromes[m][pos1-1:pos2]
            frag2 = Chromes[n][pos1-1:pos2]
    
            for v in frag2:
                P_chr1.remove(v)
            for v in frag1:
                P_chr2.remove(v)
            Chromes[m] = P_chr2[pos1-2:]+frag1+P_chr2[:pos1-2]+Chromes[m][-1:]
            Chromes[n] = P_chr1[pos1-2:]+frag2+P_chr1[:pos1-2]+Chromes[m][-1:]
        
        Cells[m] = [[]]   # 用于存储每个基因的各个单元        
        for j in range(0,len(Chromes[m])-1):
            if Chromes[m][j]//(Worker+1)==0:
                Cells[m][-1].append(Chromes[m][j])
            if Chromes[m][j]//(Worker+1)==0 and Chromes[m][j+1]//(Worker+1)!=0:
                Cells[m].append([])
        Cells[m].pop(-1)

        Cells[n] = [[]]   # 用于存储每个基因的各个单元        
        for j in range(0,len(Chromes[n])-1):
            if Chromes[n][j]//(Worker+1)==0:
                Cells[n][-1].append(Chromes[n][j])
            if Chromes[n][j]//(Worker+1)==0 and Chromes[n][j+1]//(Worker+1)!=0:
                Cells[n].append([])
        Cells[n].pop(-1)
        
    return Chromes, Cells