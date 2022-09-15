def moveZeroes(nums: list[int]) -> None:
  """
  Do not return anything, modify nums in-place instead.
  """
  n = len(nums)
  write = 0
  read = 1

  while read < n:
    if nums[write] != 0:
      write += 1
    elif nums[read] != 0:
      nums[write] = nums[read]
      write += 1
      nums[read] = 0
    read += 1  
  
  print(nums)



print(moveZeroes(nums=[1,2,0,0,7]))