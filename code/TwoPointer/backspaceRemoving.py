class Solution:
    def compare(self, str1, str2):
        # use two pointer approach to compare the strings
        i = len(str1) - 1
        j = len(str2) - 1
        while i >= 0 and j >= 0:
            i = self.get_next_valid_char_index(str1, i)
            j = self.get_next_valid_char_index(str2, j)
            if i < 0 or j < 0 or str1[i] != str2[j]:
                return False
            if i < 0 and j < 0:
                return True
            i -= 1
            j -= 1

        return True

    def get_next_valid_char_index(self, str, index):
        pass


def main():
    sol = Solution()
    print(sol.compare("xy#z", "xzz#"))
    print(sol.compare("xy#z", "xyz#"))
    print(sol.compare("xp#", "xyz##"))
    print(sol.compare("xywrrmp", "xywrrmu#p"))


main()
