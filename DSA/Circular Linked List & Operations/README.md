# 📘 Circular Linked List & Operations

🎥 **Video Title:** Circular Linked List and Operations in Data Structures  
🔗 [Watch on YouTube](https://www.youtube.com/watch?v=41lXYJID3OQ&list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi&index=20)  

---

## 📌 What You Will Learn Today

- What a **Circular Linked List (CLL)** is and how it differs from a normal linked list.
- Why the **last node points back to the head**, forming a loop.
- Operations demonstrated:
  - **Traversal**
  - **Insertion at head**
  - **Insertion at end**
- How pointers must be handled carefully to maintain the circular structure.
- Use cases of circular linked lists such as:
  - Round-robin scheduling  
  - Cyclic processes  
  - Repetitive access patterns
- Why CLL avoids `NULL` terminations and allows continuous iteration.

---

## 🧒 Beginner-Friendly Explanation Table

| 📌 Concept              | 👶 Simple Explanation                                       | 🧠 Memory Hook                                       |
|------------------------|-------------------------------------------------------------|------------------------------------------------------|
| Circular Linked List   | Last node points back to first                             | Like a merry-go-round 🎠                             |
| Tail Pointer           | Points to the last node that reconnects to head           | Like the last person holding the first person’s hand 🔗 |
| Traversal             | Move node-to-node until you return to start                | Like jogging in a circle 🏃‍♀️➰                     |
| Insert at Head        | Add before current head and update last node link          | Like letting someone join at the front of a ring 👥  |
| Insert at End         | Add new node before head and update previous end           | Like adding one more person at the end of a circle 🤝 |

---

## 💻 Code Examples (C + Python Concept)

### 🔎 C Code: Circular Linked List Basics

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

// Insert at end
void insertAtEnd(struct Node** head_ref, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;

    if (*head_ref == NULL) {
        newNode->next = newNode;
        *head_ref = newNode;
        return;
    }

    struct Node* temp = *head_ref;
    while (temp->next != *head_ref) {
        temp = temp->next;
    }

    temp->next = newNode;
    newNode->next = *head_ref;
}

// Print circular list
void printCircular(struct Node* head) {
    if (head == NULL) return;

    struct Node* temp = head;
    do {
        printf("%d -> ", temp->data);
        temp = temp->next;
    } while (temp != head);

    printf("(Back to Head)\n");
}

int main() {
    struct Node* head = NULL;

    insertAtEnd(&head, 10);
    insertAtEnd(&head, 20);
    insertAtEnd(&head, 30);

    printCircular(head); // Output: 10 -> 20 -> 30 -> (Back to Head)

    return 0;
}
```

---

### 🔍 Python Concept: Circular Linked List Logic

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        curr = self.head
        while curr.next != self.head:
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head

    def print_list(self):
        if not self.head:
            return

        curr = self.head
        while True:
            print(curr.data, end=" -> ")
            curr = curr.next
            if curr == self.head:
                break
        print("(Back to Head)")

# Example
cll = CircularLinkedList()
cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)
cll.print_list()
```

---

## 📊 Summary Table

| ✅ Operation              | ⏱️ Time Complexity | 💡 Notes                                                         |
|--------------------------|--------------------|------------------------------------------------------------------|
| Traversal               | O(n)               | Loop ends when pointer reaches head again                        |
| Insert at Head         | O(n)               | Must adjust last node to point to new head                       |
| Insert at End          | O(n)               | Traverse to last node unless tail reference is stored            |
| Searching              | O(n)               | No early exit; must detect loop entry                            |

---

## 💬 One-Line Summary

> **“A circular linked list loops forever — perfect for repeated access, but pointer accuracy is everything.”**

---

## 🔁 Flash Revision Prompts

- What makes a circular linked list different from a singly linked list?
- Why does traversal require a stopping condition based on the head?
- What pointer must be updated when inserting at the head?
- How do circular linked lists help in round-robin scheduling?

---

## ✅ Citation

📚 Based on: **Circular Linked List and Operations**  
📺 Playlist: **DSA in C/C++** by CodeWithHarry  
🧠 All credit belongs to the original creator.

---

**Made with 💙 by [@oswalgarima](https://github.com/oswalgarima)**  
_Learning out loud, one note at a time 🚀_
