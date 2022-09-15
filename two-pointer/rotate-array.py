def rotate(nums: list[int], k: int) -> list[int]:
  """
  Do not return anything, modify nums in-place instead.
  """
  n = len(nums)
  k %= n
  
  start_index = count = 0
  while count < n:
      curr_idx, inital_value = start_index, nums[start_index]
      while True:
          next_idx = (curr_idx + k) % n
          nums[next_idx], inital_value = inital_value, nums[next_idx]
          curr_idx = next_idx
          count += 1
          
          if start_index == curr_idx:
              break
      start_index += 1
  
  return nums


print(rotate(nums=[1,2,3,4,5,6,7], k=3))