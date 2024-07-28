class Solution(object):
    def twoSum(self, nums, target):
        previous = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in previous:
                return(previous[diff],i)
            previous[n] = i 
            