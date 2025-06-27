'''You're given a string s and a list of words words, 
where all words have the same length.

A concatenated substring is formed by joining all the words from any permutation 
of words — each used exactly once, without any extra characters in between.

For example, if words = ["ab", "cd", "ef"], then valid concatenated strings 
include "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab". 
A string like "acdbef" is not valid because it doesn't match any complete 
permutation of the given words.

Return all starting indices in s where such concatenated substrings appear.
You can return the indices in any order.

Example 1:

Input: String="catfoxcat", Words=["cat", "fox"]  
Output: [0, 3]  
Explanation: The two substring containing both the words are "catfox" & "foxcat".
Example 2:

Input: String="catcatfoxfox", Words=["cat", "fox"]  
Output: [3]
Explanation: The only substring containing both the words is "catfox".
'''


class Solution:
    def findWordConcatenation(self, str1, words):
        if len(words) == 0 or len(words[0]) == 0:
            return []

        word_frequency = {}

        for word in words:
            if word not in word_frequency:
                word_frequency[word] = 0
            word_frequency[word] += 1

        result_indices = []
        words_count = len(words)
        word_length = len(words[0])

        for i in range((len(str1) - words_count * word_length)+1):
            words_seen = {}
            for j in range(0, words_count):
                next_word_index = i + j * word_length
                # Get the next word from the string
                word = str1[next_word_index: next_word_index + word_length]
                if word not in word_frequency:  # Break if we don't need this word
                    break

                # Add the word to the 'words_seen' map
                if word not in words_seen:
                    words_seen[word] = 0
                words_seen[word] += 1

                # No need to process further if the word has higher frequency than required
                if words_seen[word] > word_frequency.get(word, 0):
                    break

                if j + 1 == words_count:  # Store index if we have found all the words
                    result_indices.append(i)

        return result_indices

from collections import Counter


def findSubstring(s, words):
    if not s or not words or len(words[0]) == 0:
        return []

    word_length = len(words[0])
    num_words = len(words)
    total_length = word_length * num_words
    word_count = Counter(words)
    result_indices = []

    for i in range(len(s) - total_length + 1):
        seen = {}
        for j in range(0, total_length, word_length):
            word = s[i + j: i + j + word_length]
            if word in word_count:
                seen[word] = seen.get(word, 0) + 1
                if seen[word] > word_count[word]:
                    break
            else:
                break
        else:
            result_indices.append(i)

    return result_indices


def main():
    sol = Solution()
    print(sol.findWordConcatenation("catfoxcat", ["cat", "fox"]))
    print(sol.findWordConcatenation("catcatfoxfox", ["cat", "fox"]))


main()
