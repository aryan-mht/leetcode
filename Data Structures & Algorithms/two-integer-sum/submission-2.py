class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        [3,4,5,6], target = 7
        map val : index 

        '''

        mapping = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapping:
                return [mapping[diff], i]
            mapping[n] = i
        return 

