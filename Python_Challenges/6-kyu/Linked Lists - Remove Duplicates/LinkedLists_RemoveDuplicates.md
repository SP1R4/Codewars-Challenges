# 🔍 Linked Lists - Remove Duplicates

This repository contains a solution to the **Linked Lists - Remove Duplicates** problem. The goal is to remove duplicate values from a sorted linked list.

## 📝 Problem Description

Write a RemoveDuplicates() function which takes a list sorted in increasing order and deletes any duplicate nodes from the list. Ideally, the list should only be traversed once. The head of the resulting list should be returned.

```
var list = 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> null
removeDuplicates(list) === 1 -> 2 -> 3 -> 4 -> 5 -> null
```

If the passed in list is null/None/nil, simply return null.

Note: Your solution is expected to work on long lists. Recursive solutions may fail due to stack size limitations.

The push() and buildOneTwoThree() functions need not be redefined.


## 💡 Solution

The solution involves iterating through the linked list and removing nodes with duplicate values by adjusting pointers. The function maintains a single pass through the list, which ensures efficiency.

### Approach

1. **Initialize**:
   - Start from the head of the linked list.
2. **Iterate**:
   - Compare each node with the next node.
   - If they have the same value, skip the next node by adjusting pointers.
   - Otherwise, move to the next node.
3. **Return**:
   - Return the head of the modified linked list.

### Code Implementation

```python
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def remove_duplicates(head):
    if head is None:
        return None

    current = head
    while current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head
```

### How It Works

- **Initialization**:
  - Begin at the head node of the linked list.
- **Duplicate Removal**:
  - Traverse the list and compare each node with the next node.
  - Adjust the `next` pointers to remove duplicates.
- **Completion**:
  - Continue until all nodes have been processed.
