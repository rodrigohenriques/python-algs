def checkInclusion(s1: str, s2: str) -> bool:
  def strToCharMap(s: str) -> dict:
    chars = {}
    for c in s:
      count = chars.get(c, 0)
      chars[c] = count + 1
        
    return chars
  
  baseline = strToCharMap(s1)
  
  left, right = 0, len(s1)

  while left < right <= len(s2):
    substr = s2[left:right]
    charMap = strToCharMap(substr)
    if charMap == baseline:
      return True
    left +=1
    right +=1

  return False

  
  

print(checkInclusion("adc", "dcda"))