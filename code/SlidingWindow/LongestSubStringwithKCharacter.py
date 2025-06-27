'''Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.

Example 1:

Input: String="araaci", K=2  
Output: 4  
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1  
Output: 2  
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3  
Output: 5  
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
Constraints:

1 <= str.length <= 5 * 104
0 <= K <= 50
'''


class Solution:
    def findLength(self, str1, k):
      # TODO: Write your code here
        max_length = 0
        charFreq = {}
        start = 0
        
        for end in range(len(str1)):
            rightChar = str1[end]
            charFreq[rightChar] = charFreq.get(rightChar, 0) + 1

            while len(charFreq) > k:
                leftChar = str1[start]
                charFreq[leftChar] -= 1
                if charFreq[leftChar] == 0:
                    del charFreq[leftChar]
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length
