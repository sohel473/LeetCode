class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = dict()
        
        for i, n in enumerate(nums):
            m = target - n
            if m in found:
                return [i, found[m]]
            found[n] = i