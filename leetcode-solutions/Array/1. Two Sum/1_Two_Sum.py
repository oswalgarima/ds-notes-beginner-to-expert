# LeetCode #1: Two Sum
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/two-sum/

# Problem:
# Given a list of integers and a target number,
# return the indices of the two numbers that add up to the target.

# You can assume:
# - Each input has exactly one solution
# - You cannot use the same element twice
# - You can return the indices in any order

def twoSum(nums, target):
    # Create an empty dictionary to store numbers we’ve seen so far
    # Format: { number : index }
    seen = {}

    # Loop through the list with index and number
    for i, num in enumerate(nums):
        # Calculate the number we need to reach the target
        complement = target - num

        # Check if we’ve already seen that complement number before
        if complement in seen:
            # ✅ Found the answer! Return the indices
            return [seen[complement], i]

        # Save the current number and its index for later
        seen[num] = i

    # This return will never be hit because the problem guarantees one solution
    return []

# Example Test Cases
print(twoSum([2, 7, 11, 15], 9))     # Output: [0, 1]
print(twoSum([3, 2, 4], 6))          # Output: [1, 2]
print(twoSum([3, 3], 6))             # Output: [0, 1]