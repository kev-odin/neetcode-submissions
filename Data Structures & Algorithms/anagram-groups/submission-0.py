class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        
        for word in strs:
            key = [0] * 26
            for char in word:
                index = ord(char) - ord("a")
                key[index] += 1
            output[tuple(key)].append(word)

        return output.values()

"""
Input: 
strs = ["act","pots","tops","cat","stop","hat"]
                                           *

{a: 1, c: 1, t: 1}          : [act, cat]
{p: 1, o: 1, t: 1, s: 1}    : [pots, tops, stop]
{h: 1, a: 1, t: 1}          : [hat]

Output: 
[["hat"],["act", "cat"],["stop", "pots", "tops"]]

Understand
- What are sublists?
- Are the characters used with the strings limited to lowercase?
- Is there a limit to how many elements are in strs?
- What happens if I am given an empty list or string?
- What is the output format?
Match
- String
- Counting
Plan
1) Declare results list
2) Iterate thru the strs
    a) Create Key based on the counted occurence of the letters
    b) Append word that matches with an existing key
3) Combine values into the results list
Implement
- See if there are any mistakes with plan
Review
- A little tricky to nail the logic for this problem
Evaluate 
- Time: O(m * n) due to the traversal for creating each key per word
- Space: O(n) due to storing the keys in a HashMap
"""