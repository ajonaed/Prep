'''
We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:

If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.

Example 1:

Input: [1, 2, -1, 2, 2]
Output: true
Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0
Example 2:

Input: [2, 2, -1, 2]
Output: true
Explanation: The array has a cycle among indices: 1 -> 3 -> 1
Example 3:

Input: [2, 1, -1, -2]
Output: false
Explanation: The array does not have any cycle.
Constraints:

1 <= arr.length <= 5000
`-1000 <= arr[i] <= 1000
arr[i] != 0
'''
# Time Complexity: O(N^2) where N is the number of elements in the array.
# Space Complexity: O(1) as we are not using any extra space.
class Solution:
    def loopExists(self, arr):
        # TODO: Write your code here
        
        for i in range(len(arr)):
            if arr[i] == 0:
                continue  
            slow = i
            fast = i
            is_forward = arr[i] > 0
        
            while True:
                slow = self._find_next_index(arr, slow, is_forward)
                fast = self._find_next_index(arr, fast, is_forward)
                
                if fast != -1:
                    fast = self._find_next_index(arr, fast, is_forward)
                if slow == -1 or fast == -1 or slow == fast:
                    break
            if slow != -1 and slow == fast:
                return True
        
        return False
    
    def _find_next_index(self, arr, index, is_forward):
        direction = arr[index] > 0
        if direction != is_forward:
            return -1
        
        next_index = (index + arr[index]) % len(arr)
        
        if next_index == index:
            return -1
        
        return next_index
  

def main():
    arr = [1, 2, -1, 2, 2]
    solution = Solution()
    print(solution.loopExists(arr))  # Output: True

    arr = [2, 2, -1, 2]
    print(solution.loopExists(arr))  # Output: True

    arr = [2, 1, -1, -2]
    print(solution.loopExists(arr))  # Output: False

if __name__ == "__main__":
    main()




class Solution2:
    def loopExists(self, arr):
        n = len(arr)
        visited = [False] * n  # Initialize visited array
        
        for i in range(n):
            if visited[i]:
                continue  # Skip already visited indices
            
            isForward = arr[i] >= 0  # Determine the direction
            slow, fast = i, i
            
            # Use slow and fast pointers to detect cycle
            while True:
                slow = self.findNextIndex(arr, isForward, slow)
                fast = self.findNextIndex(arr, isForward, fast)
                if fast != -1:
                    fast = self.findNextIndex(arr, isForward, fast)
                
                if slow == -1 or fast == -1 or slow == fast:
                    break
            
            if slow != -1 and slow == fast:
                return True  # Cycle found
            
            self.markVisited(arr, i, isForward, visited)
        
        return False

    def findNextIndex(self, arr, isForward, currentIndex):
        direction = arr[currentIndex] >= 0
        if isForward != direction:
            return -1  # Change in direction
        
        nextIndex = (currentIndex + arr[currentIndex]) % len(arr)
        if nextIndex < 0:
            nextIndex += len(arr)
        
        if nextIndex == currentIndex:
            return -1  # One element cycle
        
        return nextIndex

    def markVisited(self, arr, startIndex, isForward, visited):
        index = startIndex
        while True:
            visited[index] = True
            nextIndex = self.findNextIndex(arr, isForward, index)
            if nextIndex == -1 or visited[nextIndex]:
                break
            index = nextIndex

# Example usage
solution = Solution()
print(solution.loopExists([1, 2, -1, 2, 2]))  # Expected output: True
print(solution.loopExists([2, 2, -1, 2]))  # Expected output: True
print(solution.loopExists([2, 1, -1, -2]))  # Expected output: False
