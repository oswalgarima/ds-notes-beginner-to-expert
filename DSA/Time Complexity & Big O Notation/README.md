⸻

# 📘 Day 2: Time Complexity & Big O Notation

---

## 📌 What You Will Learn Today

### ⏱️ What is Time Complexity?

Time Complexity tells us **how the execution time of an algorithm increases** with input size `n`.  
Just like how it takes more time to cook for 10 people than for 2.

| Example             | Time Complexity |
|---------------------|-----------------|
| Constant loop       | O(1)            |
| Loop through `n`    | O(n)            |
| Nested loops        | O(n²)           |
| Binary search       | O(log n)        |

---

### 🔠 What is Big O Notation?

Big O gives a **mathematical expression** of how fast or slow an algorithm is — especially in the **worst-case scenario**.

> “How much does my code slow down as data grows?”

### 📦 Real-life Analogy:

- O(1) → Instant snack from fridge 🍫  
- O(n) → Looking through a backpack 🎒  
- O(n²) → Asking everyone about everyone in class 👥

---

## 🔍 Time Complexity Chart

| Big O      | Name         | Example                       |
|------------|--------------|-------------------------------|
| O(1)       | Constant      | Direct access (e.g., array[0]) |
| O(log n)   | Logarithmic   | Binary Search                 |
| O(n)       | Linear        | Loop over list                |
| O(n log n) | Linearithmic  | Merge Sort, Quick Sort        |
| O(n²)      | Quadratic     | Nested loops                  |
| O(2ⁿ)      | Exponential   | Recursion (e.g., Fibonacci)   |
| O(n!)      | Factorial     | Permutations, TSP             |

---

## 🧪 Sample Code Examples

### 🐍 Python Example

```python
def print_items(n):
    for i in range(n):      # O(n)
        print(i)
```
🔎 C++ Example

```cpp
void printItems(int n) {
    for(int i = 0; i < n; i++) {  // O(n)
        cout << i << endl;
    }
}
```

⸻

🧒 Beginner-Friendly Summary Table

📌 Concept	👶 Child-Level Explanation	🧠 Memory Hook
Time Complexity	How much time code takes as input grows	Pizza for 1 vs 10 people 🍕
Big O Notation	Symbol that shows how fast/slow code grows	Speed limit sign for your code 🚦
O(1)	Constant time	1-button vending machine 🥤
O(n)	Time grows with data	Reading all books on a shelf 📚
O(n²)	Time explodes with more data	Everyone comparing with everyone 👬👭
O(log n)	Input is halved each time	Guess-the-number game 🎯


⸻

💬 One-Line Summary

“Big O helps you predict performance — before running your code.”

⸻

🔁 Flash Revision Prompts
-	1.	What is time complexity in one sentence?
-	2.	Why do we use Big O notation instead of counting steps?
-	3.	Give one real-world example of O(1), O(n), and O(n²).
-	4.	What is the time complexity of binary search?

⸻

✅ Citation

📚 Based on: Time Complexity & Big O Notation by CodeWithHarry
📺 YouTube Playlist: DSA in C/C++ – CodeWithHarry
🧠 All credit for video content goes to the original creator.

⸻

**Made with 💙 by [@oswalgarima](https://github.com/oswalgarima)**  
*Learning out loud, one note at a time 🚀*
