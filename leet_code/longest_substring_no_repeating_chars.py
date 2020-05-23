class Solution(object):    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_substr_len = 0
        if len(s) <= 1:
            return len(s)
        
        max_substr_len = 0        
        char_dict = {}
        i = 0
        j = 0
        substr_len = 0
        n = len(s)
        while i < n and j < n:
            if s[j] not in char_dict.keys():
                char_dict[s[j]] = 1
                j += 1
                max_substr_len = max([max_substr_len, j - i])
            else:
                del char_dict[s[i]]
                i += 1
                    
        return max_substr_len
