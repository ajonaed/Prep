class Solution:
    def searchQuadruplets(self, arr, target):
        arr.sort()
        quadruplets = []
        for i in range(0, len(arr)-3):
            # skip same element to avoid duplicate quadruplets
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            for j in range(i + 1, len(arr)-2):
                # skip same element to avoid duplicate quadruplets
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
                self.search_pairs(arr, target, i, j, quadruplets)
        return quadruplets

    def search_pairs(self, arr, target_sum, first, second, quadruplets):
        left = second + 1
        right = len(arr) - 1
        while (left < right):
            quad_sum = arr[first] + arr[second] + arr[left] + arr[right]
            if quad_sum == target_sum:  # found the quadruplet
                quadruplets.append(
                    [arr[first], arr[second], arr[left], arr[right]])
                left += 1
                right -= 1
                while (left < right and arr[left] == arr[left - 1]):
                    left += 1  # skip same element to avoid duplicate quadruplets
                while (left < right and arr[right] == arr[right + 1]):
                    right -= 1  # skip same element to avoid duplicate quadruplets
            elif quad_sum < target_sum:
                left += 1  # we need a pair with a bigger sum
            else:
                right -= 1  # we need a pair with a smaller sum


def main():
    sol = Solution()
    print(sol.searchQuadruplets([4, 1, 2, -1, 1, -3], 1))
    print(sol.searchQuadruplets([2, 0, -1, 1, -2, 2], 2))


main()
# Paypal Charge Dispute Confirmation Number: 32388264
