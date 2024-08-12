# 🔢 Next Smaller Number

This code provides a function `next_smaller_number` that finds the largest number smaller than a given number by rearranging its digits. If no such number exists, it returns `-1`.

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


## 📜 Code Implementation

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// A utility function to swap two characters
void swap(char* a, char* b) {
    char temp = *a;
    *a = *b;
    *b = temp;
}

// Comparator function to sort in descending order
int desc(const void* a, const void* b) {
    return (*(char*)b - *(char*)a);
}

long long next_smaller_number(unsigned long long n) {
    // Convert the number to a string
    char numStr[21]; // enough to store a long long number
    sprintf(numStr, "%llu", n);
    int len = strlen(numStr);

    // Traverse the number from right to left
    for (int i = len - 1; i > 0; i--) {
        // Find the first digit that is larger than the digit next to it
        if (numStr[i] < numStr[i - 1]) {
            // Find the largest digit to the right of numStr[i-1] and smaller than numStr[i-1]
            int maxIndex = i;
            for (int j = i + 1; j < len; j++) {
                if (numStr[j] < numStr[i - 1] && numStr[j] > numStr[maxIndex]) {
                    maxIndex = j;
                }
            }

            // Swap the found digits
            swap(&numStr[i - 1], &numStr[maxIndex]);

            // Sort the digits after (i-1) in descending order
            qsort(numStr + i, len - i, sizeof(char), desc);

            // Convert back to long long
            long long result = atoll(numStr);

            // Ensure the result is valid (i.e., no leading zeros)
            if (numStr[0] == '0') {
                return -1;
            }
            return result;
        }
    }
    return -1; // Return -1 if no smaller number is possible
}
```

## 🛠️ Explanation

1. **Convert the Number to a String**: The number is converted to a string for easier manipulation of its digits.

2. **Find the Rightmost Decreasing Digit**: Traverse the number from right to left to locate the first digit that is smaller than the digit next to it.

3. **Find the Largest Smaller Digit**: Identify the largest digit to the right of the found digit that is smaller than it.

4. **Swap and Sort**: Swap the identified digits and sort the remaining digits in descending order.

5. **Convert Back and Validate**: Convert the string back to a number and ensure it does not start with a zero.

6. **Return Result**: Return the result if valid; otherwise, return `-1` if no smaller number is possible.
