class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # pattern: when doing binary search type of operations use variables to
        #   * store the length of the subarrays
        #   * calculate 1 indexed locations of elements within the subarrays
        #   * subtract 1 to get actual index location
        # makes it much easier to reason about edge cases and stopping conditions
        # rather than manipulating the zero indexed element locations
        if len(A) > len(B):
            return self.findMedianSortedArrays(B, A)
        m = len(A)
        n = len(B)
        
        imin = 0
        imax = m
        
        while imin <= imax:
            i = (imin + imax)/2
            j = (m + n + 1)/2 - i
            # handling edge cases
            if i < m and B[j-1] > A[i]:
                imin = i + 1
            elif i > 0 and B[j] < A[i-1]:
                imax = i - 1
            else:
                if i == 0:
                    left_max = B[j-1]
                elif j == 0:
                    left_max = A[i-1]
                else:
                    left_max = max(A[i-1], B[j-1])
                if (m+n) % 2 == 1:
                    return left_max
                
                if i == m:
                    right_min = B[j]
                elif j == n:
                    right_min = A[i]
                else:
                    right_min = min(A[i], B[j])
                    
                return (left_min + right_min) / 2.0
