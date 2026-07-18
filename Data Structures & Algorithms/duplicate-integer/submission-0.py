class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = []
        for lis in nums:
            if lis not in new:
                new.append(lis)
            else:
                return True
        return False