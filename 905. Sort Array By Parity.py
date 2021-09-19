class Solution(object):
    def sortArrayByParity(self, nums):
        left = 0
        right = len(nums) - 1
        mid = 0
        
        while mid < right:
            if nums[mid] % 2 == 1:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
                
            else:
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1
                
        return nums
                