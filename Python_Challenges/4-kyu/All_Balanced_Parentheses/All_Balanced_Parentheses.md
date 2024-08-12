# 🧩 Balanced Parentheses

This repository contains a solution to the **Balanced Parentheses** problem, which generates all combinations of `n` pairs of balanced parentheses.

## 📝 Problem Description

Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses

### Example

```
balanced_parens(0) => [""]
balanced_parens(1) => ["()"]
balanced_parens(2) => ["()()","(())"]
balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]
```

## 💡 Solution

The solution uses a recursive backtracking approach to generate all possible combinations of `n` pairs of balanced parentheses.

### Approach

1. **Recursive Function**: The main function `generateParenthesisUtil` is a recursive helper that builds valid parentheses combinations by tracking the number of opening and closing parentheses left to be added.

2. **Base Case**: When both `left` and `right` counters reach zero, a valid combination is formed and added to the result list.

3. **Backtracking**:
   - If there are still opening parentheses left (`left > 0`), we can add an opening parenthesis `(`.
   - If the number of closing parentheses left (`right`) is greater than the number of opening parentheses (`left`), we can add a closing parenthesis `)`.

### Code Implementation

```python
def balanced_parens(n):
    
    def generateParenthesis(n):
        result = []
        generateParenthesisUtil(n, n, "", result)
        return result
    
    def generateParenthesisUtil(left, right, temp, result):
        if left == 0 and right == 0:
            result.append(temp)
            return
        if left > 0:
            generateParenthesisUtil(left - 1, right, temp + '(', result)
        if right > left:
            generateParenthesisUtil(left, right - 1, temp + ')', result)
    
    return generateParenthesis(n)
```

### How It Works

- **Initial Call**: The `balanced_parens(n)` function initiates the process by calling `generateParenthesis(n)`.
- **Recursive Generation**: The `generateParenthesisUtil` function is used to generate all valid combinations by making decisions at each step:
  - Add an opening parenthesis `(` if we still have left parentheses to add.
  - Add a closing parenthesis `)` if the number of right parentheses remaining is greater than the left parentheses remaining.
- **Result**: The final result is a list of all valid combinations of `n` pairs of balanced parentheses.
