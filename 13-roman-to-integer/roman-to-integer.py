class Solution:
    @staticmethod
    def romanToInt(input_string: str) -> int:
        
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
        
        for char in reversed(input_string):
            current_value = symbols_values[char]

            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value

            prev_value = current_value

        return result