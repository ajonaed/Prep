'''
Given an array, print the Next Greater Element (NGE) for every element.

The Next Greater Element for an element x is the first greater element on 
the right side of x in the array.

Elements for which no greater element exist, consider the next greater element as -1.
'''


class Solution:
    def nextLargerElement(self, arr):
        res = [-1]*len(arr)
        # ToDo: Write Your Code Here.
        s = []
        for i in range(len(arr)-1, -1, -1):
            while s and s[-1] <= arr[i]:
                s.pop()
            if s:
                res[i] = s[-1]
            s.append(arr[i])
        return res

    def nextLargerElement1(self, arr):
        # Initialize an empty stack and a result list with -1 values
        s = []
        res = [-1] * len(arr)

        # Iterate through the array in reverse order
        for i in range(len(arr) - 1, -1, -1):
            # While the stack is not empty and the top element of the stack is less than or equal to the current element
            while s and s[-1] <= arr[i]:
                s.pop()  # Pop elements from the stack until the condition is met
            
            if s: 
                res[i] = s[-1]  # If the stack is not empty, set the result for the current element to the top element of the stack
            s.append(arr[i])  # Push the current element onto the stack

        return res

    

sol = Solution()
print(sol.nextLargerElement([4, 5, 2, 25]))  # Example usage
print(sol.nextLargerElement([13, 7, 6, 12]))  # Example usage
print(sol.nextLargerElement([1, 2, 3, 4, 5]))  # Example usage

