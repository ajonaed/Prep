'''
'''

'''
Time Complexity: The algorithm traverses both the ransom note and the magazine once,
making the time complexity O(n + m), where n is the length of the ransom note and m 
is the length of the magazine.

Space Complexity: The space complexity is determined by the hashmap, which in the 
worst case will have an entry for each unique character in the magazine. 
However, since the English alphabet has a fixed number of characters, 
the space complexity is O(1).'''

from collections import defaultdict

class Solution:
    def canConstructOwn(self, ransomNote: str, magazine: str) -> bool:
        # ToDo: Write Your Code Here.
        if len(magazine) < len(ransomNote):
            return False
        maza_Freq = defaultdict(int)
        for i in magazine:
            maza_Freq[i] +=  1
        
        for i in ransomNote:
            if maza_Freq[i] == 0:
                return False
            maza_Freq[i] -= 1
        
        return True
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a defaultdict to store character frequencies from the magazine
        char_count = defaultdict(int)
        
        # Populate the defaultdict with character frequencies from the magazine
        for char in magazine:
            char_count[char] += 1
        
        # Check if the ransom note can be constructed
        for char in ransomNote:
            if char_count[char] == 0:
                return False
            char_count[char] -= 1
        
        return True

    

if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct("hello", "hellworld"))  # Expected: true
    print(sol.canConstruct("notes", "stoned"))     # Expected: true
    print(sol.canConstruct("apple", "pale"))       # Expected: false
