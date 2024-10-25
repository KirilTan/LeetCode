# class Solution:
#     @staticmethod
#     def isValid(s: str) -> bool:
#         brackets_count = {
#             'parentheses': 0,
#             'square_brackets': 0,
#             'curly_brackets': 0
#         }
#
#         for bracket in s:
#             if bracket == '(':
#                 brackets_count['parentheses'] += 1
#             elif bracket == ')':
#                 brackets_count['parentheses'] -= 1
#             elif bracket == '[':
#                 brackets_count['square_brackets'] += 1
#             elif bracket == ']':
#                 brackets_count['square_brackets'] -= 1
#             elif bracket == '{':
#                 brackets_count['curly_brackets'] += 1
#             elif bracket == '}':
#                 brackets_count['curly_brackets'] -= 1
#
#         is_balanced = (brackets_count['parentheses'] == 0 and
#                        brackets_count['square_brackets'] == 0 and
#                        brackets_count['curly_brackets'] == 0)
#
#         return is_balanced

class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        # Dictionary to map closing brackets to their corresponding opening brackets
        matching_brackets = {')': '(', ']': '[', '}': '{'}
        stack = []

        for bracket in s:
            # If it's a closing bracket, check for a matching opening bracket at the stack's top
            if bracket in matching_brackets:
                # Pop from stack if it’s not empty; if empty, use a dummy value
                top = stack.pop() if stack else '#'
                if matching_brackets[bracket] != top:
                    return False
            else:
                # If it’s an opening bracket, push onto the stack
                stack.append(bracket)

        # Stack should be empty if all brackets were matched properly
        return not stack
