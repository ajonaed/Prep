'''Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters, it will have n! permutations.

Example 1:

Input: str="oidbcaf", pattern="abc"   
Output: true   
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:

Input: str="odicf", pattern="dc"   
Output: false  
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:

Input: str="bcdxabcdy", pattern="bcdyabcdx"  
Output: true  
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:

Input: str="aaacb", pattern="abc"  
Output: true  
Explanation: The string contains "acb" which is a permutation of the given pattern.'''

from collections import Counter


class Solution:

    def contains_permutation(self, s, pattern):
        if len(pattern) > len(s):
            return False

        # frequency of characters in the pattern
        pattern_freq = Counter(pattern)
        window_freq = Counter()  # frequency of characters in the current window

        for i in range(len(pattern)):  # fill the first window
            # add one character from the right side of the window
            window_freq[s[i]] += 1

            if i >= len(pattern):  # remove one character from the left side of the window
                # when the window size is bigger than the pattern
                if window_freq[s[i - len(pattern)]] == 1:
                    del window_freq[s[i - len(pattern)]]
                else:  # decrement the frequency of the character going out of the window
                    window_freq[s[i - len(pattern)]] -= 1

            if window_freq == pattern_freq:
                return True

        return False

    def findPermutation(self, str1, pattern):
        window_start, matched = 0, 0
        char_frequency = {}

        for chr in pattern:  # Same as Counter(pattern)
            if chr not in char_frequency:
                char_frequency[chr] = 0
            char_frequency[chr] += 1

        # our goal is to match all the characters from the 'char_frequency' with the current
        # window try to extend the range [window_start, window_end]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            # if current character is not part of 'char_frequency' we can skip this character
            if right_char in char_frequency:
                # decrement the frequency of matched character
                char_frequency[right_char] -= 1
                if char_frequency[right_char] == 0:
                    matched += 1
            
            if matched == len(char_frequency):
                return True

            # shrink the window by one character
            if window_end >= len(pattern) - 1:
                left_char = str1[window_start]
                window_start += 1
                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched -= 1
                    char_frequency[left_char] += 1

        return False


def main():
    sol = Solution()
    # print('Permutation exist: ' + str(sol.findPermutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(sol.findPermutation("odicf", "dc")))
    # print('Permutation exist: ' +
    #   str(sol.findPermutation("bcdxabcdy", "bcdyabcdx")))
    # print('Permutation exist: ' + str(sol.findPermutation("aaacb", "abc")))


main()
