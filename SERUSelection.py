#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 21:32:09 2018

@author: wanghao
"""

def SeruSelection(F,crowd,chromesomes,Cells,n):
    new_chromesomes = {}
    new_cells = {}
    num = 0
    i = 1
    while True:
        if num+len(F[i])<n:
            for j in F[i]:
                new_chromesomes[num+1] = chromesomes[j+1]
                new_cells[num+1] = Cells[j+1]
                num+=1
#            num = num + len(F[i])
            i = i + 1
        elif num+len(F[i])==n:
            for j in F[i]:
                new_chromesomes[num+1] = chromesomes[j+1]
                new_cells[num+1] = Cells[j+1]
                #num = num + len(F[i])
                num+=1
            break
        else:
            lst = crowd[i].copy()
            ls = crowd[i].copy()
            lst.sort(reverse = True)
            rst = n-num
            for j in range(0,rst):
                k = ls.index(lst[j])
                new_chromesomes[num+1] = chromesomes[k+1]
                new_cells[num+1] = Cells[k+1]
                ls[k] = -1
                num+=1
            #print(ls)
            break
    return new_chromesomes,new_cells