## Roman to Integer Solution Explanation

This solution efficiently converts a Roman numeral string into its corresponding integer value by following a simple rule-based approach. Below is a step-by-step explanation of the code.

### Code Breakdown:

```python
class Solution:
    @staticmethod
    def romanToInt(input_string: str) -> int:
        # Mapping of Roman numerals to integers
        symbols_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        result = 0
        prev_value = 0

        # Loop through the string in reverse order
        for char in reversed(input_string):
            current_value = symbols_values[char]

            # If current value is less than previous, subtract it
            if current_value < prev_value:
                result -= current_value
            else:
                # Otherwise, add it to the result
                result += current_value

            # Update the previous value
            prev_value = current_value

        return result
```

### Explanation:

#### 1. **Roman Numeral to Integer Mapping**:
```python
symbols_values = {
    'I': 1, 
    'V': 5, 
    'X': 10, 
    'L': 50, 
    'C': 100, 
    'D': 500, 
    'M': 1000
}
```
This dictionary maps Roman numeral symbols to their respective integer values. It is used throughout the code to translate individual Roman characters into their numerical counterparts.

#### 2. **Initial Variables**:
```python
result = 0
prev_value = 0
```
- `result`: Holds the final integer value that corresponds to the Roman numeral string.
- `prev_value`: Keeps track of the last Roman numeral's value during the iteration through the string. This is crucial for handling subtraction cases, like when `I` appears before `V` (e.g., `IV` = 4).

#### 3. **Reversed Looping**:
```python
for char in reversed(input_string):
```
The string is looped in **reverse order**. This approach simplifies handling the subtractive notation in Roman numerals, such as `IV`, `IX`, `XL`, etc.

By going from right to left, the algorithm can easily detect when a smaller value (like `I` or `X`) needs to be subtracted instead of added. This is because, in Roman numerals, smaller values placed before larger ones (e.g., `IV`) indicate subtraction.

#### 4. **Handling Subtraction Rule**:
```python
if current_value < prev_value:
    result -= current_value
else:
    result += current_value
```
Here’s the logic:
- If the current Roman numeral value (`current_value`) is **less** than the previous value (`prev_value`), it means this value should be **subtracted**. This handles cases like `IV`, `IX`, etc.
- Otherwise, the value is **added** to `result`.

For example:
- If the numeral is `IX` (9):
    - `X` is 10, and `I` is 1. Since `I` is smaller than `X`, it is subtracted from 10, yielding `9`.

#### 5. **Updating the Previous Value**:
```python
prev_value = current_value
```
At the end of each iteration, `prev_value` is updated to the current Roman numeral's value. This ensures the next iteration can correctly compare the current character's value to decide whether to add or subtract it.

### Example Walkthrough:

#### Example 1: `input_string = "IX"`
- Start with `result = 0`, `prev_value = 0`
- Loop over the string in reverse:
    - First, `X` (value 10) is added to the result: `result = 10`
    - Next, `I` (value 1) is smaller than `X`, so it is subtracted: `result = 10 - 1 = 9`
- The final result is `9`.

#### Example 2: `input_string = "MCMXCIV"`
- Start with `result = 0`, `prev_value = 0`
- Loop over the string in reverse:
    - `V` (5) is added: `result = 5`
    - `I` (1) is subtracted: `result = 5 - 1 = 4`
    - `C` (100) is added: `result = 4 + 100 = 104`
    - `X` (10) is subtracted: `result = 104 - 10 = 94`
    - `M` (1000) is added: `result = 94 + 1000 = 1094`
    - `C` (100) is subtracted: `result = 1094 - 100 = 994`
    - `M` (1000) is added: `result = 994 + 1000 = 1994`
- The final result is `1994`.

### Time and Space Complexity:

- **Time Complexity**:  
  The time complexity is **O(n)**, where `n` is the length of the input string. The code loops through the string once, making it linear in time complexity.

- **Space Complexity**:  
  The space complexity is **O(1)** because we are using only a fixed amount of extra space (the dictionary and a few variables) regardless of the input size.

This approach is efficient and easily handles standard Roman numeral rules!