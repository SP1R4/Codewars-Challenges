# 😊 Count Smileys

This repository contains a solution to the **Count Smileys** problem, which counts the number of valid smiley faces in a given list of strings.

## 📝 Problem Description

Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

### Example
```
countSmileys([':)', ';(', ';}', ':-D']);
// should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);
// should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']);
// should return 1;
```
## 💡 Solution

The solution iterates over each string in the array and checks whether it matches one of the valid smiley face patterns.

### Approach

1. **Initialize Counters**: Initialize a counter `sum` to keep track of valid smiley faces.
2. **Define Valid Parts**: Define strings for valid eyes, noses, and smiles.
3. **Iterate and Validate**: Loop through the array, checking the length of each string and validating whether it matches a smiley pattern.
4. **Return the Count**: Return the total count of valid smiley faces.

### Code Implementation

```python
def count_smileys(arr):
    sum = 0
    valid_eyes = ':;'
    valid_noses = '-~'
    valid_smiles = ')D'
    
    if not arr:
        return 0
    else:
        for i in range(len(arr)):
            if len(arr[i]) == 2:
                if (arr[i][0] in valid_eyes and arr[i][1] in valid_smiles):
                    sum += 1
            if len(arr[i]) == 3:
                if (arr[i][0] in valid_eyes and arr[i][2] in valid_smiles and arr[i][1] in valid_noses):
                    sum += 1
    return sum
```


### How It Works

- **Initial Setup**: The `count_smileys` function initializes `sum` to zero and defines the valid characters for eyes, noses, and smiles.
- **Validation Process**:
  - For each string in the array:
    - If the string has 2 characters, it checks if the first character is in `valid_eyes` and the second in `valid_smiles`.
    - If the string has 3 characters, it additionally checks if the middle character is in `valid_noses`.
  - If the string matches the criteria, `sum` is incremented.
- **Final Count**: The function returns the total number of valid smiley faces.