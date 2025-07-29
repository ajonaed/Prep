'''
Given an array of integers arr, return the sum of the minimum values from all 
possible contiguous subarrays within arr. Since the result can be very large, 
return the final sum modulo (10^9 + 7).

Examples
Example 1:

Input: arr = [3, 1, 2, 4, 5]
Expected Output: 30
Explanation:
The subarrays are: [3], [1], [2], [4], [5], [3,1], [1,2], [2,4], [4,5], [3,1,2], 
[1,2,4], [2,4,5], [3,1,2,4], [1, 2, 4, 5], [3, 1, 2, 4, 5].
The minimum values of these subarrays are: 3, 1, 2, 4, 5, 1, 1, 2, 4, 1, 1, 2, 1,
1, 1.
Summing these minimums: 3 + 1 + 2 + 4 + 5 + 1 + 1 + 2 + 4 + 1 + 1 +
2 + 1 + 1 + 1 = 30.
Example 2:

Input: arr = [2, 6, 5, 4]
Expected Output: 36
Explanation:
The subarrays are: [2], [6], [5], [4], [2,6], [6,5], [5,4], [2,6,5], [6,5,4],
 [2,6,5,4].
The minimum values of these subarrays are: 2, 6, 5, 4, 2, 5, 4, 2, 4, 2.
Summing these minimums: 2 + 6 + 5 + 4 + 2 + 5 + 4 + 2 + 4 + 2 = 36.
Example 3:

Input: arr = [7, 3, 8]
Expected Output: 35
Explanation:
The subarrays are: [7], [3], [8], [7,3], [3,8], [7,3,8].
The minimum values of these subarrays are: 7, 3, 8, 3, 3, 3.
Summing these minimums: 7 + 3 + 8 + 3 + 3 + 3 = 27.

Youtube: Need code: https://www.youtube.com/watch?v=aX1F2-DrBkQ&ab_channel=NeetCodeIO
'''


class Solution:
    def sumSubarrayMins(self, arr):
        MOD = 1_000_000_007
        n = len(arr)
        result = 0  # Final sum of subarray minimums
        stack = []

        # Iterate through the array plus one extra iteration for a sentinel.
        for currentIndex in range(n + 1):
            # If we reached the end, use 0 as a sentinel value; otherwise,
            # use the current element.
            # It helps to process all remaining elements in the stack.
            currentElement = 0 if currentIndex == n else arr[currentIndex]

            # Process elements in the stack while the current element is smaller
            # than the element at the top.
            # Here, we maintain monotonic increasing stack.
            while stack and arr[stack[-1]] > currentElement:
                # Pop the index whose corresponding element is greater than
                # currentElement.
                minIndex = stack.pop()
                # Determine the previous index from the stack; if the stack is
                # empty, use -1.
                previousIndex = -1 if not stack else stack[-1]

                # Calculate the number of subarrays where arr[minIndex] is the
                # minimum:
                # (minIndex - previousIndex) gives the count of subarrays ending
                # at minIndex,
                # and (currentIndex - minIndex) gives the count of subarrays
                # starting at minIndex
                # that can extend until currentIndex.
                countSubarrays = (minIndex - previousIndex) * \
                    (currentIndex - minIndex)
                print(countSubarrays, minIndex, previousIndex, currentIndex)

                # Add the contribution of arr[minIndex] for these subarrays to the result.
                result = (result + arr[minIndex] * countSubarrays % MOD) % MOD
                print('=====',result)

            # Push the current index onto the stack for further processing.
            stack.append(currentIndex)

        return result % MOD


# Example usage
solution = Solution()
arr1 = [3, 1, 2, 4, 5]
print("Example 1:", solution.sumSubarrayMins(arr1))
arr2 = [2, 6, 5, 4]
print("Example 2:", solution.sumSubarrayMins(arr2))
arr3 = [7, 3, 8]
print("Example 3:", solution.sumSubarrayMins(arr3))
