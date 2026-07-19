class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = set()
        for x in nums:
            if x in new:
                pass
            new.add(x)
        unique = set(nums)
        if len(unique) < len(nums):
            return True
        return False