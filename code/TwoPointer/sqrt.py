'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator. 
For example, do not use pow(x, 0.5) in C++ or x ** 0.5 in Python.

Example 1:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.8284, 
and since we need to return the floor of the square root (integer), hence we returned 2.  
Example 2:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2.
Example 3:

Input: x = 2
Output: 1
Explanation: The square root of 2 is 1.414, 
and since we need to return the floor of the square root (integer), hence we returned 1.  

✅Approach:
To compute the square root of x, rounded down 
(i.e., floor(sqrt(x))), without using sqrt() or **, we can use:

Binary Search (Efficient - O(log x)) ✅ Best approach
Brute Force (Slow - O(√x)) ❌ Inefficient for large numbers

Binary search is the most efficient way to find the square root 
by narrowing down the possible values.

🔹 Idea:
    The square root of x always lies between 0 and x.
    Use binary search to find the largest integer m such that m * m ≤ x.
    If m * m > x, search in the left half; otherwise, search in the right half.
'''


def mySqrt(x: int) -> int:
    if x == 0 or x == 1:
        return x  # Base cases

    left, right = 1, x
    ans = 0  # Stores the largest valid sqrt

    while left <= right:
        mid = (left + right) // 2  # Find middle
        if mid * mid == x:
            return mid  # Perfect square found!
        elif mid * mid < x:
            ans = mid  # Store possible answer
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return ans  # Return the floor of sqrt(x)


'''
2️⃣ Alternative (Brute Force O(√x))
A simple but slow approach is to incrementally check squares from 1 to x.

Why is this slow?
    Time Complexity: O(√x), which is worse than O(log x) for large numbers.'''


def mySqrtSlow(x: int) -> int:
    pass  # Return the last valid number


def mySqrtOwnVersion(x):
    pass


print(mySqrtOwnVersion(8))
