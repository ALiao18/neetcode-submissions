class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        idx = set(nums)
        return len(idx) != len(nums)