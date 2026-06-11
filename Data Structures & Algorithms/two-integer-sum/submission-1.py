class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        [3, 5, 6, 4, 8]   target = 7 

        {
        mapping target-num : index
            4: 0
            2: 1
            1: 2

        }
        '''
        remainingSum = dict()
        for i in range(len(nums)):
            r_sum = target - nums[i]
            r_index = remainingSum.get(nums[i])
            if r_index is None:
                remainingSum[r_sum] = i
            else:
                return [r_index, i]

