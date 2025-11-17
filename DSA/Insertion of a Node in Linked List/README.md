# 📘 Linked List Data Structure: Insertion of a Node

🎥 **Video Title:** Insertion of a Node in a Linked List  
🔗 [Watch on YouTube](https://www.youtube.com/watch?v=ewCc7O2K5SM&list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi&index=16)

---

## 📌 What You Will Learn Today

- How to **insert a node** at different positions in a linked list:
  - At the beginning (head)
  - At the end (tail)
  - At a specific position (e.g., after 2nd node)
- Role of pointers in adjusting `next` references correctly.
- Real-time C code implementation using `malloc()` and `struct`.
- Importance of traversal for positional insertion.
- Dynamic memory and pointer handling for safe insertions.

---

## 🧒 Beginner-Friendly Explanation Table

| 📌 Concept           | 👶 Simple Explanation                          | 🧠 Memory Hook                                |
|---------------------|-----------------------------------------------|-----------------------------------------------|
| Insert at Head      | Add node in front and link to old head        | Like putting a new engine in front of a train 🚂 |
| Insert at End       | Traverse till last node and link new one      | Like adding a new trailer to the end 🚛       |
| Insert at Position  | Go to the position before and re-link nodes   | Like sneaking a box into a chain 📦           |
| Traversal           | Move one node at a time till desired spot     | Like walking room to room through doors 🚪     |
| malloc in C         | Allocates memory for new node                 | Like booking a hotel room before check-in 🛎️   |

---

## 💻 Code Examples (C + Python)

### 🔎 C Code: Insertion in Linked List

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

// Insert at head
void insertAtHead(struct Node** head, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = *head;
    *head = newNode;
}

// Insert at end
void insertAtEnd(struct Node* head, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;

    while (head->next != NULL)
        head = head->next;

    head->next = newNode;
}

// Print list
void printList(struct Node* head) {
    while (head != NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

int main() {
    struct Node* head = NULL;

    insertAtHead(&head, 20);
    insertAtHead(&head, 10);
    insertAtEnd(head, 30);

    printList(head); // Output: 10 -> 20 -> 30 -> NULL
    return 0;
}
```

### 🔎 Python Code: Insertion in Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
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

# Usage
ll = LinkedList()
ll.insert_at_head(20)
ll.insert_at_head(10)
ll.insert_at_end(30)
ll.print_list()  # Output: 10 -> 20 -> 30 -> NULL
```
⸻

## 📊 Summary Table

| ✅ Operation        | ⏱️ Time Complexity | 💡 Notes                                           |
|--------------------|--------------------|----------------------------------------------------|
| Insert at Head     | O(1)               | Quick and simple                                   |
| Insert at End      | O(n)               | Traverse to end unless tail pointer is tracked     |
| Insert at Position | O(n)               | Need to traverse to the (pos−1)th node             |
| Traversal          | O(n)               | Required for most insertions unless at head        |


⸻

💬 One-Line Summary

“Inserting in a linked list is all about updating pointers correctly — whether it’s the start, middle, or end, it’s just a matter of linking right!”

⸻

🔁 Flash Revision Prompts
-	•	How do you insert a node at the beginning of a linked list?
-	•	What’s the time complexity of inserting at the end?
-	•	Why do we use **head in function arguments in C?
-	•	What happens if you forget to update next in the middle insertion?
-	•	How do you handle insertion in an empty list?

⸻

✅ Citation

- 📚 Based on: Insertion of a Node in a Linked List
- 📺 YouTube Playlist: DSA in C/C++ – CodeWithHarry￼
- 🧠 All credit goes to the original creator.

⸻

**Made with 💙 by @oswalgarima￼**
Learning out loud, one note at a time 🚀
