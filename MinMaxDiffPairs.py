from collections import defaultdict
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        def validpair(threshold):
            index = count = 0
            while index < n-1:
                if nums[index+1] - nums[index] <= threshold:
                    count += 1
                    index += 1
                index += 1
            return count
        nums.sort()

        left = 0
        right = nums[n-1] - nums[0]
        while(left < right):
            mid = left + (right - left) // 2
            if validpair(mid) >= p:
                right = mid
            else:
                left = mid + 1
        return left