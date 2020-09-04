#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# @Time    : 2020/9/2 16:18
# @File    : temp.py
# @Software: PyCharm
# @Introduction:

'''

11 个点 计算最佳变换参数
experiment on two main transforms T :

Isometrics Transform  3-parameters
affine Transform , 6-parameters

target points :  P_i , i=1,..., 11
source points : Q_i , i=1 ,...,11

  min  cost = \sum( distance(P_i , Q_i) )


附加约束，视效果而定 ： 脖子到脸颊上的两点，要落在变换后的曲线上
'''



def affine_transform():
    pass

P = None
Q = None
def cost_func_affine(T):
    cost = 0.0
    TM =  np.array( [ [ T[0], T[1], T[4] ] , [ T[2] , T[3] ,T[5]  ] , [0, 0, 1]   ]  )
    for i in range(11):
        P_t = np.matmul(TM , P[i]) # note : homogeneus coordinate
        cost +=  (P_t[0] - Q[i][0]) ** 2  + ( P_t[1] - Q[i][1]) ** 2
    return cost


def solve_cost_fun():
    T = None  #
    # T = [a11 ,a12 ,a21 ,a22 , tx ,ty ]
    res = minimize(cost_func_affine, T0, method='nelder-mead', options={'xatol': 1e-8, 'disp': True})
    print(res.x )


#test
import numpy as np
from scipy.optimize import minimize

def rosen(x):
    return sum(100.0 * (x[1:] - x[:-1] ** 2.0) ** 2.0 + (1 - x[:-1]) ** 2.0)


def tes_minimize_rosen():
    x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
    res = minimize(rosen, x0 , method= 'nelder-mead' , options={'xatol': 1e-8, 'disp': True})
    print(res.success)
    print(res.x)

import numpy as np
if __name__ == '__main__':
    X,Y  = np.meshgrid([1,2,3,4],[6,7,8] )
    x_r = X.flatten().reshape((1 , 12 ))
    y_r = Y.flatten().reshape((1 , 12 ))
    np.vstack((x_r, y_r, np.ones_like(x_r)))

