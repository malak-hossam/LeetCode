class Solution(object):
    def longestCommonPrefix(self, strs):
        new = ''
        for i in range(len(strs[0])):
            for j in strs:
                if i == len(j) or j[i] != strs[0][i]:
                    return new
            new += strs[0][i]
        return new