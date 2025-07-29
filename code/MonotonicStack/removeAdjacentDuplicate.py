'''You are given a string s consisting of lowercase English letters. 
A duplicate removal consists of choosing two adjacent and equal letters and 
removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.'''


class Solution:
    def removeDuplicates(self, s: str) -> str:
        # Initialize stack
        stack = []
        
        # Process each character in s
        for c in s:
            # If the stack is not empty and the current character is the same as the top of the stack, pop the character from the stack
            if stack and c == stack[-1]:
                stack.pop()
            else: # Push the current character onto the stack
                stack.append(c)
        
        # Join the stack to a string
        return ''.join(stack)
    
    '''Time and Space Complexity:
        The time complexity of this algorithm is O(N), where N is the length of s, 
        because we perform one operation per character in s. The space complexity 
        is also O(N),
        as in the worst case, every character in s is pushed onto the stack.'''

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates("abccba")) # Output: ""
    print(solution.removeDuplicates("foobar")) # Output: "fbar"
    print(solution.removeDuplicates("abcd")) # Output: "abcd"

