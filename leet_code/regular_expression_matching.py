'''
Notes

* Dynamic programming memo data structure - use dict indexed by string location tuples
* Used top down approach here - could also have done bottom up working backwards from the ends of both strings
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        def match(i, j):
            if (i,j) not in memo:
                if j >= len(p):
                    ret = (i == len(s))
                else:
                    first_char_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
                    if j+1 < len(p) and p[j+1] == '*':
                        ret = match(i, j+2) or (first_char_match and match(i+1, j))
                    else:
                        ret = first_char_match and match(i+1,j+1)
                memo[(i,j)] = ret
            return memo[(i,j)]
        
        return match(0,0)
