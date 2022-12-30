# **SLIDING WINDOW: Brute Force**
A brute-force strategy is used as an attempt to process all elements without the optimization in mind

## Problem Statement
Given an array, find the average of all sub-arrays of "K" contiguous elements in it.

     Array = [ 1 , 3 , 2 , 6 , -1 , 4 , 1 , 8 , 2 ] and K=5

 Step 1: [**1 , 3 , 2 , 6 , -1** , 4 , 1 , 8 , 2] = (11 / 5) = **2.2**
 
 Step 2: [1 , **3 , 2 , 6 , -1 , 4** , 1 , 8 , 2] = **2.8**
 
 Step 3: [1 , 3 , **2 , 6 , -1 , 4 , 1** , 8 , 2] = **2.4**
 
 
    Final Output = [ 2.2 , 2.8 , 2.4 , 3.6 , 2.8 ]
    