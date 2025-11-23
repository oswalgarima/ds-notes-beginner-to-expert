# 📘 Linked List Data Structure: Deletion in C and Python

🎥 **Video Title:** Deletion in a Linked List | Deleting a Node  
🔗 [Watch on YouTube](https://www.youtube.com/watch?v=R_7qJzAWrMg&list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi&index=17)  

---

## 📌 What You Will Learn Today

- How to **delete a node** from a linked list using C language.
- Different deletion operations:
  - **Delete at the beginning (head)**
  - **Delete at the end (tail)**
  - **Delete at a specific position**
- How pointers are adjusted safely to avoid memory loss.
- Importance of handling special cases:
  - Empty list  
  - Single-node list  
  - Invalid positions
- Why `free()` is required to release memory in C.
- Traversal logic used to reach previous nodes during deletion.

---

## 🧒 Beginner-Friendly Explanation Table

| 📌 Concept             | 👶 Simple Explanation                                  | 🧠 Memory Hook                                      |
|-----------------------|--------------------------------------------------------|------------------------------------------------------|
| Delete at Head        | Remove the first node and move head to next            | Like cutting the first link of a chain ✂️            |
| Delete at End         | Go to last node’s previous, unlink last node           | Like removing the last coach of a train 🚃           |
| Delete at Position    | Reach (pos−1), unlink the next node                    | Like removing a bead from the middle of a necklace 📿 |
| Traversal             | Move one node at a time until target is reached        | Like stepping through connected rooms 🚪             |
| free() in C           | Releases memory after deletion                         | Like returning a rented room after checkout 🛏️       |

---

## 💻 Code Examples (C + Python)

### 🔎 C Code: Deletion in Linked List

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

// Delete at head
void deleteAtHead(struct Node** head_ref) {
    if (*head_ref == NULL) return;

    struct Node* temp = *head_ref;
    *head_ref = (*head_ref)->next;
    free(temp);
}

// Delete at end
void deleteAtEnd(struct Node* head) {
    if (head == NULL || head->next == NULL) return;

    struct Node* prev = NULL;
    while (head->next != NULL) {
        prev = head;
        head = head->next;
    }

    prev->next = NULL;
    free(head);
}

// Delete at position
void deleteAtPosition(struct Node* head, int pos) {
    if (head == NULL) return;

    for (int i = 0; i < pos - 1 && head->next != NULL; i++) {
        head = head->next;
    }

    if (head->next == NULL) return;

    struct Node* temp = head->next;
    head->next = temp->next;
    free(temp);
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
    // Create simple list: 10 -> 20 -> 30 -> 40
    struct Node* head = malloc(sizeof(struct Node));
    head->data = 10;
    head->next = malloc(sizeof(struct Node));
    head->next->data = 20;
    head->next->next = malloc(sizeof(struct Node));
    head->next->next->data = 30;
    head->next->next->next = malloc(sizeof(struct Node));
    head->next->next->next->data = 40;
    head->next->next->next->next = NULL;

    deleteAtHead(&head);
    deleteAtEnd(head);
    deleteAtPosition(head, 1);  // delete middle element

    printList(head);  // Expected output: 20 -> NULL
    return 0;
}
```

---

### 🔍 Python Equivalent: Deletion in Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def delete_at_head(self):
        if not self.head:
            return
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None

    def delete_at_position(self, pos):
        if pos == 0:
            self.delete_at_head()
            return
        curr = self.head
        for _ in range(pos - 1):
            if not curr or not curr.next:
                return
            curr = curr.next
        curr.next = curr.next.next if curr.next else None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("NULL")

# Example usage
ll = LinkedList()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next = Node(40)

ll.delete_at_head()
ll.delete_at_end()
ll.delete_at_position(1)
ll.print_list()  # Output: 20 -> NULL
```

---

## 📊 Summary Table

| ✅ Operation          | ⏱️ Time Complexity | 💡 Notes                                              |
|----------------------|--------------------|------------------------------------------------------|
| Delete at Head       | O(1)               | Fastest deletion                                      |
| Delete at End        | O(n)               | Must reach second-last node                           |
| Delete at Position   | O(n)               | Traversal required to reach previous node             |
| Traversal            | O(n)               | Needed for most deletions except head                 |

---

## 💬 One-Line Summary

> “Deleting in a linked list means carefully unlinking the right node — whether at the start, middle, or end, pointer handling is everything!”

---

## 🔁 Flash Revision Prompts

- How do you delete the **first** node in C?
- Why does deleting the **last** node require traversal?
- What happens if you delete with an invalid position?
- Why is `free()` important in linked list deletion?
- What’s the time complexity of deleting at a position?

---

## ✅ Citation

📚 Based on: **Deletion in a Linked List**  
📺 YouTube Playlist: **DSA in C/C++** by CodeWithHarry  
🧠 All credit goes to the original creator.

---

**Made with 💙 by [@oswalgarima](https://github.com/oswalgarima)**  
_Learning out loud, one note at a time 🚀_
