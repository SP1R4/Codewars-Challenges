# 🔢 Prime Factors

This repository contains a solution to the **Prime Factors** problem, which computes the prime factors of a given integer.

## 📝 Problem Description

Inspired by one of Uncle Bob's TDD Kata

Write a function that generates factors for a given number.

The function takes an integer as parameter and returns a list of integers (ObjC: array of NSNumbers representing integers). That list contains the prime factors in numerical sequence.

### Example

```
1  ==>  []
3  ==>  [3]
8  ==>  [2, 2, 2]
9  ==>  [3, 3]
12 ==>  [2, 2, 3]
```

## 💡 Solution

The solution uses a straightforward approach to find prime factors by dividing the number by the smallest possible prime and accumulating the factors.

### Approach

1. **Initialize Variables**: Start with the smallest prime number, `2`.
2. **Factorization Loop**:
   - While the number `n` is not reduced to `1`, check if `n` is divisible by the current prime number `x`.
   - If divisible, divide `n` by `x` and append `x` to the result list.
   - If not divisible, increment `x` to test the next potential factor.
3. **Return Result**: The list of factors collected is returned.

### Code Implementation

```python
def prime_factors(n):
    result = []
    x = 2
    while n != 1:
        if n % x == 0:
            n = n // x
            result.append(x)
        else:
            x += 1
    return result
```

### How It Works

- **Initial Setup**: Start with the smallest prime number (`2`).
- **Factorization Process**:
  - Check if `n` is divisible by `x`. If so, divide `n` by `x` and add `x` to the result list.
  - If not, move to the next integer value for `x`.
- **Completion**: Continue until `n` is reduced to `1`.
