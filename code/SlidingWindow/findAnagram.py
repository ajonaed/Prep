'''Given a string and a pattern, find all anagrams of the pattern in the given string.

Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get  permutations (or anagrams) of a string having  characters. For example, here are the six anagrams of the string abc:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: str="ppqp", pattern="pq"  
Output: [1, 2]  
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:

Input: str="abbcabc", pattern="abc"  
Output: [2, 3, 4]  
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
Constraints:

1 <= s.length, p.length <= 3 * 104
str and pattern consist of lowercase English letters.
'''

from collections import Counter
import math


class Solution:

    def findStringAnagrams(self, str1, pattern):
        window_start, matched = 0, 0
        char_frequency = {}
        result_indices = []

        for char in pattern:
            char_frequency[char] = char_frequency.get(char, 0) + 1

        for window_end in range(len(str1)):
            right_char = str1[window_end]

            if right_char in char_frequency:
                char_frequency[right_char] -= 1
                if char_frequency[right_char] == 0:
                    matched += 1

            if matched == len(char_frequency):
                result_indices.append(window_start)

            if window_end >= len(pattern) - 1:
                left_char = str1[window_start]
                window_start += 1
                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched -= 1
                    char_frequency[left_char] += 1

        return result_indices


def main():
    sol = Solution()
    print(sol.findStringAnagrams("ppqp", "pq"))
    print(sol.findStringAnagrams("abbcabc", "abc"))


main()
