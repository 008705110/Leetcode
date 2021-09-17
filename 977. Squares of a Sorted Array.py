class Solution(object):
    def sortedSquares(self, nums):
        L = 0
        R = len(nums)-1
        result = []
        
        while L <= R:
            L2 = ((nums[L])**2)
            R2 = ((nums[R])**2)
            if L2 > R2:
                result.insert(0,L2)
                L += 1
            else:
                result.insert(0,R2)
                R -= 1
        return result
        
        