class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:       
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        seen = set()

        def dfs(row: int, col: int):
            # Base cases: not in range OR seen OR value == 0
            if row not in range(rows) or col not in range(cols): 
                return 0
            if (row, col) in seen or grid[row][col] == 0: 
                return 0

            # Recursive cases: check the adjacent values
            seen.add((row, col))
            area = 1
            directions = [(1, 0),(-1, 0),(0, 1),(0, -1)]
            for xr, xc in directions:    
                area += dfs(row + xr, col + xc)
            return area
        
        result = 0
        for row in range(rows):
            for col in range(cols):
                result = max(result, dfs(row, col)) 

        return result

"""
Understand
- What is going to happen if I am given an empty array?
- Based on the input data, are all the values within the inner arrays integer values?
- How can I simplify my solution with recursion?
    Base case
    Recursive case

Matching
- Iterate through the entire grid, 2d array traversal
- DFS to find the adjacent 1 values that have not been previously seen
- Compare with a previous value

Plan
1) Iterate through the grid array
2) Call recursive DFS when a 1 is encountered
    a) Base case - return 0
        - Out of range, not a 1, seen before
    b) Recursive case - return 1
        - Check adjacent positions to the current node
        - Add and compare area when the function calls
3) Return the area value that is compared with prior area evaluations

Implement
- Trouble with writing the logic for when to return the count

Review
- Elapsed: 30 minutes
- A fun problem for getting into the groove of writing DFS

Evaluate
- Time: O(n * m) due to varying length of the array, each node is seen once
- Space: O(n * m) due to storing every element in the visited set
"""