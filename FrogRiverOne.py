# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:03:06 2019

@author: cheik
"""
def solution(X, A):
    # write your code in Python 3.6
    checked = [False]*X
    time = 0
    
    for index in range(len(A)):
        if 0 < A[index] <= X and checked[A[index]-1] == False:
            time = time + 1
            checked[A[index]-1] = True
            if time == X:
                return index
    
    return -1

solution(5, [1, 3, 1, 4, 2, 3, 5, 4]) 

