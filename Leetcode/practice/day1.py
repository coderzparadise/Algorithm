# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 09:33:40 2021

@author: coderzparadise

Fastest time to implement code and explain:
    -X minutes
"""

# Q1: single number
# input: array of integers with all nums having a duplicate except 1
# output: the single number in array that has no duplicates
def single_num(nums):
    s = set()
    for i in nums:
        if i in s:
            s.remove(i)
        else:
            s.add(i)
    return s.pop()




# Q2: remove duplicates from sorted array
# input: array of int's Sorted w/ or w/o duplicates
# output: int of length of array w/o duplicates or list of array w/o duplicates
def remove_duplicates(nums):
    left = 1
    
    for right in range(len(nums)-1 ):
        if nums[right] != nums[right+1]:
            nums[left] = nums[right+1]
            left += 1
    return nums[:left]

# Q3:
#input:
#output:
