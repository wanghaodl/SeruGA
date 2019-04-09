#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 20:59:50 2018

@author: wanghao
"""
import copy

def DelRep(P_Chromes, P_Cells, Worker):
    Chromes = copy.deepcopy(P_Chromes)
    UniqueChromes = {}
    for k,v in Chromes.items():
        sub_chr = [i if i <= Worker else 0 for i in v]
        v = []
        for i in range(0,len(sub_chr)-1):
            if sub_chr[i]==0 and sub_chr[i+1]==0:
                continue
            else: 
                v.append(sub_chr[i])
        if v[0]!=0:
            v.insert(0,0)
        if v[-1]!=0:
            v.append(0)
    
    for k,v in Chromes.items():
        if v not in UniqueChromes.values():
            UniqueChromes[k] = copy.deepcopy(v)
    C_Cells = {}
    C_Chromes = {}
    i = 1
    for k,v in UniqueChromes.items():
#        UniqueChromes[k] = copy.deepcopy(P_Chromes[k])
        C_Chromes[i] = copy.deepcopy(P_Chromes[k])
        C_Cells[i] = copy.deepcopy(P_Cells[k])
        i = i+1

#    for i in range(0,len(TTPT)):
#        if i+1 not in UniqueChromes.keys():
#            TTPT[i] = max(TTPT)
#            TLH[i] = max(TLH)
        
    return C_Chromes, C_Cells