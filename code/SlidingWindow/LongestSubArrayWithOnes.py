'''Given an array containing 0s and 1s, if you are allowed to replace no more than 
‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2  
Output: 6  
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3  
Output: 9  
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
Example 3:

Input: Array=[1, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: By flipping 0 at the second and fifth index in the list, we get [1, 0, 1, 1, 1, 1, 1, 1], which has 6 consecutive 1s.
Constraints:

1 <= arr.length <= 
arr[i] is either 0 or 1.
0 <= k <= nums.length
'''


class Solution:
    def findLength(self, arr, k):
        max_length = 0
        start = 0
        OnesCount = 0

        for end in range(len(arr)):
            if arr[end] == 1:
                OnesCount += 1

            if end - start + 1 - OnesCount > k:
                # update OnesCount,
                if arr[start] == 1:
                    OnesCount -= 1
                start += 1
            max_length = max(max_length, end - start + 1)

        # TODO: Write your code here
        return max_length

    def longest_ones(self, arr, k):
        left = 0
        max_length = 0
        zero_count = 0

        for right in range(len(arr)):
            if arr[right] == 0:
                zero_count += 1

            while zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


def main():
    sol = Solution()
    print(sol.findLength([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(sol.findLength([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
