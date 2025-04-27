# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 13:19:48 2021

@author: coderzparadise
"""
import heapq

########################################################################

# Q1: Maximum Size Subarray Sum Equals k
# input: 1-d array of int's called 'nums' and integer k
# output: integer, the longest subarray that equals to k in nums 
def max_subarray_length_k(nums, k):
    longest_subarray = 0
    prefix_sum = 0
    d = dict()
    
    for i in range(len(nums) ): 
        prefix_sum += nums[i] 

        if prefix_sum == k:
            longest_subarray = i+1 
        
        if prefix_sum - k in d:
            longest_subarray = max(longest_subarray, i - d[prefix_sum - k] ) 
        
        if prefix_sum not in d:
            d[prefix_sum] = i
    
    return longest_subarray
    


# Q2: Longest Substring with At Most K Distinct Characters
# input: string 's' of letters and integer k determing how many distinct letters we can have in dict
# output: integer of the max length substring possible with k distict letters
def longest_substring_distinct_k_letters(s, k):
    n = len(s)
    if n*k == 0:
        return 0
    
    left =  0
    d = dict()
    max_len = 1
    
    for right in range(n):
        # add all our letters to 'd'
        if s[right] in d:
            d[s[right] ] += 1
        else:
            d[s[right] ] = 1
        
        # if k letter overflow and in-bound, remove from dict to not overflow  
        while left < right and len(d) > k:
            if d[s[left] ] == 1:
                del d[s[left]]
            else:
                d[s[left] ] -= 1
            left += 1
        
        #update the max-len possible
        max_len = max(max_len, right - left + 1)
        
    return max_len
    
    

# Q3: subarray sum equals k
# input: 1-d array of int's and 'k' the integer sum goal
# output: return integer of the total amount of continious subarrays that equal to k
def subarray_sum_equal_k(nums, k):
    d = dict()
    d[0] = 1
    
    prefix_sum = 0
    count = 0
    
    for i in range(len(nums) ):
        prefix_sum += nums[i]
        
        #check if difference is in dictionary
        diff = prefix_sum - k
        if diff in d:
            count += d[diff]
            
        #Add prefix sum to dictionary
        if prefix_sum in d:
            d[prefix_sum] += 1
        else:
            d[prefix_sum] = 1
    
    print(d)
    return count

if __name__ == "__main__":
    q3 = [3,5,1,1,7,14,8]
    print( subarray_sum_equal_k(q3, 8) )
    
        


# Q4: Sliding Window Maximum
# input: 1-d array of integers and integer 'k' that is the size of the window
# output: integer array of the all the maximum int's at each combination subarray of size k
def max_sliding_window(nums, k):
    left = right = 0
    result = []
    dq = [] #indices : dq[0] large --- dq[-1] small
    
    for right in range(len(nums) ):
        #if nums[right] is greater than previous items in dq
        while dq and nums[dq[-1]] <= nums[right]:
            dq.pop(-1)
            
        dq.append(right)
        
        # if left is outside of window
        if left > dq[0]:
            dq.pop(0)
            
        #sliding window reaches length of k
        if right + 1 >= k:
            result.append(nums[dq[0]]) #append largest num
            left += 1

    return result


# Q5: Top K frequent words
# input: 1-D array of string words and integer k for the amount of top freq. words
# output: a list of the top 'k' frequent words
def top_k_frequent_words(words, k):
    d = dict()
    
    for i in words:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    h1 = []
    #store key and values into Max heap
    for key in d:
        heapq.heappush(h1, (-1 * d[key], key))
    
    result = []
    for i in range(k):
        freq, curr_word = heapq.heappop(h1)
        result.append(curr_word)
    
    return result



# Q6: is palidrome (integer)
# input: integer above zero
# output: boolean determining if integer is palidrome or not
def is_int_palindrome(x):
    if x < 0:
        return False
    if x != 0 and x % 10 == 0:
        return False
    
    
    reverted_num = 0
    while x > reverted_num:
        reverted_num = reverted_num*10 + x % 10
        x = x//10
    
    return x == reverted_num or x == reverted_num // 10



# Q7: subset sum goal
# input: given set of arr of numbers, indice of last pos of array (not length), desired goal sum
# output: subet of numbers who sum is equal to goal 
#  (Set of int, last index, goal)
def get_goal_subset(given_set, last, goal):
    if goal == 0:
        return True, []
    if goal < 0 or last < 0:
        return False, []
    
    res, returned_subset = get_goal_subset( given_set, last-1, goal - given_set[last] )
    if res:
        returned_subset.append(given_set[last])
        return True, returned_subset
    else:
        return get_goal_subset(given_set, last-1, goal)

