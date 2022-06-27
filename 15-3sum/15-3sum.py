class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        n = len(nums)
        
        nums.sort()
        
        for i in range(n-2):
            target = 0 - nums[i]
            
            j, k = i+1, n-1
            while j < k:
                if nums[j] + nums[k] == target:
                    triplet = [nums[j], nums[k], nums[i]]
                    if triplet not in result:
                        result.append(triplet)
                    j += 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -=1
        return result