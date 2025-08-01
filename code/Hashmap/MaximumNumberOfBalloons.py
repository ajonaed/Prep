'''
Given a string, determine the maximum number of times the word "balloon" 
can be formed using the characters from the string. Each character in the
 string can be used only once.

Examples:

Example 1:

Input: "balloonballoon"
Expected Output: 2
Justification: The word "balloon" can be formed twice from the given string.
Example 2:

Input: "bbaall"
Expected Output: 0
Justification: The word "balloon" cannot be formed from the given string 
as we are missing the character 'o' twice.
Example 3:

Input: "balloonballoooon"
Expected Output: 2
Justification: The word "balloon" can be formed twice, even though there 
are extra 'o' characters.
'''


from collections import defaultdict


class Solution:
    # Time Complexity: O(n), where n is the length of the input string.
    # Space Complexity: O(1), since the character set is fixed and small.m89797
    def maxNumberOfBalloons(self, text):
        # Create a defaultdict to store character frequencies
        char_count = defaultdict(int)

        # Populate the defaultdict with character frequencies from the string
        for char in text:
            char_count[char] += 1

        min_count = float('inf')
        # Calculate the maximum number of times "balloon" can be formed
        min_count = min(min_count, char_count['b'])
        min_count = min(min_count, char_count['a'])
        min_count = min(min_count, char_count['l'] // 2)
        min_count = min(min_count, char_count['o'] // 2)
        min_count = min(min_count, char_count['n'])

        return min_count

    def maxNumberOfBalloonsOwn(self, text: str) -> int:
        min_count = float('inf')
        # ToDo: Write Your Code Here.
        char_count = defaultdict(int)

        for c in text:
            char_count[c] += 1

        # Calculate the maximum number of times "balloon" can be formed
        for i in 'balon':
            if i != 'l' and i != 'o':
                min_count = min(min_count, char_count[i])
            else:
                min_count = min(min_count, char_count[i]//2)

        return min_count  # type: ignore

    '''Time Complexity:
    Iterating through the string: We iterate through the entire string 
    once to count the frequency of each character. This operation takes 
    (O(n)) time, where (n) is the length of the string.

    Iterating through the hashmap: After counting the frequencies, 
    we iterate through the hashmap to determine how many characters 
    can be used to form the palindrome. In the worst case, 
    this would be (O(26)) for the English alphabet, which is a constant time.
    However, in general terms, if we consider any possible character 
    (not just English alphabet), this would be (O(k)), where (k) is the number 
    of unique characters in the string.

    Combining the two steps, the overall time complexity is 
    (O(n) + O(k) = O(n)) as k<= n .
    
    Space Complexity:
    Hashmap for character frequencies: The space taken by the hashmap is 
    proportional to the number of unique characters in the string. 
    In the worst case, this would be (O(26)) for the English alphabet, 
    which is a constant space. However, in general terms, if we consider 
    any possible character (not just English alphabet), this would be 
    (O(k)), where (k) is the number of unique characters in the string.

    Thus, the space complexity of the algorithm is (O(1)).'''


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxNumberOfBalloons("balloonballoon"))  # Expected: 2
    print(sol.maxNumberOfBalloons("bbaall"))          # Expected: 0
    print(sol.maxNumberOfBalloons("balloonballoooon"))  # Expected: 2
