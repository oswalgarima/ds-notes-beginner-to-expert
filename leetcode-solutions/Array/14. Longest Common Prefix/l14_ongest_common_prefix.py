# LeetCode 14: Longest Common Prefix
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/longest-common-prefix/

# GOAL:
# Given a list of strings, return the longest common prefix (starting part) shared by all strings.
# If no common prefix exists, return an empty string "".
'''python
def longestCommonPrefix(strs):
    # Edge Case Check: If the input list is empty, return empty string
    if not strs:
        return ""

    # ✅ Start by assuming the first word is the full prefix.
    # We'll check if other words start with this, and shorten it if needed.
    prefix = strs[0]

    # 🔁 Loop through each word in the list starting from the second one
    for word in strs[1:]:
        # ⏬ While the current word does NOT start with the current prefix
        while not word.startswith(prefix):
            # Shorten the prefix by removing the last character
            prefix = prefix[:-1]

            # If prefix becomes empty, there's no common prefix
            if not prefix:
                return ""

    # ✅ If we make it through the loop, 'prefix' holds the longest common prefix
    return prefix

# 🚀 Example Test Cases:

print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))      # Output: ""
print(longestCommonPrefix(["interspecies", "interstellar", "interstate"]))  # Output: "inters"
print(longestCommonPrefix(["throne", "throne"]))  # Output: "throne"
print(longestCommonPrefix([""]))  # Output: ""
print(longestCommonPrefix(["a"]))  # Output: "a"

'''
