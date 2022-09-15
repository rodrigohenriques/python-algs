def lengthOfLongestSubstring(s: str) -> int:
  left, right = 0, 0
  chars = {}
  longest = 0

  while right < len(s):
    charAtRight = s[right]

    if charAtRight in chars:
      longest = max(len(chars), longest)
      
      while left <= right and s[left] != charAtRight:
        chars.pop(s[left])
        left += 1
      
      left += 1
      
    chars[charAtRight] = 1
    right += 1
  
  return max(longest, len(chars))


print(lengthOfLongestSubstring("abcabcbb"))
