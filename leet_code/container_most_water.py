class Solution(object):
    def volume(self, p, q):
        return min(p[1], q[1]) * abs(p[0]-q[0])
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        coords = [(i, h) for i, h in enumerate(height)]
        n = len(coords)
        i = 0
        j = n-1
        max_vol = 0
        while i < j:
            max_vol = max(max_vol, self.volume(coords[i], coords[j]))
            if coords[i][1] < coords[j][1]:
                i += 1
            else:
                j -= 1
        return max_vol
