class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping_dict ={ ')':'(',
                        '}':'{',
                        ']':'['
                         }
        
        # iterate through the chars in input string
        for char in s:
            # if char is in mapping dict
            if char in mapping_dict:
                #check if stack peek contains the mapped start of parenthesis
                if stack and stack[-1] == mapping_dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack