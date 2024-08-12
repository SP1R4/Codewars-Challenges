# 🔢 Possible number combos

This repository contains a solution to the **Possible number combos** problem. The function `combos` generates all unique combinations of integers that sum up to a given number.

## 📝 Problem Description

Jon and Joe have received equal marks in the school examination. But, they won't reconcile in peace when equated with each other. To prove his might, Jon challenges Joe to write a program to find all possible number combos that sum to a given number. While unsure whether he would be able to accomplish this feat or not, Joe accpets the challenge. Being Joe's friend, your task is to help him out.

Task
Create a function combos, that accepts a single positive integer num (30 > num > 0) and returns an array of arrays of positive integers that sum to num.

## Notes
-Sub-arrays may or may not have their elements sorted.
-The order of sub-arrays inside the main array does not matter.
-For an optimal solution, the following operation should complete within 6000ms.
### Example

```
combos(3) => [ [ 3 ], [ 1, 1, 1 ], [ 1, 2 ] ]
combos(10) => [ [ 10 ],
  [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 2 ],
    [ 1, 1, 1, 1, 1, 1, 1, 3 ],
    [ 1, 1, 1, 1, 1, 1, 4 ],
    [ 1, 1, 1, 1, 1, 5 ],
    [ 1, 1, 1, 1, 6 ],
    [ 1, 1, 1, 7 ],
    [ 1, 1, 8 ],
    [ 1, 9 ],
    [ 1, 1, 1, 1, 1, 1, 2, 2 ],
    [ 1, 1, 1, 1, 1, 2, 3 ],
    [ 1, 1, 1, 1, 2, 4 ],
    [ 1, 1, 1, 1, 2, 2, 2 ],
    [ 1, 1, 1, 1, 3, 3 ],
    [ 1, 1, 1, 2, 5 ],
    [ 1, 1, 1, 2, 2, 3 ],
    [ 1, 1, 1, 3, 4 ],
    [ 1, 1, 2, 6 ],
    [ 1, 1, 2, 2, 4 ],
    [ 1, 1, 2, 2, 2, 2 ],
    [ 1, 1, 2, 3, 3 ],
    [ 1, 1, 3, 5 ],
    [ 1, 1, 4, 4 ],
    [ 1, 2, 7 ],
    [ 1, 2, 2, 5 ],
    [ 1, 2, 2, 2, 3 ],
    [ 1, 2, 3, 4 ],
    [ 1, 3, 6 ],
    [ 1, 3, 3, 3 ],
    [ 1, 4, 5 ],
    [ 2, 8 ],
    [ 2, 2, 6 ],
    [ 2, 2, 2, 4 ],
    [ 2, 2, 2, 2, 2 ],
    [ 2, 2, 3, 3 ],
    [ 2, 3, 5 ],
    [ 2, 4, 4 ],
    [ 3, 7 ],
    [ 3, 3, 4 ],
    [ 4, 6 ],
    [ 5, 5 ] ]
```

## 💡 Solution

The solution involves using a recursive approach with memoization to generate all possible combinations that sum up to the target number. The results are stored in a memoization dictionary to avoid redundant computations.

### Approach

1. **Initialize Memoization**:
   - Use a dictionary `memo` to store previously computed results.
2. **Generate Combinations**:
   - For each integer from 1 to the target number, recursively compute combinations for the remaining target.
   - Combine these with the current integer and ensure uniqueness by sorting and checking.
3. **Store and Return**:
   - Store the results in the `memo` dictionary to optimize future computations and return the results.

### Code Implementation

```python
def combos(num):
    memo = {}

    def generate_combinations(target):
        if target in memo:
            return memo[target]

        if target == 0:
            return [[]]

        if target < 0:
            return None

        result = []
        for i in range(1, target + 1):
            sub_combos = generate_combinations(target - i)
            if sub_combos is not None:
                for combo in sub_combos:
                    new_combo = [i] + combo
                    new_combo.sort()
                    if new_combo not in result:
                        result.append(new_combo)

        memo[target] = result
        return result

    return generate_combinations(num)
```

### How It Works

- **Memoization**:
  - The `memo` dictionary is used to store results of previously computed targets to avoid redundant calculations.
- **Recursive Combination Generation**:
  - The function `generate_combinations` recursively computes all combinations for a reduced target.
  - Each combination is constructed by adding the current integer and is sorted to ensure uniqueness.
- **Optimization**:
  - Use of sorting and checking ensures that only unique combinations are added to the result.
