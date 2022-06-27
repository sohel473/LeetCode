class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_sum = nums[0]
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum > prev_sum:
                prev_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return prev_sum      