⸻

# 📘 Introduction to Linked List

🎥 **Video Title:** Introduction to Linked List in Data Structures  
🔗 [Watch on YouTube](https://www.youtube.com/watch?v=TWMCMvfEAv4&list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi&index=13)  

---

## 📌 What You Will Learn Today

- What a **linked list** is and how it's different from arrays.  
- How data is stored using **nodes** and **pointers** instead of continuous memory.  
- The role of the **head** node in a linked list.  
- How to **create**, **traverse**, and **display** a basic linked list in C.  
- When to use **linked lists** instead of arrays (dynamic memory, flexible insertions/deletions).  
- Concepts like **node structure**, **next pointers**, and **dynamic allocation using malloc**.  

---

## 🧒 Beginner‑Friendly Explanation Table

| 📌 Concept           | 👶 Simple Explanation                                       | 🧠 Memory Hook                               |
|---------------------|-------------------------------------------------------------|----------------------------------------------|
| Linked List         | Chain of data boxes (nodes), each pointing to the next      | Like a treasure hunt with clues to next step |
| Node                | One box with a value and pointer to next                    | A bead on a necklace                         |
| Head                | Starting point of the list                                  | First train car that pulls all others        |
| Traversal           | Going from one node to the next until NULL                  | Walking along a path with arrows             |
| Dynamic Memory      | Space is given only when needed, not in advance             | Like expanding a notebook page by page       |
| malloc              | Allocates memory for a node in C                            | Shopping for a box before you use it         |

---

## 🐍 & 💻 Code Examples (C + Python Concept)

### 🔎 C Code: Basic Linked List

```c
#include <stdio.h>
#include <stdlib.h>

// Define node structure
struct Node {
    int data;
    struct Node* next;
};

// Create a new node with data
struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;
    return newNode;
}

// Print the linked list
void printList(struct Node* head) {
    struct Node* current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    // Creating nodes manually
    struct Node* head = createNode(10);
    head->next = createNode(20);
    head->next->next = createNode(30);

    // Print the list
    printList(head);
    return 0;
}
```

⸻

🐍 Python Concept: Same Idea with Classes

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("NULL")

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.print_list()  # Output: 10 -> 20 -> 30 -> NULL
```

---

## 📊 Summary Table

| ✅ Operation         | ⏱️ Time Complexity | 💡 Notes                                               |
|---------------------|--------------------|--------------------------------------------------------|
| Traversal           | O(n)               | Must go node-by-node to reach end                     |
| Insertion at Head   | O(1)               | Just point new node to old head                       |
| Insertion at End    | O(n)               | Need to traverse entire list unless tail is tracked   |
| Deletion (General)  | O(n)               | Find node, update links                                |

---

💬 **One-Line Summary**  
> “A linked list is like a flexible chain of boxes where each one knows where the next is — it grows and shrinks without needing a fixed size.”

---

🔁 **Flash Revision Prompts**

1. What’s the main difference between arrays and linked lists in memory layout?  
2. Why is traversal O(n) even for a short operation?  
3. What’s the role of `malloc` in C linked lists?  
4. How is the last node of a linked list identified?  
5. What happens if you forget to update the next pointer in insertion?

---

✅ **Citation**

📚 Based on: *Introduction to Linked List in Data Structures*  
📺 YouTube Playlist: DSA in C/C++ – CodeWithHarry  
🧠 All credit to the original creator.

⸻

**Made with 💙 by [@oswalgarima](https://github.com/oswalgarima)**  
*Learning out loud, one note at a time 🚀*
