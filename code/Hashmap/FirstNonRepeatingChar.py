'''
Given a string, identify the position of the first character that appears 
only once in the string. If no such character exists, return -1.

Examples

Example 1:

Input: "apple"
Expected Output: 0
Justification: The first character 'a' appears only once in the string 
and is the first character.

Example 2:
Input: "abcab"
Expected Output: 2
Justification: The first character that appears only once is 'c' and 
its position is 2.

Example 3:
Input: "abab"
Expected Output: -1
Justification: There is no character in the string that appears only once.
'''

class SolutionOwn:
    def firstUniqCharOwn(self, s: str) -> int:
        # ToDo: Write Your Code Here.
        counter = {}
        for i in range(len(s)):
            counter[s[i]] = counter.get(s[i],0) + 1
        
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Create a dictionary to store the frequency of each character
        freq = {}
        
        # Traverse the string to populate the dictionary with character frequencies
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        # Traverse the string again to find the first unique character
        for i, c in enumerate(s):
            if freq[c] == 1:
                return i
        
        # If no unique character is found, return -1
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar("apple"))  # Expected: 0
    print(sol.firstUniqChar("abcab"))  # Expected: 2
    print(sol.firstUniqChar("abab"))   # Expected: -1

