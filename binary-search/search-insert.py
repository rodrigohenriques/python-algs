def sortedSquares(nums: list[int]) -> list[int]:
  left = 0
  right = len(nums) - 1
  result = [0] * len(nums)
  pivot = -1
  
  while (left <= right):
    leftValue = abs(nums[left])
    rightValue = abs(nums[right])
    
    if leftValue > rightValue:
      result[pivot] = pow(leftValue, 2) 
      left += 1
    else:
      result[pivot] = pow(rightValue, 2)
      right -= 1
    
    pivot -= 1
  
  return result



print(sortedSquares(nums=[-4, -2, 0, 1, 3, 5, 6]))