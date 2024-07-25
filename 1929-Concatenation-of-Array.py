class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        c = 1
        for i in nums*2:
            ans.append(i)
            c+=1
        return ans
                
        