#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 20:01:03 2018

@author: wanghao
"""

import random

'''
两段式编码，一个单元构建段，一个批量分割段。
单元构建段随机数编码
批量分割分为五个部分，每个部分一个产品。每个产品用游标的方式分成W段（W=工人数）
参数：Worker:工人数，Proudct:{产品种类:产品数量}，Population:种群数
'''
def SeruEncoding(Worker, Product, Population):
    Chromesomes = {}
    Cells = {}
    for i in range(1,Population+1):
        '''染色体第一段的构建，单元构建段'''
        
        WorkerChrome = [m for m in range(1,Worker*2)]
        random.shuffle(WorkerChrome)
        WorkerChrome.append(Worker*2)
        Chromesomes[i] = WorkerChrome
        
        '''单元信息'''
        Cells[i] = [[]]   # 用于存储每个基因的各个单元
        for j in range(0,len(WorkerChrome)-1):
            if WorkerChrome[j]//(Worker+1)==0:
                Cells[i][-1].append(WorkerChrome[j])
            if WorkerChrome[j]//(Worker+1)==0 and WorkerChrome[j+1]//(Worker+1)!=0:
                Cells[i].append([])
        Cells[i].pop(-1)
        
    return Chromesomes, Cells