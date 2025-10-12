class Solution(object):
    def lengthOfLongestSubstring(self, s):
        lst = []
        x = 0 
        for j,i in enumerate(s):
            if i not in lst:
                lst.append(i)
            elif i in lst:
                del lst[:lst.index(i)+1]
                lst.append(i)
            if len(lst) > x:
                x = len(lst)
        return x
        