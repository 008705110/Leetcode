class Solution(object):
    def containsDuplicate(self, nums):
        dic = {}
        for i in range(len(nums)):
            if dic.get(nums[i]) is not None:
                return True
            else:
                dic[nums[i]] = 0
        return False 
        