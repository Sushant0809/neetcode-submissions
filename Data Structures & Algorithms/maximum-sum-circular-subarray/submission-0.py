class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        cur_max = 0
        max_total = nums[0]
        cur_min = 0
        min_total = nums[0]
        total_sum = 0

        for n in nums:
            cur_max = max(n, cur_max + n)
            max_total = max(max_total, cur_max)
            
            cur_min = min(n, cur_min + n)
            min_total = min(min_total, cur_min)
            
            total_sum += n

        return max(max_total, total_sum - min_total) if max_total > 0 else max_total