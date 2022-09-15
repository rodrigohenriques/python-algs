def reverseString(s: str) -> str:
  """
  Do not return anything, modify s in-place instead.
  """
  left = 0
  index = 0

  while index < len(s):
    if index == " ":
      right = 0, index - 1

      while left < right:
        s[left], s[right] = s[right], s[left]
        left+=1
        right-=1

      left = index + 1
    
    index += 1

  return s


s = "Let's take LeetCode contest"

print(reverseString(s=s))