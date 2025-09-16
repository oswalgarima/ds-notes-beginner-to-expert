⸻

# 📘 How to Calculate Time Complexity + Solved Questions

---

## 📌 What You Will Learn Today

- How to actually **compute** the time complexity of different code snippets — not just theory, but with examples.  
- When to **drop constant factors and lower-order terms** in big‑O calculations.  
- How different parts of code (loops, nested loops, conditional blocks) contribute to overall complexity.  

---

## 🔍 Key Rules for Calculating Time Complexity

| Rule # | What to Do                                             |
|--------|---------------------------------------------------------|
| 1      | Identify loops, nested loops — each loop mostly adds a factor of n. |
| 2      | For separate statements/blocks — add their complexities. |
| 3      | Ignore constant multipliers (e.g. 2 * n → just O(n)).   |
| 4      | Lower‑order terms (like + n, + 3) are less important than the highest term. |
| 5      | Multiplicative effects from nested structure matter most. |

---

## 🐍 & 💻 Example Code Snippets

### 🐍 Python Example

```python
def sum_array(arr):
    total = 0                  # O(1)
    for x in arr:              # O(n)
        total += x             # O(1) inside loop
    return total               # O(1)
# → Overall: O(n)
```

🔎 C++ Example

```cpp
int sumArray(vector<int>& arr) {
    int total = 0;             // O(1)
    for(int x : arr) {         // O(n)
        total += x;            // O(1)
    }
    return total;              // O(1)
}
// → Overall: O(n)

```
⸻

🧒 Beginner‑Friendly Summary Table

📌 Concept	👶 Child‑Level Explanation	🧠 Memory Hook
Dropping constants	Ignore “x2”, “+3”, etc. since they don’t change growth with n	Like ignoring small pebbles on a big road
Focusing on highest order term	Watch what grows fastest (like n² vs n)	Highest term wins the race
Sum of parts	If you do A then B, add their times (O(A + B))	Like first homework then chores
Nested loops multiply	Inner loop * outer loop → more work	Row × Column grid pattern


⸻

💬 One‑Line Summary

“Calculating time complexity means looking at how loops and operations grow as input gets bigger — and simplifying it by keeping only the dominant part.”

⸻

🔁 Flash Revision Prompts
-	1.	Why do constant factors not matter in big‑O?
-	2.	What happens to complexity when you have nested loops?
-	3.	Give an example of when two separate code blocks are added and how you combine their complexities.
-	4.	How would you simplify O(3n + 2n² + 5)?

⸻

✅ Citation

📚 Based on: How to Calculate Time Complexity of an Algorithm + Solved Questions by CodeWithHarry
📺 YouTube Playlist: DSA in C/C++ – CodeWithHarry
🧠 All credit for video content and examples goes to the original creator.

⸻
