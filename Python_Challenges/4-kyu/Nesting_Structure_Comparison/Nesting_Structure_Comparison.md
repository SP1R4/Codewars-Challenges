# Nesting Structure Comparison

This repository contains a solution to the **Same Structure As** problem, which checks if two lists have the same structure. Two lists have the same structure if they have the same nested arrangement of lists, regardless of their content.

## 📝 Problem Description

Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

### Example
```
# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
## 💡 Solution
```

The solution uses recursion to compare the structure of two lists, ensuring they have the same nested arrangement.

### Approach

1. **Check Base Cases**: Determine if both inputs are lists and compare their lengths.
2. **Recursive Comparison**: Use recursion to compare corresponding elements of both lists.
3. **Return Result**: Return `True` if the structures match and `False` otherwise.

### Code Implementation

```python
def same_structure_as(a, b):
    def is_list(p):
        return isinstance(p, list)
    
    if not is_list(a) and not is_list(b):
        return True
    elif (is_list(a) and is_list(b)) and (len(a) == len(b)):
        return all(map(same_structure_as, a, b)) # Here
    return False
```

### How It Works

- **Helper Function**: The `is_list` function checks if a given parameter is a list.
- **Base Case**: If neither `a` nor `b` are lists, their structures match.
- **Recursive Case**:
  - If both `a` and `b` are lists and have the same length, recursively check the structure of each corresponding element.
  - The `map` function is used to apply the `same_structure_as` function to each pair of elements from `a` and `b`.
- **Final Result**: The function returns `True` if all corresponding elements have the same structure, and `False` otherwise.
