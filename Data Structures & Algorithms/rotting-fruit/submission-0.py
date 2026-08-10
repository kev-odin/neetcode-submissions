class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time = oranges = 0
        q = collections.deque([])
        
        # Gather the initial rotten fruits and fresh fruit
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    oranges += 1
                if grid[row][col] == 2:
                    q.append((row, col))
        
        # From the initial positions expand out the rotten fruit
        while q and oranges > 0:
            for _ in range(len(q)):
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                row, col = q.popleft()
                
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    
                    if (
                        new_row in range(rows) and new_col in range(cols) 
                        and grid[new_row][new_col] == 1
                    ):
                        q.append((new_row, new_col))
                        grid[new_row][new_col] = 2
                        oranges -= 1

            time += 1
        return time if oranges == 0 else -1

"""
Understand
- Would I be given an empty array?
- Would there be a case where no fruit are rotten?
- Returning a integer value
Match
- 2D Matrix traversal
- BFS and use of a Queue
Plan
1) Gather the initial rotten fruits and fresh fruit
2) Add the rotten fruit to the queue
    - Based on the length of the queue
    - Find other fruit based off of being 1
3) Return the number of iteration needed to turn the fruit rotten
Implement
- Recall using queues for BFS
Review
- 1 hour + video
Evaluate
- Time: O(n * m) twice due to the initital traversal and the post processing
- Space: O(n * m) if all the fruit in the grid is rotten
"""