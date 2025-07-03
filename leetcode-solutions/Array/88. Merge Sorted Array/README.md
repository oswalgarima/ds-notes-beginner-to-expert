
⸻

# 🧩 LeetCode 88 – Merge Sorted Array (Easy)

### 📄 Problem Statement

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums2` into `nums1` as one sorted array.

> ⚠️ Note:  
The final sorted array should be stored **inside `nums1` only**. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements are meaningful, and the rest are 0 placeholders.

---

### 🍭 Real-Life Analogy (Child-level Intuition)

You have a box of candies sorted alphabetically:  
`[Chocolate, Mango, Orange, _, _, _]`  
And another small box:  
`[Mango, Pineapple, Strawberry]`

Mom says:
> “Put all candies in one box and keep them in order!”

You use the empty space at the back of `nums1` to fill bigger candies from the **end** first.

---

### 🔍 Step-by-Step Dry Run (With Indices)

**Input:**
```python
nums1 = [1, 2, 3, 0, 0, 0], m = 3  
nums2 = [2, 5, 6], n = 3

We start comparing from the end:

Pointer	Value
i = m - 1 = 2	nums1[2] = 3
j = n - 1 = 2	nums2[2] = 6
k = m + n - 1 = 5	last index of nums1

▶ Steps:
	•	Compare 3 and 6 → place 6 at index 5 → nums1 = [1, 2, 3, 0, 0, 6]
	•	Compare 3 and 5 → place 5 at index 4 → nums1 = [1, 2, 3, 0, 5, 6]
	•	Compare 3 and 2 → place 3 at index 3 → nums1 = [1, 2, 3, 3, 5, 6]
	•	Compare 2 and 2 → place 2 at index 2 → nums1 = [1, 2, 2, 3, 5, 6]
	•	Done!

⸻

🧠 Key Idea

Start merging from the end using 3 pointers:
One at the end of nums1 (real part), one at the end of nums2, and one at the total end of nums1.

⸻


🧵 One-Liner Takeaway

Always start merging from the end to avoid overwriting existing values in nums1.

⸻

📘 Tags

#Array #TwoPointers #Merge #InPlace

⸻

🧠 Confidence Reminder

If you struggled with this problem, it’s okay!
You’re not weak — you just need the right way to think.
This is how every great coder starts 💪

---
