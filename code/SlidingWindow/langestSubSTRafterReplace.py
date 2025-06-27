'''Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: str="aabccbb", k=2  
Output: 5  
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: str="abbcb", k=1  
Output: 4  
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:

Input: str="abccde", k=1  
Output: 3  
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
Constraints:

1 <= str.length <= 
s consists of only lowercase English letters.
0 <= k <= s.length'''


class Solution:
    def findLength(self, str1, k):
        max_length = 0
        # TODO: Write your code here
        start = 0
        charFreq = {}
        maxRepeated = 0

        for end in range(len(str1)):
            rightChar = str1[end]
            charFreq[rightChar] = charFreq.get(rightChar, 0) + 1

            maxRepeated = max(maxRepeated, charFreq[rightChar])

            if (end - start + 1 - maxRepeated) > k:
                leftChar = str1[start]
                charFreq[leftChar] -= 1
                start += 1
            max_length = max(max_length, end-start+1)
        return max_length

    def characterReplacement(self, s, k):
        left = 0
        max_freq = 0
        max_len = 0
        freq = [0] * 26

        for right in range(len(s)): 
            idx = ord(s[right]) - ord('a')
            freq[idx] += 1
            max_freq = max(max_freq, freq[idx])

            while (right - left + 1) - max_freq > k:
                freq[ord(s[left]) - ord('a')] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


def main():
    sol = Solution()
    print(sol.findLength("aabccbb", 2))
    print(sol.findLength("abbcb", 1))
    print(sol.findLength("abccde", 1))


main()
