# The isBadVersion API is already defined for you.


def isBadVersion(version: int) -> bool:
  return version >= 4


def firstBadVersion(n: int) -> int:
    left, right = 1, n
    
    while left < right:
      mid = (left + right) // 2
      
      if isBadVersion(mid) == True:
        right = mid
      else:
        left = mid + 1

    if left == right:
        return left
    
    return -1

print(firstBadVersion(5))