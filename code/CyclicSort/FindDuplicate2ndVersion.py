'''Problem 1: Can we solve the above problem in O(1) space and without modifying 
the input array?

Solution: While doing the cyclic sort, we realized that the array will 
have a cycle due to the duplicate number and that the start of the cycle 
will always point to the duplicate number. This means that we can use the 
fast & the slow pointer method to find the duplicate 
number or the start of the cycle similar to Start of LinkedList Cycle.
The time complexity of the above algorithm is O(n) and the space complexity is O(1).'''


class Solution:
    def findDuplicate(self, arr):
        slow, fast = arr[0], arr[arr[0]]
        while slow != fast:
            slow = arr[slow]
            fast = arr[arr[fast]]

        # find cycle length
        current = arr[arr[slow]]
        cycleLength = 1
        while current != arr[slow]:
            current = arr[current]
            cycleLength += 1

        return self.find_start(arr, cycleLength)

    def find_start(self, arr, cycleLength):
        pointer1, pointer2 = arr[0], arr[0]
        # move pointer2 ahead 'cycleLength' steps
        while cycleLength > 0:
            pointer2 = arr[pointer2]
            cycleLength -= 1

        # increment both pointers until they meet at the start of the cycle
        while pointer1 != pointer2:
            pointer1 = arr[pointer1]
            pointer2 = arr[pointer2]

        return pointer1


def main():
    sol = Solution()
    print(sol.findDuplicate([1, 4, 4, 3, 2]))
    print(sol.findDuplicate([2, 1, 3, 3, 5, 4]))
    print(sol.findDuplicate([2, 4, 1, 4, 4]))


main()
