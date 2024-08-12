# 🔢 parseInt() reloaded

This repository contains a solution to the **parseInt() reloaded** problem, which converts a string representing a number in words into its corresponding integer value.

## 📝 Problem Description

In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them

## 💡 Solution

The solution involves parsing the string, converting words to their corresponding numeric values, and handling different magnitudes such as hundreds, thousands, and millions.

### Approach

1. **Define Word Mappings**: Create a dictionary that maps number words to their integer values.
2. **Parse String**: Replace hyphens with spaces and split the string into tokens.
3. **Process Tokens**:
   - Convert number words to integers using the dictionary.
   - Handle special tokens like "hundred", "thousand", and "million" to adjust the numeric value accordingly.
4. **Calculate Result**: Sum up the values to get the final integer result.

### Code Implementation

```python
def parse_int(string):
    ONES = {'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten': 10,
            'eleven': 11,
            'twelve': 12,
            'thirteen': 13,
            'fourteen': 14,
            'fifteen': 15,
            'sixteen': 16,
            'seventeen': 17,
            'eighteen': 18,
            'nineteen': 19,
            'twenty': 20,
            'thirty': 30,
            'forty': 40,
            'fifty': 50,
            'sixty': 60,
            'seventy': 70,
            'eighty': 80,
            'ninety': 90,
              }

    numbers = []
    for token in string.replace('-', ' ').split(' '):
        if token in ONES:
            numbers.append(ONES[token])
        elif token == 'hundred':
            numbers[-1] *= 100
        elif token == 'thousand':
            numbers = [x * 1000 for x in numbers]
        elif token == 'million':
            numbers = [x * 1000000 for x in numbers]
    return sum(numbers)
```

### How It Works

- **Initial Setup**: The `ONES` dictionary maps English words to their corresponding numeric values.
- **Token Processing**:
  - Replace hyphens with spaces and split the string into individual tokens.
  - Convert each token to its numeric value using the dictionary.
  - Handle magnitude words ("hundred", "thousand", "million") to adjust the numeric values accordingly.
- **Calculate and Return**:
  - Use a list to accumulate numbers and apply magnitude multipliers.
  - Sum up all values to get the final integer result.
