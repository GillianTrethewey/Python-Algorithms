# Leetcode: array of integers (nums), integer (target), 
# return indices of the two numbers such that theyadd
# up to target
# ex. Input: nums=[2,7,11,15], target = 9
# Output: [0,1] nums[0] = 2, nums[1] = 7 so they add to 9
# 

nums = [3,5,2,-4,8,11]
target = 7
i = 0
j = 1
max = len(nums)

def twosum(nums,target):
	for i in range( 0, max-1 ):
		for j in range( 1, max ):
			if (nums[i] + nums[j] == target):
				print('nums[' , i , '] + nums[' , j , '] = ', target)

twosum(nums,target)