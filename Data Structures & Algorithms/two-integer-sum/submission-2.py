class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            new_list = {}
            for i,n in enumerate(nums):
                diff = target - n
                if diff in new_list:
                    return [new_list[diff],i]
                new_list[n] = i            