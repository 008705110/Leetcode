class Solution(object):
    def maximumWealth(self, accounts):

        highest = 0
        for i in accounts:
            sum = 0
            for j in i :
                sum = sum + j
            if sum > highest:
                highest = sum
        return highest