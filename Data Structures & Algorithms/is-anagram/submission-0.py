class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        counter = {}
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        
        for char in t:
            if char in counter and counter[char] > 0:
                counter[char] -= 1
            else:
                return False
        
        return True
"""
counter = {
r: 2
a: 2
c: 2
e: 1
}
           *
s = "racecar"
     *
t = "carrace"

Understand
- Do anagrams need to use all the given characters?
- Would I be given an empty string for an input?
- What time and space requirements would I need to consider?
Match
- String/Array traversal
- Counts
Plan
1) Create a counter dictionary
2) Iterate through the first string to gather the counted occurences of characters
3) Iterate through the second string to compare counted values, deduct until count is 0
Implement
- A simple idea that can be used in other problems
Review
- Elapsed: 20 minutes
Evaluate
- Time: O(n) due to a single traversal through both strings
- Space: O(1) due to using a counter that has limited keys
"""