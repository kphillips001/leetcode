# use a stack & loop through all characters (stack must be empty at the very end)
# push open brackets and pop close brackets
# close bracket must match open bracket
# how to know if open or close bracket? Need a list of brackets. Check if item is in that list. 
# Can wrap characters in a set. Can use list also. If char in open brackets, add to stack. 
# How to figure which brackets are matching (open/close)? Can use a dictionary with key value pair. 
# if char not in dict: add to stack
class Solution:
    def isValid(self, s: str) -> bool:
        close_brackets = {
            ')' : '(', 
            '}' : '{',
            ']' : '['
        }
 
        stack = []
         # for each char in s:
        for char in s
            # if char in close_bracket_dict
            if char in close_brackets
                # try to pop the stack
                # if the top of the stack doesn't match the close bracket                     # OR if the stack is empty
                if len(stack) == 0 or stack[-1] != close_brackets[char]    
                    return false
                else: 
                    stack.pop()    
            # if chart is NOT in close_bracket_dict:
            else:
                # add the bracket onto the stack
                stack.append(char)
        # check if the stack is not empty
        if len(stack) > 0: 
            return False
        # otherwise return true
        return True