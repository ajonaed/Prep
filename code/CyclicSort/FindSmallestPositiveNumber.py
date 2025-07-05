'''
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Note: Positive numbers start from '1'.

Example 1:

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'
Example 2:

Input: [3, -2, 0, 1, 2]
Output: 4
Example 3:

Input: [3, 2, 5, 1]
Output: 4
Example 4:

Input: [33, 37, 5]
Output: 1

Constraints:

1 <= nums.length <= 
-231 <= nums[i] <= 231 - 1
'''


class SolutionOWn:
    def findNumber(self, nums):
        # TODO: Write your code here
        i, n = 0, len(nums)

        while i < n:
            # rearrange the array, 1 <= nums[i] <= n and nums[i] != nums[j]
            j = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


class Solution:
    def findNumber(self, nums):
        i, n = 0, len(nums)
        # Rearrange the elements to place each positive integer at its correct index.
        # Negative numbers and numbers greater than the array size are ignored.
        while i < n:
            j = nums[i] - 1
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  # Swap
            else:
                i += 1

        # Find the first index where the element does not match its expected positive value.
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all elements from 1 to n are present, return n + 1.
        return len(nums) + 1


def main():
    sol = Solution()
    print(sol.findNumber([-3, 1, 5, 4, 2]))  # Output: 3
    print(sol.findNumber([3, -2, 0, 1, 2]))  # Output: 4
    print(sol.findNumber([3, 2, 5, 1]))     # Output: 4
    print(sol.findNumber([33, 37, 5]))      # Output: 1


if __name__ == "__main__":
    main()
