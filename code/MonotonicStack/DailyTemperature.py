'''
Given an array of integers temperatures representing daily temperatures, 
calculate how many days you have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

Examples
Example 1
Input: temperatures = [70, 73, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
Explanation: The first day's temperature is 70 and the next day's temperature 
is 73 which is warmer. So for the first day, you only have to wait for 1 day 
to get a warmer temperature. Hence, the first element in the result array is 1. 
The same process is followed for the rest of the days.

Example 2
Input: temperatures = [73, 72, 71, 70]
Output: [0, 0, 0, 0]
Explanation: As we can see, the temperature is decreasing every day. 
So, there is no future day with a warmer temperature. 
Hence, all the elements in the result array are 0.

Example 3
Input: temperatures = [70, 71, 72, 73]
Output: [1, 1, 1, 0]
Explanation: For the first three days, the next day is warmer. 
But for the last day, there is no future day with a warmer temperature. 
Hence, the result array is [1, 1, 1, 0].
'''

class Solution:
    '''Time and Space Complexity:
        The time complexity of this algorithm is O(N), where N is the length of the temperatures array, 
        because each temperature is pushed and popped from the stack at most once. 
        The space complexity is O(N) in the worst case, where all temperatures are in decreasing order, 
        and all indices are stored in the stack.'''
    def dailyTemperatures(self, temperatures):
        # TODO: Write your code here
        stack = []
        res = [0]* len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures([70, 73, 75, 71, 69, 72, 76, 73])) # Output: [1, 1, 4, 2, 1, 1, 0, 0]
    print(solution.dailyTemperatures([73, 72, 71, 70])) # Output: [0, 0, 0, 0]
    print(solution.dailyTemperatures([70, 71, 72, 73])) # Output: [1, 1, 1, 0]