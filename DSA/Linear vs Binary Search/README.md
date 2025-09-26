⸻

# 📘 Linear vs Binary Search (C Language)

🎥 **Video Title:** Linear Vs Binary Search
🔗 [Watch on YouTube](https://www.youtube.com/watch?v=ZHCP9vFOJiU&list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi&index=12)  

---

## 📌 What You Will Learn Today

- How **linear search** goes one-by-one through each array element until it finds the target.
- How **binary search** cuts the search space in half repeatedly — but requires **sorted arrays**.
- The difference in **efficiency** between both algorithms.
- Implementing both in **C language** and conceptually comparing their behavior.
- Time complexity differences in **best**, **worst**, and **average** cases.
- Translation into **Python** versions for easier readability and use.

---

## 🧒 Beginner‑Friendly Explanation Table

| 📌 Concept         | 👶 Simple Explanation                                  | 🧠 Memory Hook                              |
|-------------------|--------------------------------------------------------|---------------------------------------------|
| Linear Search     | Check one item at a time till you find the target      | Like flipping every book until you find it  |
| Binary Search     | Check middle, then go left or right                    | Like guessing a number using hot/cold hints |
| Sorted Data Req.  | Binary needs data to be sorted                         | Like searching an address book alphabetically |
| Time Complexity   | Linear = O(n), Binary = O(log n)                       | Binary is faster, but needs sorted data     |

---

## 🐍 & 💻 Code Examples (C + Python)

### 🔎 C Code: Linear & Binary Search

```c
#include <stdio.h>

int linearSearch(int arr[], int size, int target) {
    for(int i = 0; i < size; i++) {
        if(arr[i] == target)
            return i;
    }
    return -1;
}

int binarySearch(int arr[], int low, int high, int target) {
    while(low <= high) {
        int mid = low + (high - low) / 2;
        if(arr[mid] == target)
            return mid;
        else if(arr[mid] < target)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

int main() {
    int arr[] = {2, 4, 6, 8, 10, 12};
    int size = sizeof(arr)/sizeof(arr[0]);
    int target = 8;

    int indexLinear = linearSearch(arr, size, target);
    int indexBinary = binarySearch(arr, 0, size - 1, target);

    printf("Linear Search Found at: %d\n", indexLinear);
    printf("Binary Search Found at: %d\n", indexBinary);
    return 0;
}
```

⸻

🐍 Python Code: Linear & Binary Search

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example
arr = [2, 4, 6, 8, 10, 12]
target = 8
print("Linear:", linear_search(arr, target))  # Output: 3
print("Binary:", binary_search(arr, target))  # Output: 3

```
⸻

## 📊 Summary Table

| ✅ Search Type   | ⏱️ Best Case | ⏱️ Worst Case | 💡 Notes                        |
|------------------|--------------|---------------|----------------------------------|
| Linear Search     | O(1)         | O(n)          | No need for sorted array         |
| Binary Search     | O(1)         | O(log n)      | Works only on sorted arrays      |


⸻

💬 One‑Line Summary

“Linear search checks everything one-by-one, binary search jumps smartly through sorted data to find the target fast.”

⸻

🔁 Flash Revision Prompts
-	1.	Why is binary search faster than linear?
-	2.	What happens if you run binary search on unsorted data?
-	3.	When is linear search still useful?
-	4.	What’s the mid calculation in binary search and why?

⸻

✅ Citation

-📚 Based on: Linear Vs Binary Search + Code in C Language
-🎥 YouTube Playlist: DSA in C/C++ – CodeWithHarry
-🧠 All credit to the original creator

⸻
