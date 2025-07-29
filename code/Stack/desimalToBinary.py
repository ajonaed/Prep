'''
Given a positive integer n, write a function that returns its binary equivalent 
as a string. The function should not use any in-built binary conversion function.

Examples
Example 1:

Input: 2
Output: "10"
Explanation: The binary equivalent of 2 is 10.
Example 2:

Input: 7
Output: "111"
Explanation: The binary equivalent of 7 is 111.
Example 3:

Input: 18
Output: "10010"
Explanation: The binary equivalent of 18 is 10010.


Complexity Analysis
Time Complexity
Converting decimal to binary: The algorithm repeatedly divides the input number 
by 2 to get the binary digits. The number of times the division occurs is 
proportional to the number of bits in the binary representation of the number. 
For a number num, the number of iterations is O(logN), because the number of binary 
digits required to represent num is  LogN.

Stack operations: Each division operation results in a binary digit being pushed 
onto the stack, which takes constant time,O(1). Then, we pop each binary digit from 
the stack to append it to the result string, which also takes O(logN).

Therefore, the total time complexity is O(logN).

Overall time complexity: .

Space Complexity
Stack space: The stack stores each binary digit. The number of binary digits (bits) 
required to represent a number num is O(logN), so the stack will require O(logN) space.

StringBuilder: The StringBuilder is used to construct the binary representation, 
which will contain the same number of bits as the stack, i.e. O(logN),

Overall space complexity: O(logN).
'''

class SolutionOwn: 
    def decimalToBinary(self, num):
        # ToDo: Write Your Code Here.
        res = ''
        stack = []
        while num > 0:
            stack.append(num % 2)
            num //= 2
        while stack:
            res += str(stack.pop())

        return res


class Solution:
    def decimalToBinary(self, num):
        stack = []  # Create an empty stack to hold binary digits.
        while num > 0:  # Continue the loop until num becomes 0.
            stack.append(num % 2)  # Push the remainder of num divided by 2 onto the stack.
            num //= 2  # Update num by integer division (floor division) by 2.
        return ''.join(str(i) for i in reversed(stack))  # Convert the stack to a binary string.

# Test cases
sol = Solution()
print(sol.decimalToBinary(2))    # Output: "10" (Binary representation of 2)
print(sol.decimalToBinary(7))    # Output: "111" (Binary representation of 7)
print(sol.decimalToBinary(18))   # Output: "10010" (Binary representation of 18)
