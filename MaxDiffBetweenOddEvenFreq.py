import math
class Solution:
    def maxDifference(self, s: str) -> int:
       hash = {}
       for i in s:
        hash[i] = hash.get(i, 0) + 1
       max_odd = 0
       min_even = len(s)
       for i in hash:
        if hash[i] % 2 == 0:
            if min_even > hash[i]:
                min_even = hash[i]
        else:
            if max_odd < hash[i]:
                max_odd = hash[i]
       return max_odd - min_even