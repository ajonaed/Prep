'''
Given a non-negative integer represented as a string num and an integer k, 
delete k digits from num to obtain the smallest possible integer. 
Return this minimum possible integer as a string.

Examples

Input: num = "1432219", k = 3
Output: "1219"
Explanation: The digits removed are 4, 3, and 2 forming the new number 
1219 which is the smallest.

Input: num = "10200", k = 1
Output: "200"
Explanation: Removing the leading 1 forms the smallest number 200.

Input: num = "1901042", k = 4
Output: "2"
Explanation: Removing 1, 9, 1, and 4 forms the number 2 which is the 
smallest possible.
'''


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # TODO: Write your code here
        stack = []

        for i in num:
            while stack and k > 0 and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        while k > 0:
            stack.pop()
            k -= 1
        result = ''.join(stack).lstrip('0')

        return result if result else '0'
         

class SolutionCourse:
    def removeKdigitsCourse(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
                
            stack.append(digit)
            
        # Truncate the remaining K digits
        stack = stack[:-k] if k > 0 else stack 
        
        # Remove any leading zeros
        return "".join(stack).lstrip("0") or "0"
if __name__ == "__main__":
    solution = Solution()
    print(solution.removeKdigits("1432219", 3)) # Output: "1219"
    print(solution.removeKdigits("10200", 1)) # Output: "200"
    print(solution.removeKdigits("1901042", 4)) # Output: "2"              
