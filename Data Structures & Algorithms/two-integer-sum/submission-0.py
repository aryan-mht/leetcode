class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in data:
                return [data[diff], i]
            else:
                data[nums[i]] = i
        