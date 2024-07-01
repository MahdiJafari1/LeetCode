class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_unique = 1
        
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[last_unique] = nums[i]
                last_unique += 1
        return last_unique