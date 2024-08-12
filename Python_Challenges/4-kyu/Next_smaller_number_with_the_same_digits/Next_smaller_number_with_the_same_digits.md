# 🔢 Next smaller number with the same digits

This repository contains a solution to the **Next smaller number with the same digits** problem, which finds the largest number smaller than the given number that can be formed by rearranging its digits.

## 📝 Problem Description

Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

### For example
```
next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
```
Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

```
next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
```

## 💡 Solution

The solution involves the following steps:

1. **Convert to List**: Convert the number into a list of digits.
2. **Find Swap Position**: Identify the position to swap to get the next smaller number.
3. **Find Smallest Larger Digit**: Find the largest digit smaller than the identified digit.
4. **Rearrange Digits**: Rearrange the digits to form the largest possible number smaller than the original.
5. **Handle Edge Cases**: Handle cases where no smaller number can be formed.

### Code Implementation

```python
def next_smaller(n):
    num = [int(i) for i in str(n)]
    next_smallest = float("-inf")
    nsc = float("-inf")
    pos = len(num) - 1
    
    if (len(num) == 1 or num == sorted(num)):
        return -1
        
    for i in range(len(num) - 1, 0, -1):
        if num[i] < num[i - 1]:
            pos -= 1
            break
        pos -= 1
    
    for i in range(pos, len(num)):
        if (num[i] < num[pos] and num[i] > next_smallest):
            next_smallest = num[i]
            nsc = i
    
    num[pos], num[nsc] = num[nsc], num[pos]
    num2 = num[pos + 1:]
    num2.sort(reverse=True)
    
    for i in range(len(num2)):
        num[i + pos + 1] = num2[i]
        
    num = [str(x) for x in num]
    s = "".join(num)
    
    return int(s) if s[0] != '0' else -1
```

### How It Works

- **Initial Setup**: Convert the number `n` into a list of its digits.
- **Identify Swap Position**:
  - Find the rightmost position where a digit is smaller than the digit immediately before it.
  - This is the digit to be swapped to create a smaller number.
- **Find Smallest Larger Digit**:
  - From the digits to the right of the identified position, find the largest digit smaller than the identified digit.
- **Rearrange Digits**:
  - Swap the identified digit with the smallest larger digit found.
  - Sort the remaining digits to form the largest possible number smaller than the original.
- **Return Result**:
  - Convert the list of digits back to a number and handle cases where the number might start with zero.
