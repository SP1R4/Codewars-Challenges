# 🔄 So Many Permutations!

This repository contains a solution to the **So Many Permutations!** problem, which generates all possible permutations of a given list or string.

## 📝 Problem Description

In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!

Examples:
```
With input 'a':
Your function should return: ['a']

With input 'ab':
Your function should return ['ab', 'ba']

With input 'abc':
Your function should return ['abc','acb','bac','bca','cab','cba']

With input 'aabb':
Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
```
Note: The order of the permutations doesn't matter.

## 💡 Solution

The solution uses recursion to generate permutations by selecting each element in turn and recursively permuting the remaining elements.

### Approach

1. **Base Case**: If the length of the input is 1, return it as the only permutation.
2. **Recursive Case**:
   - For each element in the input, treat it as the first element and recursively generate permutations of the rest of the elements.
   - Combine the first element with each permutation of the rest of the elements.
3. **Remove Duplicates**: Convert the list of permutations to a set and back to a list to remove duplicate permutations.
The function `permutations` generates all unique permutations of the input list or string. If the input is a string, it returns a list of all permutations as strings. If the input is a list, it returns a list of all permutations as lists.

### Code Implementation


```python
def permutations(input):
    
    if len(input) == 1:
        return input if isinstance(input, list) else [input]

    result = []
    for i in range(len(input)):
        first = input[i]
        rest = input[:i] + input[i + 1:]
        rest_permutation = permutations(rest)
        for p in rest_permutation:
            result.append(first + p)
    return list(dict.fromkeys(result))
```

### How It Works

- **Base Case**: If the input has only one element, return it as the only possible permutation.
- **Recursive Case**:
  - Loop through each element of the input.
  - For each element, recursively find permutations of the remaining elements.
  - Concatenate the current element with each permutation of the remaining elements.
- **Removing Duplicates**: Use `dict.fromkeys(result)` to remove duplicate permutations and convert it back to a list.
