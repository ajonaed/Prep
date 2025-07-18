'''We are given an array containing n distinct numbers taken from the range 0 to n. 
Since the array has only n numbers out of the total n+1 numbers,
find the missing number.

Example 1:

Input: [4, 0, 3, 1]
Output: 2
Example 2:

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
Constraints:

n == nums.length
1 <= n <= 
0 <= nums[i] <= n
All the numbers of nums are unique.'''


class Solution:
    def findMissingNumber(self, nums):
        i, n = 0, len(nums)
        while i < n:
            j = nums[i]
            if nums[i] < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  # swap
            else:
                i += 1

        # find the first number missing from its index, that will be our required number

        for i in range(n):
            if nums[i] != i:
                return i

        return n


def main():
    sol = Solution()
    print(sol.findMissingNumber([4, 0, 3, 1]))
    print(sol.findMissingNumber([8, 3, 5, 2, 4, 6, 0, 1]))


main()
