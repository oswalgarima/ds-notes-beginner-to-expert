# 📘 Linked List Data Structure: Delete a Node

🎥 **Video Title:** Delete a Node from Linked List  
🔗 [Watch on YouTube](https://www.youtube.com/watch?v=UQIJNobtzVY&list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi&index=19)  

---

## 📌 What You Will Learn Today

- How to **delete a node** from a linked list in C language.
- Different deletion methods demonstrated:
  - **Delete the first node (head)**
  - **Delete the last node (tail)**
  - **Delete a node by value**
- Importance of handling:
  - Empty linked list  
  - Node not found  
  - Single-node list
- Pointer movement required to locate and unlink the correct node.
- Why we use `free()` to safely release memory after deletion.

---

## 🧒 Beginner-Friendly Explanation Table

| 📌 Concept             | 👶 Simple Explanation                                      | 🧠 Memory Hook                                          |
|-----------------------|------------------------------------------------------------|--------------------------------------------------------|
| Delete by Value       | Find the node with the value & unlink it                  | Like removing a specific bead from a necklace 📿        |
| Delete at Head        | Remove first node & point head to next                    | Cutting the first link of a chain ✂️                    |
| Delete at End         | Reach last node's previous and unlink last                | Removing the last coach of a train 🚃                   |
| Traversal             | Move node-by-node to locate value or position             | Walking room to room following a hallway 🚪            |
| free() in C           | Releases memory of deleted node                           | Like returning your hotel room after checkout 🛏️        |

---

## 💻 Code Examples (C + Python)

### 🔎 C Code: Delete Node by Value

```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

// Delete node by value
void deleteNode(struct Node** head_ref, int value) {
    struct Node* temp = *head_ref;
    struct Node* prev = NULL;

    if (temp != NULL && temp->data == value) {
        *head_ref = temp->next;
        free(temp);
        return;
    }

    while (temp != NULL && temp->data != value) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) return;

    prev->next = temp->next;
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
    struct Node* head = malloc(sizeof(struct Node));
    head->data = 10;
    head->next = malloc(sizeof(struct Node));
    head->next->data = 20;
    head->next->next = malloc(sizeof(struct Node));
    head->next->next->data = 30;
    head->next->next->next = NULL;

    deleteNode(&head, 20); // delete value 20

    printList(head); // Output: 10 -> 30 -> NULL
    return 0;
}
```

---

### 🔍 Python Equivalent: Delete Node by Value

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def delete_node(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
            return

        curr = self.head
        while curr.next and curr.next.data != value:
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next

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

ll.delete_node(20)
ll.print_list()  # Output: 10 -> 30 -> NULL
```

---

## 📊 Summary Table

| ✅ Operation          | ⏱️ Time Complexity | 💡 Notes                                                  |
|----------------------|--------------------|----------------------------------------------------------|
| Delete by Value      | O(n)               | Must traverse to find matching value                     |
| Delete at Head       | O(1)               | Fastest, no traversal needed                             |
| Delete at End        | O(n)               | Must reach second-last node                              |
| Traversal            | O(n)               | Required for value-based deletion                        |

---

## 💬 One-Line Summary

> “Deleting a node in a linked list is all about finding it, unlinking it, and freeing memory — pointer accuracy is key!”

---

## 🔁 Flash Revision Prompts

- How do you delete a specific value in a linked list?
- What happens if the value is in the head node?
- Why is traversal needed in deletion?
- Why must we call `free()` in C?
- What should the code do if the node is not found?

---

## ✅ Citation

📚 Based on: **Delete a Node from Linked List**  
📺 YouTube Playlist: **DSA in C/C++** by CodeWithHarry  
🧠 All credit goes to the original creator.

---

**Made with 💙 by [@oswalgarima](https://github.com/oswalgarima)**  
_Learning out loud, one note at a time 🚀_
