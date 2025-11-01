⸻

# 📘 Operations on Arrays – Traversal, Insertion, Deletion & Searching

🎥 **Video Title:** Operations on Arrays in Data Structures: Traversal, Insertion, Deletion and Searching  
🔗 [Watch on YouTube](https://www.youtube.com/watch?v=p5TDnxAYAZY&list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi&index=10)  

---

## 📌 What You Will Learn Today

- What array operations are: traversal (visiting each element), insertion (adding elements), deletion (removing elements), and searching (finding elements).  
- How each operation works in both best and worst cases.  
- Time complexity of these operations in a typical array implementation.  
- How shifting elements is necessary for insertion/deletion in certain positions (not just at end).

---

## 🧒 Beginner‑Friendly Explanation Table

| 📌 Operation     | 👶 Simple Explanation                                             | 🧠 Memory Hook / Analogy                                |
|------------------|-------------------------------------------------------------------|----------------------------------------------------------|
| Traversal        | Going through each item one by one                               | Like reading all books on a shelf                      |
| Searching        | Looking for a specific item                                       | Finding a name in a list                                |
| Insertion        | Adding an item (at end or middle)                                  | Putting a new book on shelf; may shift others           |
| Deletion         | Removing an item (and shifting others to fill gap)                | Taking a book out and closing the gap                  |

---

## 🐍 & 💻 Code Examples (Python & C++)

### 🐍 Python Example

```python
arr = [10, 20, 30, 40, 50]

# Traversal
for x in arr:
    print(x)

# Searching
def search(arr, x):
    for i, val in enumerate(arr):
        if val == x:
            return i
    return -1

# Insertion (at end)
arr.append(60)

# Deletion (remove first occurrence)
arr.remove(30)
```

🔎 C++ Example

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[6] = {10, 20, 30, 40, 50};
    int size = 5;

    // Traversal
    for(int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Searching
    int x = 30;
    int index = -1;
    for(int i = 0; i < size; i++) {
        if(arr[i] == x) {
            index = i;
            break;
        }
    }

    // Insertion at position 2 (shift right)
    for(int i = size; i > 2; i--) {
        arr[i] = arr[i - 1];
    }
    arr[2] = 25;
    size++;

    // Deletion at position 3 (shift left)
    for(int i = 3; i < size - 1; i++) {
        arr[i] = arr[i + 1];
    }
    size--;

    // Display updated array
    for(int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
```

⸻

## 📊 Summary Table

| Operation         | Time Complexity (Best Case) | Time Complexity (Worst Case) | 💡 Notes                                      |
|------------------|------------------------------|-------------------------------|-----------------------------------------------|
| Traversal        | O(n)                         | O(n)                          | Must visit all elements                       |
| Search           | O(1) (if found early)        | O(n)                          | Depends where the item is in the array       |
| Insertion (end)  | O(1)                         | O(n)                          | Fast if appending; slow if resizing needed   |
| Insertion (mid)  | O(n)                         | O(n)                          | All elements after insert point shift forward|
| Deletion (mid)   | O(n)                         | O(n)                          | All elements after delete point shift backward|


⸻

💬 One‑Line Summary

“Arrays allow you to store items in order — but inserting or removing in the middle costs extra work.”

⸻

🔁 Flash‑Revision Prompts
-	1.	What’s the difference between insertion at the end vs insertion in the middle?
-	2.	Why is deletion slower in an array than deletion in other structures like linked lists?
-	3.	How does searching change in best vs worst case?
-	4.	What makes shifting necessary for some operations?

⸻

✅ Citation

📚 Based on: Operations on Arrays in Data Structures: Traversal, Insertion, Deletion and Searching by CodeWithHarry
📺 YouTube Playlist: DSA in C/C++ – CodeWithHarry
🧠 All credit to the original creator.

⸻

**Made with 💙 by [@oswalgarima](https://github.com/oswalgarima)**  
*Learning out loud, one note at a time 🚀*
