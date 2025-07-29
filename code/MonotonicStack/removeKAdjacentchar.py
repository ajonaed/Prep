'''You are given a string s and an integer k. Your task is to remove groups of 
identical, consecutive characters from the string such that each group has exactly 
k characters. The removal of groups should continue until it's no longer possible 
to make any more removals. The result should be the final version of the string 
after all possible removals have been made.

Examples

Input: s = "abbbaaca", k = 3
Output: "ca"
Explanation: First, we remove "bbb" to get "aaaca". Then, we remove "aaa" to get "ca".

Input: s = "abbaccaa", k = 3
Output: "abbaccaa"
Explanation: There are no instances of 3 adjacent characters being the same.

Input: s = "abbacccaa", k = 3
Output: "abb"
Explanation: First, we remove "ccc" to get "abbaaa". Then, we remove "aaa" to get "abb".
'''


class SolutionOwn:
    def removeDuplicatesOwn(self, s: str, k: int) -> str:
        # TODO: Write your code here
        stack = []
        tempS = ''

        for i in range(len(s)):
            while stack and stack[-1] == s[i]:
                tempS += stack.pop()
            tempS += s[i]
            if len(tempS) == k:
                tempS = ''
                continue
            for i in tempS:
                stack.append(i)
            tempS = ''

        return ''.join(stack)


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Initialize an empty stack to track characters and their counts.
        stack = []

        for c in s:
            # If the stack is not empty and the current character is the same as the top of the stack.
            if stack and stack[-1][0] == c:
                # Increment the count of the top character in the stack.
                stack[-1][1] += 1
            else:
                # Otherwise, push a new character-count pair onto the stack.
                stack.append([c, 1])

            # If the count of the top character in the stack reaches 'k'.
            if stack[-1][1] == k:
                stack.pop()  # Remove it from the stack.

        # Reconstruct the string from the characters remaining in the stack.
        return ''.join(c * n for c, n in stack)

    def removeDuplicatesOwn(self, s: str, k: int) -> str:
        # TODO: Write your code here
        stack = []
        tempS = ''

        for i in range(len(s)):
            while stack and stack[-1] == s[i]:
                tempS += stack.pop()
            tempS += s[i]
            if len(tempS) == k:
                tempS = ''
                continue
            for i in tempS:
                stack.append(i)
            tempS = ''

        return ''.join(stack)


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates("abbbaaca", 3))  # Output: "ca"
    print(solution.removeDuplicates("abbaccaa", 3))  # Output: "abbaccaa"
    print(solution.removeDuplicates("abbacccaa", 3))  # Output: "abbaa"
    print(solution.removeDuplicates("deeedbbcccbdaa", 3))  # Output: "aa"
    print(solution.removeDuplicates("aaaabbbacd", 3))  # Output: "aa"
    print(solution.removeDuplicatesOwn("deeedbbcccbdaa", 3))  # Output: "aa"
    print(solution.removeDuplicatesOwn("aaaabbbacd", 3))  # Output: "aa"
