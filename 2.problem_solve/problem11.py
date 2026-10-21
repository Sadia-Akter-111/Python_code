class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
         nums = [1, 2, 0, 4, 6, 0, 8, 0, 9, 0]

         n = len(nums)
         j = 0

         for i in range(n):
              if nums[i] != 0:
                 nums[j] = nums[i]
                 j += 1

              while j < n:
                  nums[j] = 0
                  j += 1
         return nums
print(nums)
      
        