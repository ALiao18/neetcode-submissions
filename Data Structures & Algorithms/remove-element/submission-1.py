class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_len = len(nums)
        while val in nums:
            nums.remove(val)
        new_len = len(nums)
        return new_len