class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_len = len(nums)
        for i in range(nums_len):
            if val in nums:
                nums.remove(val)
            else:
                break
        new_len = len(nums)
        return new_len