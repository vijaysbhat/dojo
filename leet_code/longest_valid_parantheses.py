'''
Notes:

* Stack based solution more intuitive
* Think of alternatives a bit before immediately assuming a DP approach
'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ret = 0
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if (len(stack) == 0):
                    stack.append(i)
                else:
                    ret = max([ret, i - stack[-1]])
        return ret
