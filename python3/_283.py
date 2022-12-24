# O(n)
# compares pairs of 2 and swaps if left is 0 and right is number
# jumps every number
class Solution:
    def moveZeroes(self, nums: list) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0 and nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]

            # wait while we find a non-zero element to swap
            if nums[left] != 0:
                left += 1

                # [1 ,2 , 0 , 9 ,9 , 4, 0, 3]
                # ^  ^