'''
Given a string and a pattern, find the smallest substring 
in the given string which has all the character occurrences of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"  
Output: "abdec"  
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="aabdec", Pattern="abac"  
Output: "aabdec"  
Explanation: The smallest substring having all characters occurrences of the pattern is "aabdec"
Example 3:

Input: String="abdbca", Pattern="abc"  
Output: "bca"  
Explanation: The smallest substring having all characters of the pattern is "bca".
Example 4:

Input: String="adcad", Pattern="abc"  
Output: ""  
Explanation: No substring in the given string has all characters of the pattern
Constraints:

m == String.length
n == Pattern.length
1 <= m, n <= 105
String and Pattern consist of uppercase and lowercase English letters.
'''


class Solution:
    def findSubstring(self, str1, pattern):
        start, matched = 0, 0
        strStart = 0
        minLength = float('inf')
        pMap = {}

        for i in pattern:
            pMap[i] = pMap.get(i, 0) + 1

        for end in range(len(str1)):
            rChar = str1[end]
            if rChar in pMap:
                pMap[rChar] -= 1
                if pMap[rChar] == 0:
                    matched += 1

            while matched == len(pMap):  # Fix: match against unique characters
                if minLength > end - start + 1:
                    minLength = end - start + 1
                    strStart = start

                lChar = str1[start]
                start += 1
                if lChar in pMap:
                    if pMap[lChar] == 0:
                        matched -= 1
                    pMap[lChar] += 1

        return '' if minLength > len(str1) else str1[strStart: strStart + minLength]

    def findSubstring1(self, str1, pattern):
        window_start, matched, substr_start = 0, 0, 0
        min_length = len(str1) + 1
        char_frequency = {}

        for chr in pattern:
            if chr not in char_frequency:
                char_frequency[chr] = 0
            char_frequency[chr] += 1

        # try to extend the range [window_start, window_end]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char in char_frequency:
                char_frequency[right_char] -= 1
                if char_frequency[right_char] >= 0:
                    matched += 1

            # Shrink the window if we can, finish as soon as we remove a matched character
            while matched == len(pattern):
                if min_length > window_end - window_start + 1:
                    min_length = window_end - window_start + 1
                    substr_start = window_start

                left_char = str1[window_start]
                window_start += 1
                if left_char in char_frequency:
                    # Note that we could have redundant matching characters, therefore we'll
                    # decrement the matched count only when a useful occurrence of a matched
                    # character is going out of the window
                    if char_frequency[left_char] == 0:
                        matched -= 1
                    char_frequency[left_char] += 1

        if min_length > len(str1):
            return ""
        return str1[substr_start:substr_start + min_length]
    
def main():
    sol = Solution()
    print(sol.findSubstring("aabdec", "abc"))
    print(sol.findSubstring("aabdec", "abac"))
    print(sol.findSubstring("abdbca", "abc"))
    print(sol.findSubstring("adcad", "abc"))


main()