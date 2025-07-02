'''We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
 The array originally contained all the numbers from 1 to ‘n’, but due to a data error, 
 one of the numbers got duplicated which also resulted in one number going missing. 
 Find both these numbers.

Example 1:

Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.
Example 2:

Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.'''


class Solution:
    def findNumbers(self, nums):
        # TODO: Write your code here
        # the array
        i = 0
        n = len(nums)
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i+1]

        return [-1, -1]


def main():
    sol = Solution()
    print(sol.findNumbers([3, 1, 2, 5, 2]))
    print(sol.findNumbers([3, 1, 2, 3, 6, 4]))


if __name__ == "__main__":
    main()
