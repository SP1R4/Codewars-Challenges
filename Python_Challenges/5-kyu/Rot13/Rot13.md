# 🔄 ROT13 Cipher

This repository contains a solution to the **ROT13 Cipher** problem, which implements the ROT13 encryption algorithm. ROT13 is a special case of the Caesar cipher that shifts each letter by 13 places in the alphabet.

## 📝 Problem Description

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.

## 💡 Solution

The solution involves creating a translation table that maps each letter to its ROT13 counterpart and applying this transformation to each character in the input string.

### Approach

1. **Create Translation Table**:
   - Define the alphabet in both uppercase and lowercase.
   - Create a translation string that maps each letter to its ROT13 equivalent.
2. **Translate Characters**:
   - For each character in the input message, use the translation table to find its ROT13 counterpart.
   - If the character is not in the translation table, it remains unchanged.
3. **Combine Results**:
   - Join all transformed characters into a single string and return it.

### Code Implementation

```python
def rot13(message):
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    trans = chars[26:]+chars[:26]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c) > -1 else c
    return ''.join(rot_char(c) for c in message)
```

### How It Works

- **Translation Table**:
  - The `chars` string contains all uppercase and lowercase letters.
  - The `trans` string is a rotated version of `chars` by 13 positions, providing the ROT13 mappings.
- **Character Transformation**:
  - The `rot_char` lambda function finds the index of each character in `chars` and maps it to the corresponding character in `trans`.
- **Result Construction**:
  - Use `''.join()` to concatenate all transformed characters into the final string.
