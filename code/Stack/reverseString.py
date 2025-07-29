'''
Given a string, write a function that uses a stack to reverse the string. The function should return the reversed string.

Examples
Example 1:

Input: "Hello, World!"
Output: "!dlroW ,olleH"
Example 2:

Input: "OpenAI"
Output: "IAnepO"
Example 3:

Input: "Stacks are fun!"
Output: "!nuf era skcatS"
'''


class Solution:
    def reverseString(self, s):
        # ToDo: Write Your Code Here.
        stack = []
        for i in s:
            stack.append(i)
        result = ''
        while stack:
            result += stack.pop()
        return result


