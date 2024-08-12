# 🎨 RGB to Hex Conversion

This repository contains a solution to the **RGB to Hex Conversion** problem, which converts RGB color values into their corresponding hexadecimal color code.

## 📝 Problem Description
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

### Examples (input --> output):
```
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
```

## 💡 Solution

The solution involves clamping the RGB values to ensure they are within the valid range, converting these values to a hexadecimal string, and then formatting the string in uppercase.

### Approach

1. **Clamping Values**:
   - Use a helper function to ensure that each RGB value is within the valid range (`0` to `255`).
2. **Hexadecimal Conversion**:
   - Convert the clamped RGB values to a hexadecimal format.
   - Ensure that each color component is represented by exactly two hexadecimal digits.
3. **Formatting**:
   - Convert the hexadecimal string to uppercase.

### Code Implementation

```python
def rgb(r, g, b):
    # helper function
    def help(c):
        if c < 0: return 0
        if c > 255: return 255
        return c
    
    # make sure that values are within bounds
    r = help(r)
    g = help(g)
    b = help(b)
    
    # convert to hex
    # maintain 2 spaces each
    val = "%02x%02x%02x" % (r, g, b)
    
    # return UpperCase string
    return val.upper()
```

### How It Works

- **Value Clamping**:
  - The `help` function ensures that each RGB value is within the valid range.
- **Hexadecimal Conversion**:
  - Convert each RGB value to a two-digit hexadecimal string and concatenate them.
- **Formatting**:
  - Convert the final hex string to uppercase to match the expected output format.
