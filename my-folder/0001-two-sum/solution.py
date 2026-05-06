class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map: dict = {}
        for i, n in enumerate(nums):
            difference = target - nums[i]
            if difference in num_map:
                return[num_map[difference], i]
            num_map[n] = i
        return []

