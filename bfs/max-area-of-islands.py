def maxAreaOfIsland(grid: list[list[int]]) -> int:
    R = len(grid)
    C = len(grid[0])

    if R <= 0 or C <= 0:
        return 0

    maxArea = 0

    def dfs(r: int, c: int) -> int:
        if r < 0 or r >= R: return 0
        if c < 0 or c >= C: return 0
        if grid[r][c] == 0: return 0

        grid[r][c] = 0

        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

    for r in range(R):
        for c in range(C):
          if grid[r][c] == 1:
            maxArea = max(dfs(r, c), maxArea)

    return maxArea


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
    0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

print(maxAreaOfIsland(grid=grid))
