'''
Given a stack, sort it using only stack operations (push and pop).

You can use an additional temporary stack, but you may not copy the elements 
into any other data structure (such as an array). The values in the stack are
 to be sorted in descending order, with the largest elements on top.

Examples
1. Input: [34, 3, 31, 98, 92, 23]
   Output: [3, 23, 31, 34, 92, 98]

2. Input: [4, 3, 2, 10, 12, 1, 5, 6]
   Output: [1, 2, 3, 4, 5, 6, 10, 12]

3. Input: [20, 10, -5, -1]
   Output: [-5, -1, 10, 20]

'''


class SolutionOWN:
    def sortStack(self, stack):
        tempStack = []
        # ToDo: Write Your Code Here.
        rSt = []
        for i in range(len(stack)):
            while tempStack and tempStack[-1] > stack[i]:
                rSt.append(tempStack.pop())
            tempStack.append(stack[i])
            while rSt:
                tempStack.append(rSt.pop())

        return tempStack

    def chatGPTVersion(self, stack):
        tempStack = []

        for val in stack:
            # Move elements greater than val to a temporary holding area
            buffer = []
            while tempStack and tempStack[-1] > val:
                buffer.append(tempStack.pop())

            # Insert the current value in the correct place
            tempStack.append(val)

            # Move the elements back
            while buffer:
                tempStack.append(buffer.pop())
        return tempStack


class Solution:

    '''Time Complexity
Outer while loop: The outer loop runs until the input stack is empty. 
If the input stack has N elements, each element is popped from the input 
stack exactly once and pushed onto the temporary stack.

Inner while loop: In the worst case, the inner loop runs for each element 
that is being popped from the input stack. If the elements in the input stack 
are in descending order, every element in tmpStack needs to be popped and 
then pushed back. Thus, for each of the N elements, we may have to move 
several elements between the stacks, leading to a quadratic time complexity.

Overall time complexity: O(N^2) , where N is the number of elements in the input stack.

Space Complexity
Temporary stack: The algorithm uses an additional temporary stack, 
tmpStack, to hold the sorted elements. The space required by this stack 
is proportional to the number of elements in the input stack, O(N).

Input stack: The input stack itself uses space O(N), but since this is part of 
the input and we are not creating a new copy, it is not considered extra space.

Other variables: The algorithm uses a few extra variables (e.g., tmp), 
which take constant space, O(1).

Overall space complexity: O(N).'''

    def sortStack(self, stack):
        # Create an empty stack to store the sorted elements
        tempStack = []

        # Continue sorting until the original stack is empty
        while stack:
            # Pop the top element from the original stack
            temp = stack.pop()

            # Move elements from the temporary stack back to the original stack
            # until we find the correct position for the current element
            while tempStack and tempStack[-1] > temp:
                stack.append(tempStack.pop())

            # Place the current element in its correct sorted position in the temporary stack
            tempStack.append(temp)

        # Return the sorted stack
        return tempStack


# Example usage
sol = Solution()
stack = [34, 3, 31, 98, 92, 23]
print("Input: ", stack)
print("Sorted Output: ", sol.sortStack(stack))
