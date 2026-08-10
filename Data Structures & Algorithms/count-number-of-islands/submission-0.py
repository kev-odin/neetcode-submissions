class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0
        
        rows, cols = len(grid), len(grid[0])
        result = 0
        seen = set()

        def dfs(row: int, col: int):
            # Base Cases - Checking if the position is valid
            if row not in range(rows) or col not in range(cols): return
            if grid[row][col] == "0" or (row, col) in seen: return

            # Recursive case - Adding possible adjacent "1" positions
            seen.add((row, col))
            directions = [(0, 1),(0, -1),(1, 0),(-1, 0)]
            for xr, xc in directions:
                dfs(row + xr, col + xc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in seen:
                    result += 1
                    dfs(row, col)
    
        return result
        

"""
Input:
grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]

Output: 
1

Understand
- What would be the output if the input was None?
- Could there be a possibility for no islands?
- What is the input within each of the grid?
Match
- Graph problem represented as a 2D array
- DFS makes the most sense in this case
Plan
1) Iterate thru the 2D array by getting the number of rows and columns
2) Inititate a DFS when a '1' is encountered
    Recursion
        Base case:
            Return when we are out of bounds or if the position has been seen before
        Recursive case:
            Recursively call DFS for each "1" found
Implement
- Needed to remember how to iterate over a 2D array
Review
- Needed 30 minutes and a quick review of DFS
Evaluate
- Time: O(n * m) due to the size difference between row and col. Plus we process each position once.
- Space: O(n * m) due to storing all the nodes in the seen set.
"""