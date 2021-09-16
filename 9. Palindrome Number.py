class Solution(object):
    def isPalindrome(self, x):
        
        string_x = str(x)
        print(x)
        for left_i in range(0, len(string_x) /2):
            right_i = len(string_x) - left_i - 1
            if string_x[left_i] == string_x[right_i]:
                continue 
            else:
                return False
        return True
                    