class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2: return False
        seen_num = set()
        for num in nums:
            if num in seen_num: 
                return True
            else: 
                seen_num.add(num)
        return False
"""
nums = [1,2,3,3]
              *
seen_set = set(1,2,3)

Understand
- What is my expected return type?
- Are the values limited to the positive integers?
- Can I be given an empty nums array?
- Is this nums array sorted?
Match
- Sets
- Array traversal
Plan
1) Check the length of the nums array.
2) Create a Set for storing values that have been seen
3) Iterate through nums
    a) Check if in set -> return True
    b) Add to set
4) Return False if the loop has completed 
Implement
- A simple for-loop solves all.
- Checking a collection is helpful with the set.
Review
- Reread the prompt and remember to dry-run code before running
Evaluate
- Time: O(n) due to the single traversal through the array
- Space: O(n) due to the worst case is adding all elements to the set()
"""