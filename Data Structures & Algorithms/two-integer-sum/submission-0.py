class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in complement:
                return [complement[diff], idx]
            complement[num] = idx

"""
Input:
        0,1,2,3 
nums = [3,4,5,6]
target = 7

Output: 
[0,1]

Understand
- There are many ways to approach this problem
- Would I ever consider values that are negative?
- What is the minimum length of my given nums array?
- Are there ways to optimize the solution?
- What are my return values?
Match
- Array traversal
- Searching for a complement value
Plan
1) Create a complement dictionary for the values we need to achieve the target
2) Iterate through the nums array
    * dictionary keys are mapped {complement_value:index}
    a) Find the complement -> return the result as an array 
    b) Add the value to the complement dictionary
3) Since the problem is closed. The solution should be provided in the input.
Implement
- Silly mistake while reading the problem
Review
- Elapsed: 15 minutes
Evaluate
- Time: O(n) due to traversing the array a single time
- Space: O(n) due to the worst case being adding all the values to the HashMap
"""