# 📘 Linked List Data Structure: Insertion in C and Python Language

🎥 **Video Title:** Insertion in a Linked List in C Language  
🔗 [Watch on YouTube](https://www.youtube.com/watch?v=_PuIzVqJJbA&list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi&index=16)  

---

## 📌 What You Will Learn Today

- How to insert a node into a **linked list** using **C language**.
- Insertion at different locations:
  - At the **beginning (head)**
  - At the **end (tail)**
  - At a specific **position** in the middle
- Why we pass `struct Node** head_ref` when inserting at the beginning.
- How memory is dynamically allocated using `malloc`.
- Importance of traversal for inserting at position or at the end.
- Proper pointer manipulation to avoid memory issues and segmentation faults.

---

## 🧒 Beginner-Friendly Explanation Table

| 📌 Concept           | 👶 Simple Explanation                          | 🧠 Memory Hook                                 |
|---------------------|-----------------------------------------------|------------------------------------------------|
| Insert at Head      | Add node in front and link to old head        | Like adding a new engine in front of a train 🚂 |
| Insert at End       | Traverse till last node and link new one      | Like attaching a new trailer to the end 🚛      |
| Insert at Position  | Go to previous node, link new node correctly  | Like sneaking a box into a linked chain 📦      |
| Traversal           | Moving node by node until reaching target     | Like walking through connected rooms 🚪         |
| malloc in C         | Allocates memory for new node                 | Like renting space before adding furniture 🛏️  |

---

## 💻 Code Examples (C + Python)

### 🔎 C Code: Inserting Nodes at Various Positions

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

// Insert at head
void insertAtHead(struct Node** head_ref, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = *head_ref;
    *head_ref = newNode;
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

// Insert at position
void insertAtPosition(struct Node* head, int value, int pos) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;

    for (int i = 0; i < pos - 1 && head != NULL; i++) {
        head = head->next;
    }

    if (head == NULL) return; // Invalid position

    newNode->next = head->next;
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

    insertAtHead(&head, 30);
    insertAtHead(&head, 20);
    insertAtHead(&head, 10);
    insertAtEnd(head, 40);
    insertAtPosition(head, 25, 2); // After 2nd node

    printList(head); // Output: 10 -> 20 -> 25 -> 30 -> 40 -> NULL
    return 0;
}
```

---

### 🔍 Python Equivalent: Insertion in Linked List

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

    def insert_at_position(self, value, pos):
        new_node = Node(value)
        curr = self.head
        for _ in range(pos - 1):
            if not curr:
                return
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("NULL")

# Example
ll = LinkedList()
ll.insert_at_head(30)
ll.insert_at_head(20)
ll.insert_at_head(10)
ll.insert_at_end(40)
ll.insert_at_position(25, 2)
ll.print_list()  # Output: 10 -> 20 -> 25 -> 30 -> 40 -> NULL
```

---

## 📊 Summary Table

| ✅ Operation        | ⏱️ Time Complexity | 💡 Notes                                           |
|--------------------|--------------------|----------------------------------------------------|
| Insert at Head     | O(1)               | Constant time, pointer shift only                  |
| Insert at End      | O(n)               | Traverse to last node unless tail pointer used     |
| Insert at Position | O(n)               | Traverse to (pos−1) node and adjust pointers       |
| Traversal          | O(n)               | Needed for most mid/end insertions                 |

---

## 💬 One-Line Summary

> "Inserting in a linked list is just carefully pointing next arrows — whether it’s front, middle, or end, pointers must stay in sync!"

---

## 🔁 Flash Revision Prompts

- How do you insert a node at the **beginning** in C?
- Why do we pass `**head` when inserting at head?
- What’s the time complexity of inserting at a position?
- What happens if you forget to link the new node’s `next` properly?
- How does `malloc` help when inserting a node?

---

## ✅ Citation

📚 Based on: **Insertion in a Linked List in C Language**  
📺 YouTube Playlist: **DSA in C/C++** by CodeWithHarry  
🧠 All credit to the original creator.

---

**Made with 💙 by [@oswalgarima](https://github.com/oswalgarima)**  
_Learning out loud, one note at a time 🚀_
