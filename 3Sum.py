class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            l, r = i + 1, n - 1
            target = -nums[i]

            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[l], nums[r]])
                    left_val = nums[l]
                    while l < r and nums[l] == left_val:
                        l += 1
                    right_val = nums[r]
                    while l < r and nums[r] == right_val:
                        r -= 1

                elif s < target:
                    l += 1
                else:
                    r -= 1

        return res
