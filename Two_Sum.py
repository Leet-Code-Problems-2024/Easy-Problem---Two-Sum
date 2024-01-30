class Solution(object):
    def twoSum(self, nums, target):
        
        index = list() #create list for return type
        
        for j in range(0,len(nums)-1): #one counter for first pass over numbers
            for i in range(j + 1,len(nums)): #second counter for rest of numbers
                if(nums[i] + nums[j] == target):
                    index1 = j
