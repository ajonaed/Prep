'''Step-by-Step Algorithm
Sort the Array:

Sort the input array in non-decreasing order. This helps in easily skipping duplicate 
elements and applying the two-pointer technique.
Iterate through the Array:

Use a for loop to iterate through the array, stopping at the third-to-last element.
For each element, check if it's the same as the previous one to avoid duplicates.
If it's the same, skip to the next iteration.
Fix the Current Element and Find Pairs:

Fix the current element and use two pointers to find pairs whose sum 
is the negative of the fixed element (targetSum = -arr[i]).
The left pointer starts from the next element (i + 1) and the 
right pointer starts from the end of the array.
Find Pairs with Two Pointers:

Calculate the sum of the left pointer and the right pointer (currentSum = arr[left] + arr[right]).
If the currentSum equals targetSum, add the triplet to the list 
([-targetSum, arr[left], arr[right]]) and move both pointers to the next unique elements.
If currentSum is less than targetSum, move the left pointer to the right to increase the sum.
If currentSum is greater than targetSum, move the right pointer to the left to decrease the sum.
Skip Duplicates:

Ensure that the left and right pointers skip duplicate elements to 
avoid counting the same triplet multiple times.
Return the Result:

After processing all elements, return the list of unique triplets.'''


class Solution:
  def searchTriplets(self, arr):
    


def main():
  sol = Solution()
  print(sol.searchTriplets([-3, 0, 1, 2, -1, 1, -2]))
  print(sol.searchTriplets([-5, 2, -1, -2, 3]))


main()
