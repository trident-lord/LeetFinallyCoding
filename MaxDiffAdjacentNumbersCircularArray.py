class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = 0
        n = len(nums)
        for i in range(n):
            diff = abs(nums[i] - nums[(i+1)%n])
            if diff > max_diff:
                max_diff = diff
        return max_diff 