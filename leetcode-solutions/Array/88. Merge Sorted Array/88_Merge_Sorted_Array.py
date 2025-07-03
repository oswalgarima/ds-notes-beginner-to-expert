"""
LeetCode 88 – Merge Sorted Array
---------------------------------
You are given two sorted arrays: nums1 and nums2, and two integers m and n.

nums1 has a size of m + n, where the first m elements are valid and the rest are 0s (placeholders).
You need to merge nums2 into nums1, sorted in non-decreasing order.

This function modifies nums1 in-place to store the merged result.

Example:
Input: nums1 = [1,2,3,0,0,0], m = 3
       nums2 = [2,5,6], n = 3
Output: nums1 becomes [1,2,2,3,5,6]
"""

def merge(nums1, m, nums2, n):
    # Initialize three pointers:
    # i = last valid element in nums1
    # j = last element in nums2
    # k = last total index in nums1 (end of the array)
    i = m - 1
    j = n - 1
    k = m + n - 1

    # Merge from the back to avoid overwriting nums1 values
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If nums2 still has elements left, copy them
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# Optional Test Case (Uncomment to run)
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# merge(nums1, 3, nums2, 3)
# print(nums1)  # Output: [1,2,2,3,5,6]