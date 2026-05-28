# List - the array of PYTHON

nums = [3, 1, 4, 1, 5, 9, 2, 6]

# Accessing elements - 0(1)
print(nums[0])       # 3 -> first element
print(nums[-1])      # 6 -> last element  (negative index counts from end)
print(nums[-2])      # 2 -> second from last 

# Slicing - creates a new list - 0(k) where k is slice size
print(nums[1:4])     # [1, 4, 1] -> index 1 upto (not including) 4
print(nums[:3])      # [3, 1, 4] -> from start to index 3 (not including)
print(nums[5:])      # [9, 2, 6] -> from index 5 to end
print(nums[::-1])    # [6, 2, 9, 5, 1, 4, 1, 3] -> reversed!

# Modifying
nums.append(7)       # add to end        -- 0(1)
nums.insert(0, 99)   # insert at index 0  --  0(n)  <- expensive, shifts everything
nums.pop()           # removes last      --  0(1)
nums.pop(0)          # removes index 0    -- 0(n)   <- expensive too
nums.remove(4)       # removes first occurance of value 4 -- 0(n)

# Useful operations
print(len(nums))     # Length of list
print(3 in nums)     # True - check membership 0(n)
nums.sort()          # sort in-place — O(n log n)
nums.reverse()       # reverse in-place — O(n)
sorted_copy = sorted(nums)     # returns a new sorted list — O(n log n)
