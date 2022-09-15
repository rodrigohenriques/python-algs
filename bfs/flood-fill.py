
def floodFill(image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
  R = len(image)
  C = len(image[0])

  colorToFill = image[sr][sc]
  
  if (colorToFill == newColor): return image

  def paint(r: int, c: int):
      if image[r][c] == colorToFill:
        image[r][c] = newColor
        if r >= 1: paint(r - 1, c)
        if r + 1 < R: paint(r + 1, c)
        if c >= 1: paint(r, c - 1)
        if c + 1 < C: paint(r, c + 1)
  
  paint(sr, sc)

  return image

print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
    


