⸻


# 📘 Array ADT Implementation in C (+ Python version)


---

## 📌 What You Will Learn Today

- What it means to implement an **Array as an Abstract Data Type (ADT)** in C: wrapping up arrays and operations in a clean interface.  
- Common operations include: create, access, modify/update, display, maybe delete.  
- How ADT separates **what** operations you can do from **how** they are done.  
- Python doesn’t force you to implement ADTs strictly, but you can simulate similar structure-friendly code for learning.

---

## 🐍 & 💻 Code Example

### 🔎 C Example (Based on Video)

```cpp
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *data;         // pointer to array elements
    int size;          // number of used elements
    int capacity;      // total allocated capacity
} ArrayADT;

ArrayADT* create(int capacity) {
    ArrayADT* arr = malloc(sizeof(ArrayADT));
    arr->data = malloc(capacity * sizeof(int));
    arr->size = 0;
    arr->capacity = capacity;
    return arr;
}

int get(ArrayADT* arr, int index) {
    if (index < 0 || index >= arr->size) {
        // handle error, e.g. return -1 or exit
        return -1;
    }
    return arr->data[index];
}

void set(ArrayADT* arr, int index, int value) {
    if (index < 0 || index >= arr->size) {
        // handle error
        return;
    }
    arr->data[index] = value;
}

void display(ArrayADT* arr) {
    for (int i = 0; i < arr->size; i++) {
        printf("%d ", arr->data[i]);
    }
    printf("\\n");
}

void destroy(ArrayADT* arr) {
    free(arr->data);
    free(arr);
}

```
⸻

🐍 Python Version (Simulating Array ADT for Beginners)

```python
class ArrayADT:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.data[index]

    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.data[index] = value

    def add(self, value):
        if self.size >= self.capacity:
            raise OverflowError("Array capacity reached")
        self.data[self.size] = value
        self.size += 1

    def display(self):
        for i in range(self.size):
            print(self.data[i], end=" ")
        print()

```
⸻

🧒 Beginner‑Friendly Explanation Table

| 💡 Concept        | 👶 Simple Explanation                                     | 🧠 Memory Hook                          |
|------------------|-----------------------------------------------------------|----------------------------------------|
| Array ADT        | A box that holds items + rules for how to use it         | Like a toolbox + instruction sheet     |
| Capacity & Size  | Capacity = how many items it could hold, Size = used slots | A shelf vs number of books placed      |
| Create           | Build the box with empty slots                            | Making the toolbox                     |
| Get / Set        | Read or write at a specific position                      | Open slot #3 / Put book in slot #3     |
| Add Element      | Place new item at next available slot                     | Like adding new item in empty box slot |
| Display          | Show all items currently in the array                     | Taking out books to show others        |
| Destroy          | Free memory when done                                     | Throwing away old box after cleaning   |


⸻

💬 One‑Line Summary

“In C, implementing Array as ADT means wrapping data + operations in a clean interface; you can mirror this in Python by creating classes with similar methods.”

⸻

🔁 Flash Revision Prompts
-	1.	What is the difference between array implementation in C and the Python class version?
-	2.	Why do we separate interface (ADT) from implementation?
-	3.	What happens if you try to set or get outside the array size?
-	4.	How would you increase capacity if needed (dynamic array)?

⸻

✅ Citation

-📚 Based on: Implementing Array as an Abstract Data Type in C Language by CodeWithHarry
-📺 YouTube Playlist: DSA in C/C++ – CodeWithHarry
-🧠 All credit to the original creator.

⸻

**Made with 💙 by [@oswalgarima](https://github.com/oswalgarima)**  
*Learning out loud, one note at a time 🚀*
