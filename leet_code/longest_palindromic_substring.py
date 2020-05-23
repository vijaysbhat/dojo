'''
Notes:

* Use while loop instead of for loop since it is better for explicitly controlling boundary condition
* Check whether counter is being incremented in while loop
* Check whether if statements with multiple clauses have all condition combinations are being handled explicitly, otherwise can cause unpredictable behavior
* Python substring operator is exclusive of second operand
* Loop termination boundary condition - write out equation for constraints with all relevant variables and rearrange
* Dynamic programming - bottom up approach is easier to reason about and place correctness guarantees on
'''

class Solution(object):
    def is_palindrome(self, s, memo, i, j):
        if i == j:
            memo[(i,j)] = True
            return True
        if j == i + 1:
            if s[i] == s[j]:
                memo[(i,j)] = True
                return True
            else:
                memo[(i,j)] = False
                return False
        
        if memo[(i+1, j-1)] == True and s[i] == s[j]:
            memo[(i,j)] = True
            return True
        memo[(i,j)] = False
        return False
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        memo = {}
        n = len(s)
        l = 1
        i = 0
        max_len = 0
        max_str = ''
        while l <= n:
            i = 0
            while i < n - l + 1:
                if self.is_palindrome(s, memo, i, i+l-1) and max_len < l:
                    max_str = s[i:i+l]
                i += 1
            l += 1
        return max_str
