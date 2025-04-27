# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 12:07:10 2021

@author: coderzparadise
"""

########################################################################

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



# Q3: remove element
# input: given array of integers and key_item to remove
# output: return int of length of new list w/o key_item's
def remove_element(nums, key):
    left = 0
    right = len(nums)-1
    
    while left <= right:
        if nums[left] == key:
            nums[left] = nums[right]
            right -= 1
        else:
            left += 1
    return nums[:left]

    # Linear Time
    # left = 0
    # for i in range(len(nums) ):
    #     if nums[i] != key:
    #         nums[left] = nums[i]
    #         left += 1
    # return nums[:left]


# Q4: two sum
# inputs: array of int's and target int
# output: return index of items from array that sum to target
def two_sum(nums, target):
    d = dict()

    for i in range(len(nums) ):
        remain = target - nums[i]
        if remain in d:
            return d[remain], i
        else:
            d[nums[i] ] = i
            
            

# Q5: longest_substring_no_duplicates
# input: string
# output: integer; length of longest non duplicated chars in string
def longest_substring_no_dup(string1):
    s = set()
    left = 0
    result = 0
    
    for right in range(len(string1) ):
        while string1[right] in s:
            s.remove(string1[left] )
            left += 1
        s.add(string1[right])
        result = max(result, right-left + 1)
    return result


# Q6: longest prefix
# input: 1-D array of words in a list
# output: string; longest prefix word
import math

def longest_prefix(words):
    shortest_word = math.inf
    
    for w in words:
        shortest_word = min(len(w), shortest_word)
    
    
    result = ''
    for i in range(shortest_word):
        temp = words[0][i]
        
        for j in range(1, len(words) ):
            if temp != words[j][i]:
                return result
        result += temp
    return result


# Q7: group anagrams
# input: 1-D array of strings
# output: 2-D array of all anagrams grouped together correlated to each word/characters
def group_anagrams(words):
    d = dict()
    
    for word in words:
        ordered_word = ''.join(sorted(word) )
        if ordered_word in d:
            d[ordered_word] += word
        else:
            d[ordered_word] = word
    return d.values()


# Q8: valid parenthesis
# input: a string of brackets
# output: Boolean testing if string1 passed as parameter has valid parenthesis
def valid_parenthesis(string1):
    opened = ['(', '[', '{']
    closed = [')', ']', '}']
    stack = []
    
    for c in string1:
        if c in opened:
            stack.append(c)
        else:
            if stack and stack[-1] == opened[closed.index(c) ]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False


# Q9: search rotated array
# input: array sorted than can be rotated left or right, and a target integer
# output: Boolean to see if target is inside the rotated array
def search_rotated_array(nums, target):
    if len(nums) == 0:
        return
    
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        
        if nums[mid] == target:
            return True
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False


# PRACTICE !!
# Q10: sqrt
# input: integer x
# output: find the number that is the sqrt or closest sqrt of integer
def sqrt(x):
    left = 0 
    right = x
    
    while left <= right:
        mid = (right + left) // 2
        
        if mid*mid <= x < (mid+1)*(mid+1):
            return mid
        
        elif mid*mid > x:
            right = mid - 1
        
        elif mid*mid < x:
            left = mid + 1
            
            

# Q11: polish notation
# input: 1-D array of int's and operation symbols
# output: return the polish notation of the given expression
def polish_notation(expression):
    stack = []
    
    for c in expression:
        
        if c not in "*-+/":
            stack.append(int(c) )
        else:
            right = stack.pop()
            left = stack.pop()
            
            if c == "+":
                stack.append(left+right)
            elif c == "-":
                stack.append(left-right)
            elif c == "*":
                stack.append(left*right)
            elif c == "/":
                stack.append(int(left//right) )
                
    return stack.pop()

#Q12: two sum - sorted
# input: given a nums array sorted and a given target int
# output: return index of nums in array that equal to target result
def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        if nums[left] + nums[right] == target:
            return left,right
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
            
# Q13: number of islands
# input: given a 2-D array of 1's and 0's that represent land - 1 and water - 0
# output: return the total number of islands where horizontal and vertical is islands
def number_of_islands(island):
    if not island:
        return 
    
    count = 0
    for i in range( len(island) ):
        for j in range( len(island[0]) ):
            if island[i][j] == 1:
                dfs_islands(island, i, j)
                count += 1
    return count

def dfs_islands(nums, i, j):
    if i < 0 or i >= len(nums) or j < 0 or j >= len(nums[0] ) or nums[i][j] != 1 :
        return
    
    nums[i][j] = 2
    dfs_islands(nums, i-1, j)
    dfs_islands(nums, i+1, j)
    dfs_islands(nums, i, j-1)
    dfs_islands(nums, i, j+1)
    
    
# Q14: contains duplicates
# input: given an array of numbers
# output: return boolean if contains duplicate or not
def contain_duplicates(nums):
    s = set()
    for i in nums:
        if i in s:
            return True
        else:
            s.add(i)
    return False
    

# Q15: move zeros
# input: given an array of numbers
# output: move all zeros to the end and edit nums array in place
def move_zeros(nums):
    left_index = 0
    zeros = 0
    
    for i in range(len(nums) ):
        if nums[i] == 0:
            zeros += 1
        else:
            nums[left_index] = nums[i]
            left_index += 1
    
    for j in range(zeros):
        nums[-j-1] = 0
        
        

# Q16: reverse string
# input: 1-D array of letters in a list
# output: reverse all letters in array inplace
def reverse_string(string1):
    if len(string1) <= 1:
        return
    
    right = len(string1)-1
    left = 0
    
    while left < len(string1) // 2:
        temp = string1[left]
        string1[left] = string1[right]
        string1[right] = temp
        right -= 1
        left += 1
    
# Q17: intersection of arrays
# input: (2) 1-D arrays of integers
# output: list of intersecting nums from list1 and list2
def intersection_of_arr(list1, list2):
    s1 = set(list1)
    result = []
    for i in list2:
        if i in s1:
            result.append(i)
            s1.remove(i)
    return result


# Q18: binary search
# input: 1-D array of integers and target goal
# output: boolean if found target within n
def binary_search(nums, target):
    left = 0
    right = len(nums)-1
    
    while left <= right:
        mid = (left + right) // 2
        print( nums[mid] )
        
        if nums[mid] == target:
            return True
        
        elif nums[mid] < target:
            left = mid + 1
        
        elif nums[mid] > target:
            right = mid - 1
            
    return False
    

# Q19: first unique char
# input: given string1 of letters
# output: return int index of first non-repeating char
def first_unique_char(string1):
    d = dict()
    
    for c in string1:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    for k,v in d.items():
        if v == 1:
            return string1.index(k)
    

# Q20: decode string
# input: recieved a string of nums and letters and brackets [,]
# output: return string of decoded string
def decode_string(string1):
    curr_string = ''
    curr_num = 0
    stack = []
    
    for c in string1:
        if c == '[':
            stack.append(curr_string)
            stack.append(curr_num)
            curr_string = ''
            curr_num = 0
        
        elif c == ']':
            prev_num = stack.pop()
            prev_string = stack.pop()
            curr_string = prev_string + prev_num * curr_string
        
        elif c.is_digit():
            curr_num = int(c)
            # curr_num = (prev_num*10) + int(c)
            
        else:
            curr_string += c
            
    return curr_string
            

# #Q21: max consecutive one's
# input: 1-D array of 1's and 0's 
# output: integer of the highest amount of consecutive one's
def max_consecutive_ones(nums):
    consec = 0
    longest = 0
    for i in nums:
        if i == 1:
            consec += 1
        else:
            consec = 0
        longest = max(longest, consec)
    return longest


# Q22: find pivot
# input: takes in 1-D array of int's
# output: return int index that has the right and left side of pivot index equal each other
def find_pivot_index(nums):
    tsum = sum(nums)
    left_side = 0
    
    for i in range(len(nums) ):
        if left_side == tsum - left_side - nums[i]:
            return i
        left_side += nums[i]
    return -1


# Q23: how many days until a hotter day
# input: 1-D array of integers of tempertures
# output: array that shows the days until a hotter days appears corelating to temperature index
def daily_temperture(temperture):
    stack = []
    result = [0] * len(temperture)
    
    for i in range(len(temperture) ):
        while stack and temperture[i] > temperture[stack[-1] ]:
            curr_index = stack.pop()
            result[curr_index] = i - curr_index
        stack.append(i)
        
    return result      

      

# Q24: largest number that is at least double than all others
# input: 1-D array of integers greater than zero
# output: return the index of item that is 2x as big as any other integer
def dominant_index(nums):
    index = 0
    first = -math.inf
    second = -math.inf
    
    for i in range(len(nums) ):
        if nums[i] > first:
            second = first
            first = nums[i]
            index = i
        
        elif nums[i] > second:
            second = nums[i]
            
    if first >= second * 2:
        return index
    
    return -1


# Q25: jewels and stones
# input: string called jewels that contain char jewels and string called stones made of char's
# output: return integer of how many stones match the type of jewels
def jewels_stones(jewels, stones):
    s = set()
    for i in jewels:
        if i not in s:
            s.add(i)
    
    counter = 0
    for j in range(stones):
        if stones[j] in s:
            counter += 1
            
    return counter


# Q26: keys and rooms
# input: 2-D array where each bucket is the room and each bucket has room keys
# output: return boolean if you come across each key from previous rooms/buckets visited
# description: you automatically get the room key 0.
def keys_and_rooms(rooms):
    stack = []
    visited = set()
    stack.append(0)
    
    while stack:
        curr_room = stack.pop()
        visited.append(curr_room)
        
        for i in rooms[curr_room]:
            if i not in visited:
                stack.append(i)
                
    return len(rooms) == len(visited)


# Q27: squares of sorted array
# input: a sorted array of neg. and pos. integers 
# output: return a 1-D array of sorted integers that are the squares of the input array
# example: nums = [-8, -3, 0, 5, 10, 12]
def sorted_squares(nums):
    left = 0
    right = len(nums) - 1
    result = [0] * len(nums)
    index = right
    
    while left <= right:
        if abs(nums[left] ) > abs(nums[right] ):
            result[index] = nums[left]*nums[left]
            left += 1
        else:
            result[index] = nums[right]*nums[right]
            right -= 1
        
        index -= 1
    
    # result[index] = nums[left]*nums[left]
    return result


# Q28: find numbers with even number integers
# input: 1-D array of integers
# output: return how many integers have even amount of integers ex.) 23, 4125, 689030
def count_even_integers(nums):
    result = 0
    
    for i in nums:
        temp = 0
        while i > 0:
            i = i // 10            
            temp += 1
        
        if temp % 2 == 0:
            result += 1
            
    return result

# Q29: check if double int exists
# input: array of integers
# output: return boolean to see if there's an integer that is double than another integer in nums
def check_if_double_exist(nums):
    s = set()
    
    for i in nums:
        if i*2 in s or (i%2 == 0 and i // 2 in s):
            return True
        s.add(i)
    return False




if __name__ == "__main__":
    print('start\n')
    
    # q13 = [[0,0,1,0,0], [0,1,1,0,0], [1,0,0,0,0], [0,0,1,1,1], [0,0,0,0,0] ]
    # print(number_of_islands(q13) )
    
    
    # q16 = ['t', 'h', 'e', 'C', 'a', 't']
    # reverse_string(q16)
    # print(q16)
    
    
        
                      
                
    
    