⸻

# 📘 Deletion Operation in Array (C Language)

🎥 **Video Title:** Coding Deletion Operation in Array Using C Language  
🔗 [Watch on YouTube](https://www.youtube.com/watch?v=2jVcRw1jP9I&list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi&index=14)  

---

## 📌 What You Will Learn Today

- How to implement **deletion** of an element at a given index in a static array in C.  
- The process for **shifting elements** to the left after deletion to fill the gap.  
- How to check for invalid deletion (index out of bounds) and update the size of the array.  
- Time complexity of deletion in best and worst cases.  
- Also some ideas for how this would translate in Python (lists) which handle many operations for you.

---

## 🧒 Beginner‑Friendly Explanation Table

| 📌 Concept           | 👶 Simple Explanation                                             | 🧠 Memory Hook                        |
|----------------------|-------------------------------------------------------------------|----------------------------------------|
| Deletion             | Remove an item at a specific position and shift the rest         | Like pulling a book out and closing the gap |
| Valid Index Check    | Make sure the position you want to delete exists                | Checking the box number is real       |
| Shift Left           | Move all later items one position to the left                    | Pushing all books left to fill the hole |
| Update Size          | Reduce the count of how many items are in the array              | Like reducing your list size          |
| Time Complexity      | Deletion often costs more time if deletion is in the middle       | More shifting = more work              |

---

## 🐍 & 💻 Code Examples (C + Python)

### 🔎 C Example (Based on Video)

```c
#include <stdio.h>
#define MAX 100

int main() {
    int arr[MAX] = {1, 2, 3, 4, 5};  
    int size = 5;
    int index = 2;  // Delete element at position 2 (0‑based)

    if(index < 0 || index >= size) {
        printf("Invalid index\\n");
        return 1;
    }

    // Shift elements left
    for(int i = index; i < size - 1; i++) {
        arr[i] = arr[i + 1];
    }

    size--;

    // Display updated array
    for(int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\\n");
    return 0;
}

```
⸻

🐍 Python Example (Similar Behavior)
```python

def delete_at(arr, index):
    if index < 0 or index >= len(arr):
        raise IndexError("Invalid index")
    # Delete the item
    arr.pop(index)  # Python’s list auto‑shifts for you
    return arr

# Example:
my_list = [1, 2, 3, 4, 5]
print(delete_at(my_list, 2))  # [1, 2, 4, 5]
```

⸻

📊 Summary Table

Operation	Best Case Time Complexity	Worst Case Time Complexity	Notes
Deletion at end	O(1) (if deleting last)	O(n) (if shifting needed)	Fewer shifts needed if deleting end
Deletion in middle	O(n)	O(n)	All elements after must shift
Python .pop(index)	O(n)	O(n)	Under the hood does the shifting


⸻

💬 One‑Line Summary

“Deleting an element in an array in C means pulling it out and shifting everything after it — it’s fast if it’s at the end, slower in the middle.”

⸻

🔁 Flash Revision Prompts
-	1.	Why is deletion in the middle more expensive than deletion at the end?
-	2.	What checks should you do before deleting (e.g. index bounds)?
-	3.	How does Python simplify deletion compared to C?
-	4.	What is the time complexity of deletion at various positions?

⸻

✅ Citation

- 📚 Based on: Coding Deletion Operation in Array Using C Language by CodeWithHarry
- 📺 YouTube Playlist: DSA in C/C++ – CodeWithHarry
- 🧠 All credit to the original creator.

⸻
