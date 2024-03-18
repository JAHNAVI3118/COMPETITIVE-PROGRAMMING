class Solution(object):
    def findMaxK(self, nums):
        hs = set()
        max_k = -1
        for k in nums:
            if -k in hs:
                max_k = max(max_k,abs(k))
            hs.add(k)
        return max_k
        