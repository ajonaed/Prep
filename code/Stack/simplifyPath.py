'''Given an absolute file path in a Unix-style file system, simplify it by converting 
".." to the previous directory and removing any "." or multiple slashes.
The resulting string should represent the shortest absolute path.

Example 1
Input: path = "/a//b////c/d//././/.."
Expected Output: "/a/b/c"

Explanation:
Convert multiple slashes (//) into single slashes (/).
"." refers to the current directory and is ignored.
".." moves up one directory, so "d" is removed.
The simplified path is "/a/b/c".

Example 2
Input: path = "/../"
Expected Output: "/"

Explanation:
".." moves up one directory, but we are already at the root ("/"), so nothing happens.
The final simplified path remains "/".

Example 3
Input: path = "/home//foo/"
Expected Output: "/home/foo"

Explanation:
Convert multiple slashes (//) into single slashes (/).
The final simplified path is "/home/foo".
'''


class SolutionOwn:
    def simplifyPath(self, path):
        # ToDo: Write Your Code Here.
        pathList = path.split('/')
        stack = []

        for i in pathList:
            if stack and i == '..':
                stack.pop()
            else:
                if i.isalpha():
                    stack.append(i)
        res = ''
        temp = ''
        while stack:
            k = stack.pop()
            temp = '/'+k
            res = temp + res

        return res if res else '/'

    def simplifyPathChatGPT(self, path):
        parts = path.split('/')
        stack = []

        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return '/' + '/'.join(stack)


class Solution:
    def simplifyPath(self, path):
        # Create a stack to store the simplified path components
        stack = []

        # Split the input path string using '/' as a delimiter
        for p in path.split('/'):
            if p == '..':
                # If the component is '..', pop the last component from the stack
                if stack:
                    stack.pop()
            elif p and p != '.':
                # If the component is not empty and not '.', push it onto the stack
                stack.append(p)

        # Reconstruct the simplified path by joining components from the stack
        return '/' + '/'.join(stack)


# Test cases
sol = Solution()
print(sol.simplifyPath("/a//b////c/d//././/.."))  # Expected output: "/a/b/c"
print(sol.simplifyPath("/../"))  # Expected output: "/"
print(sol.simplifyPath("/home//foo/"))  # Expected output: "/home/foo"


'''
Time Complexity
Splitting the path: The input string path is split using / as the delimiter, 
which takes  time, where N is the length of the input string path.
This creates an array of strings representing the components of the path.

Processing the components: The algorithm processes each component of the path array.
For each component, it either pushes it onto the stack, pops an element from the stack,
or skips the component if it is . or empty. Since each component is processed 
at most once, this takes  time in total.

Building the result: After processing all components, the algorithm reconstructs 
the simplified path by concatenating the elements in the stack. 
This also takes O(N) time.

Overall time complexity: O(N) , where N is the length of the input string path.

Space Complexity
Stack space: The stack stores the components of the simplified path. 
In the worst case, the stack contains all components of the path,
which requires  space.

Result string space: The result string is used to store the final result which 
also takes O(N) space, as it holds the result of the same size as the input string 
(in the worst case).

Overall space complexity: .O(N), where N is the length of the input string path.
'''
