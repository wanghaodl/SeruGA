#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 20:54:04 2018

@author: wanghao
"""
import copy


def SeruFitness(TTPT, TLH):
    time_values = copy.deepcopy(TTPT)
    salaries = copy.deepcopy(TLH)
    
    F = {}
    F[1] = []
    rank = [0 for i in range(0,len(time_values))]
    sp = {}
    n_p = {}
    for p in range(0,len(time_values)):
        sp[p] = []     #表示p支配的个体
        n_p[p] = 0      #表示支配p的个体
        for q in range(0,len(time_values)):
            if p!=q:
                if (salaries[p]<=salaries[q] and time_values[p]<=time_values[q]):
                    sp[p].append(q)
                elif (salaries[p]>=salaries[q] and time_values[p]>=time_values[q]):
                    n_p[p] = n_p[p] + 1
        if n_p[p] == 0:
            rank[p] = 1
            F[rank[p]].append(p)
    i = 1
    while len(F[i])!=0:
        Q = []
        for p in F[i]:
            for q in sp[p]:
                n_p[q] = n_p[q] - 1
                if n_p[q] == 0:
                    rank[q] = i + 1
                    Q.append(q)
        i = i + 1
        F[i] = Q
    F.pop(i)

# 计算拥挤度距离
    f_max_s = max(salaries)
    f_min_s = min(salaries)
    f_max_t = max(time_values)
    f_min_t = min(time_values)
#    print('f_max_s:{}    f_min_s:{}'.format(f_max_s,f_min_s))
#    print('f_max_t:{}    f_min_t:{}'.format(f_max_t,f_min_t))
    #print(salaries)
    crowd = {}
    for k,v in F.items():
        crowd[k] = [0 for val in v]
        if len(v)<=2:   # 同一层小于两个的话，
            for i in range(0,len(v)):
                crowd[k][i] = float('inf')
            continue
        
        #fk_s = [salaries[i-1] for i in v]   ???-1是什么情况
        fk_s = [salaries[i] for i in v]   
         
        fk_s1 = fk_s.copy()
        #fk_t = [time_values[i-1] for i in v]    ?? -1是什么情况
        fk_t = [time_values[i] for i in v]
        #fk_t1 = fk_t.copy()
        fk_s.sort()     # 对pareto前沿进行排序
        fk_t.sort(reverse=True)
        s1 = fk_s1.index(fk_s[0])    # 确定pareto前沿的端点
        fk_s1[s1] = -1
        crowd[k][s1] = float('inf')
        s1 = fk_s1.index(fk_s[-1])   # 确定pareto前沿的端点
        fk_s1[s1] = -1
        crowd[k][s1] = float('inf')     # 端点的拥挤距离为无穷大
        for i in range(1,len(fk_s)-2):

            #print(fk_t[i+1]-fk_t[i-1])
            d1 = abs(fk_s[i+1]-fk_s[i-1])/(f_max_s-f_min_s) if f_max_s != f_min_s else 1
            d2 = abs(fk_t[i+1]-fk_t[i-1])/(f_max_t-f_min_t) if f_max_t != f_min_t else 1
            crowd[k][fk_s1.index(fk_s[i])] = d1 + d2
            #indx = crowd[k][fk_s1.index(fk_s[i])]    # 确定各点对应的位置
            #d = time_values[F[k][indx]-1]
    temp_crowd = []
    for v in crowd[1]:
        if v!=0:
            temp_crowd.append(v)
#    print('拥挤度种类数:{}'.format(len(temp_crowd)))
#    print(temp_crowd)
    
    return F,crowd,time_values,salaries