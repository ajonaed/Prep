'''
Given two integer arrays nums1 and nums2, return an array answer such that 
answer[i] is the next greater number for every nums1[i] in nums2.

The next greater element for an element x is the first element to the right 
of x that is greater than x. If there is no greater number, output -1 for that number.

The numbers in nums1 are all present in nums2.

Examples

Input: nums1 = [4,2,6], nums2 = [6,2,4,5,3,7]
Output: [5,4,7]
Explanation: The next greater number for 4 is 5, for 2 is 4, and for 6 is 7 in nums2.

Input: nums1 = [9,7,1], nums2 = [1,7,9,5,4,3]
Output: [-1,9,7]
Explanation: The next greater number for 9 does not exist, for 7 is 9, 
and for 1 is 7 in nums2.

Input: nums1 = [5,12,3], nums2 = [12,3,5,4,10,15]
Output: [10,15,5]
Explanation: The next greater number for 5 is 10, for 12 is 15, 
and for 3 is 5 in nums2.
'''

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # TODO: Write your code here

        stack = []
        numMap = {}

        for num in nums2:
            while stack and stack[-1] < num:
                numMap[stack.pop()] = num
            stack.append(num)
        return [numMap.get(i,-1) for i in nums1]
if __name__ == "__main__":
    solution = Solution()
    print(solution.nextGreaterElement([4, 2, 6], [6, 2, 4, 5, 3, 7])) # Output: [5, 4, 7]
    print(solution.nextGreaterElement([9, 7, 1], [1, 7, 9, 5, 4, 3])) # Output: [-1, 9, 7]
    print(solution.nextGreaterElement([5, 12, 3], [12, 3, 5, 4, 10, 15])) # Output: [10, 15, 5]