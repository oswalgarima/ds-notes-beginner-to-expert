# LeetCode #27: Remove Element
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/remove-element/

# What’s the goal?
# Given an array and a number 'val',
# remove all occurrences of 'val' in-place (without using extra space).
# Then return how many elements are left (not equal to 'val').

def removeElement(nums, val):
    k = 0  # Pointer to place next non-val number

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]  # Keep the current number if it’s not 'val'
            k += 1             # Move pointer forward for next valid number

    return k  # Total count of non-'val' numbers at the front of the array


# Example Test Cases
nums1 = [3, 2, 2, 3]
val1 = 3
k1 = removeElement(nums1, val1)
print(k1, nums1[:k1])  # Output: 2, [2, 2]

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
k2 = removeElement(nums2, val2)
print(k2, nums2[:k2])  # Output: 5, [0, 1, 3, 0, 4] — order may vary