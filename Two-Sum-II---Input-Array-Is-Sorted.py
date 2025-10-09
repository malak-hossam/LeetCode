class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            Sum = numbers[left] + numbers[right]
            if Sum == target:
                return [left+1, right+1]
            elif Sum < target:
                left += 1
            elif Sum > target:
                right -= 1 