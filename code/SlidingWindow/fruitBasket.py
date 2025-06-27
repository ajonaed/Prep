'''You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can’t skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.

Example 1:

Input: arr=['A', 'B', 'C', 'A', 'C']  
Output: 3  
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:

Input: arr = ['A', 'B', 'C', 'B', 'B', 'C']  
Output: 5  
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
Constraints:

1 <= arr.length <= 
0 <= arr[i] < arr.length
'''
import math

# Optimal Approach: O(n) time complexity and O(1) space complexity.
# We can use a sliding window approach to find the maximum number of fruits in both baskets.


class Solution:
    def findLength(self, fruits):
        max_length = 0
        # TODO: Write your code here
        fruit_bin = {}
        start = 0

        for end in range(len(fruits)):
            cur_fruit = fruits[end]
            fruit_bin[cur_fruit] = fruit_bin.get(cur_fruit, 0) + 1
            if len(fruit_bin) > 2:
                foremost = fruits[start]
                fruit_bin[foremost] -= 1
                if fruit_bin[foremost] == 0:
                    del fruit_bin[foremost]
                start += 1

            max_length = max(max_length, end - start + 1)
        return max_length

# Brute force approach: O(n^2) time complexity and O(1) space complexity.
# We can use two nested loops to find the maximum number of fruits in both baskets.
    def total_fruit(fruits):
        n = len(fruits)
        max_len = 0

        for i in range(n):
            fruit_set = set()
            for j in range(i, n):
                fruit_set.add(fruits[j])
                if len(fruit_set) > 2:
                    break
                max_len = max(max_len, j - i + 1)

        return max_len


def main():
    sol = Solution()
    print("Maximum number of fruits: "
          + str(sol.findLength(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: "
          + str(sol.findLength(['A', 'B', 'C', 'B', 'B', 'C'])))


main()

'''Similar Problems

Problem 1: Longest Substring with at most 2 distinct characters

Given a string, find the length of the longest substring in it with at most two distinct characters.

Solution: This problem is exactly similar to our parent problem.'''
