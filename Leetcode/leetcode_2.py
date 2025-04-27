# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 12:14:02 2021

@author: coderzparadise
"""

import heapq

########################################################################

# Q1: max product of 3 integers
# input: int array of numbers that are + and -
# output: return an int, being the largest product produced by 3 int's
import math
def max_3_product(nums):
    max1 = max2 = max3 = -math.inf
    min1 = min2 = math.inf
    
    for i in nums:
        if i >= max1:
            max3 = max2
            max2 = max1
            max1 = i
        elif i >= max2:
            max3 = max2
            max2 = i
        elif i >= max3:
            max3 = i
        
        if i <= min1:
            min2 = min1
            min1 = i
        elif i <= min2:
            min2 = i
            
    return max(max1*max2*max3, min1*min2*max1)


# Q2: max sum of subarray
# input: 1-d array of integers both + and -
# output: return the maximum subarray sum found
def max_subarray(nums):
    result = [0]*len(nums)
    result[0] = nums[0]
    
    for i in range(1, len(nums) ):
        result[i] = max(result[i-1]+nums[i], nums[i])
    
    return max(result)



def three_sum(nums):
    result = []
    nums.sort()
    
    for i in range(len(nums) ):
        if i > 0 and nums[i] == nums[i-1]:
                continue
        
        left = i+1
        right = len(nums)-1
        
        while left < right:
            temp_sum = nums[i] + nums[left] + nums[right]
            
            if temp_sum < 0:
                left += 1
            elif temp_sum > 0:
                right -= 1
            
            else:
                result.append([nums[i], nums[left], nums[right] ])
                left += 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
                    
    return result



# Q4: best time to sell stock 1
# input: daily prices of stocks in a 1-d array of int's
# output: an integer of the max profit that could be made in 1 transaction
import math
def best_time_sell_stock_1(prices):  
    min_price = math.inf #smallest valley  
    max_profit = 0 #highest peak
    
    for p in prices:
        min_price = min(min_price, p)
        profit = p - min_price
        max_profit = max(max_profit, profit)
    
    return max_profit



# Q5: best time to sell stock 2
# input: daily prices of stocks in a 1-d array of int's
# output: an integer of the max profit that could be made in all transactions
def best_time_sell_stock_2(prices):
    profit = 0

    for i in range( 1, len(prices) ):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit


# Q6: reverse integer
# input: given integer + or -
# output: return the integer reversed unless bigger than SYS.MAXINT
import math
def reverse_int(x):
    if x < 0:
        symbol = -1
        x = -x
    else:
        symbol = 1
    
    result = 0
    
    while x:
        result = result*10 + x%10
        x = x//10
    
    if result > math.pow(2,31):
        return 0
    
    return result*symbol



# Q7: is anagram
# input: 2 strings that represent words
# output: boolean checking if word 's' is anagram of word 't'
def is_anagram(s, t):
    d = dict() 
    
    if len(s) != len(t):
        return False
    
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
            
    for char in t:
        if char in d:
            d[char] -= 1
        else:
            return False
    
    for v in d.values():
        if v != 0:
            return False
        
    return True
    
  
# Q8: is palindrome
# input: string called 's' with spaces, nums, special chars
# output: return boolean if string is palindrome
def is_palindrome(s):
    left = 0
    right = len(s)-1
    
    while left< right:
        while not s[left].isalnum() and left<right:
            left += 1
        
        while not s[right].isalnum() and left<right:
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True



# Q9: climbing stairs
# input: integer of how many stairs there are
# output: integer of how many ways to reach the top by either taking 1 or 2 steps at a time
def climbing_stairs(n):
    forward = backward = 1
    
    for i in range(n-1):
        temp = forward
        forward = forward + backward
        backward = temp
    
    return forward

    # if n== 1 or n == 2:
    #     return n
    
    # dp = [0] * (n+1)
    
    # dp[1] = 1
    # dp[2] = 2
    
    # if n <0:
    #     return
    
    # for i in range(3, n+1):
    #     dp[i] = dp[i-1] + dp[i-2]
    
    # return dp[n]



# Q10: fibonacci sequence (dp)
# input: integer 'n'
# output: the fibo number of 'n'
def fibo(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        # print(dp)
    return dp[n]


# Q11: fibonacci sequence (o1 space)
# input: integer 'n'
# output: the fibo number of 'n'
def fibo2(n):
    if n<=1:
        return n
        
    forward = 1
    backward = 0
    
    for i in range(n-1):
        temp = forward
        forward = forward + backward
        backward = temp
    
    return forward


# Q12: house robber
# input: 1-d array of integers that represent how much money each house has acording to its position
# output: integer, the maximum money that can be stolen not robing house directly next to each other
def house_robber(nums):
    l1 = len(nums)
    
    if l1 == 0:
        return 0
    elif l1 == 1:
        return nums[0]
    elif l1 == 2:
        return max(nums[0], nums[1] )
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums) ):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
    
    return max(dp )


# Q13: roman string to integer
# input: string that is written in roman
# output: integer of the roman string in numbers
def roman_to_int(string1):
    roman = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    
    result = 0
    
    for i in range(len(string1) ):
        if i+1 < len(string1) and roman[string1[i] ] < roman[string1[i+1] ]:
            result -= roman[string1[i] ]
        else:
            result += roman[string1[i] ]
    return result
        

# Q14: integer to roman numerals
# input: integer called nums
# output: string of the corresponding integer in roman numeral form
def int_to_roman(num):
    int_val = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numeral = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    
    result = ""
    i = 0
    
    while num:
        result += (num//int_val[i]) * numeral[i]
        num = num % int_val[i]
        i += 1
        
    return result


# Q15: pascal's triangle
# input: integer of the number of rows down you want to travel pascals triangle
# output: a 2-d array of integers that represent pascals triangle
def pascal_triangle(num_rows):
    result = [ [1] ]
    
    #iter thru rows (up and down)
    for i in range(num_rows - 1):
        temp = [0] + result[-1] + [0]
        row = []
        
        #iter prev row length plus one for the new item                          
        for j in range( len(result[-1]) + 1 ):
            row.append( temp[j] + temp[j+1] )
            
        result.append(row)
        
    return result


# Q16: find missing number
# input: 1-d array of int
# output: integer of the missing number in the array 0..n
def find_missing_num(nums):
    t_sum = sum(nums)
    n = len(nums)
    
    return ((n*(n+1) ) // 2) - t_sum 


# Q17: container with most water
# input: 1-d array of int's that represent the height of each mountain at that index
# output: integer of the maximum water being able to be held without spilling
def max_water_area(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        area = 0
        if height[left] <= height[right]:
            area = height[left] * (right-left)
            left += 1
        else:
            area = height[right] * (right-left)
            right -= 1
        max_area = max(max_area, area)
    
    return max_area


# Q18: set matrix zeros across col's and row's
# input: 2-d 'matrix' array of 1's and 0's
# output: None, edit 'matrix' in-place replacing the whole row and col where '0' are found
def set_zeros_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0] )
    
    zero_row = [False] * m
    zero_col = [False] * n
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_row[i] = True
                zero_col[j] = True
    
    for i in range(m):
        for j in range(n):
            if zero_row[i] or zero_col[j]:
                matrix[i][j] = 0


# Q19: longest palindrome
# input: string 's' made of char's
# output: string palindrome that is the longest palindrome found in 's'
def longest_palindrome(s):
    result = ""
    res_length = 0
    
    for i in range(len(s) ):
        #ODD LENGTH
        l = i
        r = i
        
        while l>=0 and r <len(s) and s[l] == s[r]:
            if res_length < r-l+1:
                res_length = r - l + 1
                result = s[l:r+1]
            l -= 1
            r += 1
    
        #EVEN LENGTH
        l = i
        r = i+1
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r-l+1 > res_length:
                res_length = r - l + 1
                result = s[l:r+1]
            l -= 1
            r += 1
        
    return result


# Q20: median integer of data stream
# input: 1-D array of integers called 'nums'
# output: return the median integer of the data stream
# MAX heap     -       MIN Heap
#9, 8, 4, 2    -     10, 14, 15, 17
def median_of_data_stream(nums):
    min_heap = []
    max_heap = []
    
    for i in nums:
        heapq.heappush(max_heap, -1 * i)
        
        # keeps max_heap <= min_heap
        if len(min_heap) > 0 and len(max_heap) > 0 and (-1*max_heap[0] > min_heap[0] ):
            val = -1 * heapq.heappop(max_heap)
            heapq.heappush(min_heap, val)
            
            
        if len(max_heap) > len(min_heap) + 1:
            val = -1 * heapq.heappop(max_heap )
            heapq.heappush(min_heap, val )
        
        if len(max_heap) + 1 < len(min_heap):
            val = heapq.heappop(min_heap )
            heapq.heappush( max_heap, -1 * val )
        
    
    if len(nums) % 2 == 0:
        return ((-1 * heapq.heappop(max_heap) ) + heapq.heappop(min_heap) ) / 2
    else:
        if len(max_heap) > len(min_heap):
            return -1 * max_heap[0]
        else:
            return min_heap[0]
        
        

# Q21: word search
# input: 2-d array of char's called board and a string called 'word'
# output: return boolean if word was found in board moving up,down,left,right 
def word_search(board, word):
    rows = len(board)
    cols = len(board[0] )
    path = set()
    
    def dfs_board(r, c, i):
        if i == len(word):
            return True

        if r < 0 or r >= rows or c < 0 or c >= cols or word[i] != board[r][c] or (r,c) in path:
            return False

        path.add( (r,c) )
        res = (dfs_board(r+1, c, i + 1)  or
            dfs_board(r-1, c, i + 1) or
            dfs_board(r, c-1, i + 1) or 
            dfs_board(r, c+1, i + 1) )

        path.remove( (r,c) )
        return res

    for r in range(rows):
        for c in range(cols):
            if dfs_board(r, c, 0):
                return True
    return False
    
    

# Q22: count words with 1 iterator
# input: string of char's and space's
# output: return integer of how many words found in string1
def count_words(string1):
    words = 0
    in_word = False
    
    for i in range(len(string1) ):
        if in_word == False and string1[i] != ' ':
            in_word = True
            words += 1
        
        elif in_word == True and string1[i] == ' ':
            in_word = False
            
    return words


# Q23: t9 text letter possibility combinations
# input: a string representing a number
# output: a list of string combinations made from the input representing a number
def t9_combinations(digits):
    if not digits:
        return ""
    
    d = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    
    result = []
    stack = []
    stack.append( (0, "") )
    
    while stack:
        curr_len, combo = stack.pop()
        
        if curr_len == len(digits):
            result.append(combo)
        else:
            next_digit = digits[curr_len]
            children = d[next_digit]
            for child in children:
                stack.append( (curr_len + 1, combo+child) )
    return result


# Q24: find kth largest element
# input: 1-d array of integers called nums and integer k, representing the kth largest item
# output: integer from nums array that is the kth largest item in nums
def find_k_largest(nums, k):
    h1 = []
        
    for i in nums:
        heapq.heappush(h1, i)
    
    res = heapq.nlargest(k, h1)
    
    return res[-1]


# Q25: top k frequent items
# input: 1-d array 'nums' of integers that may contain duplicates and integer k 
# output: return a list of integers of len k, that apear the most frequent in 'nums'
def top_k_frequent(nums, k):
    if len(nums) == 0:
        return []
    
    if len(nums) == 1:
        return nums[0]
    
    d = dict()
    h1 = []
    
    for num in nums:
        if num in d:
            d[num] -= 1
        else:
            d[num] = -1
    
    for key,v in d.items():
        heapq.heappush(h1, (v, key) )
    
    
    res = []
    count = 0
    
    while count < k:
        freq, item = heapq.heappop(h1)
        res.append(item)
        count += 1
    
    return res


# Q26: find peak of mountain
# input: 1-d int array called nums of heights of mounain that go in a straight line
# output: integer index of the peak of the mountain found in nums array
def find_peak(nums):
    left = 0 
    right = len(nums) - 1
    
    while left < right:
        mid = (left+right) // 2
        
        if nums[mid] > nums[mid+1]:
            right = mid
        else:
            left = mid + 1
    return left
            
            
# Q27: unique num of path
# input: integer represent rows 'm', and integer representing num of columns 'n'
# output: integer of the possible ways to reach the bottom right of game board (m x n) only moving 1 right or down
import numpy as np
def unique_paths(m, n):
    temp = np.zeros((m,n), dtype = int)+1
        
    for i in range(1, m):
        for j in range(1, n):
            temp[i][j] = temp[i-1][j] + temp[i][j-1]
    
    return temp[m-1][n-1]
        


# Q28: longest increasing subsequence
# input: 1-d array of integers called nums
# output: return integer of the max numbers of an increasing subsequence inside nums
def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, len(nums) ):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
                
    return max(dp)


# Q29: rotate image
# input: 2-d int array
# output: in-place, rotate the 2-d matrix 90 deg to the right
def rotate_image(matrix):
    n = len(matrix)
        
    cols = (len(matrix) // 2) 
    
    if len(matrix) % 2 == 0:
        rows = (len(matrix) // 2 )            
    else:
        rows = (len(matrix) // 2 ) + 1
    
    
    for i in range( rows ): #up and down
        for j in range(cols): # left and right (exclude middle)
            
            temp = matrix[i][j]  # save top left
            
            matrix[i][j] = matrix[n-1-j][i] #bottom left to top left
            
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]  #bottom right to bottom left
            
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i] #top right to bottom right
            
            matrix[j][n-1-i] = temp #temp to top right
            

# Q30: rotate array
# input: 1-d int array of numbers and k the amount to be rotated
# output: nothing, edit in-place array rotating to the right by 'k' times
def rotate_array(nums, k):
    k = k % len(nums)
    
    if len(nums) <= 1 or k == 0:
        return
    
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums) - 1)
    
    
def reverse(nums, l, r):
    
    while l < r:
        temp = nums[l]
        nums[l] = nums[r]
        nums[r] = temp
        l += 1
        r -= 1
        
   
# Q31: get right side of BST
# input: root of BST
# output: integer values at each level that would appear first if facing BST from the right side
def right_side_BST(root):
    queue = []
    res = []
    queue.append(root)
    
    while queue:
        row_len = len(queue)
        right_side = None
        
        for i in range(row_len):
            node = queue.pop(0)
            if node:
                right_side = node
                queue.append(node.left)
                queue.append(node.right)
        
        if right_side:
            res.append(right_side.val )
    return res

        
        
        
        
        

####################################

if __name__ == "__main__":
    print('start\n')
    

    print('\nend')
