def twoSum(numbers: list[int], target: int) -> list[int]:
  """
  Do not return anything, modify nums in-place instead.
  """
  n = len(numbers)
  left, right = 0, n - 1

  while left < right:
    sum = numbers[left] + numbers[right]
    if sum == target:
      return [left + 1, right + 1]
    elif sum > target:
      right -= 1
    else:
      left += 1
  
  return []



print(twoSum(nums=[1,2,0,0,7], target=9))