#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid. An input string is valid if: Open brackets 
# must be closed by the same type of brackets. Open brackets must be closed in the correct order. 
# Example 1: Input: s = "()" Output: true 
# Example 2: Input: s = "()[]{}" Output: true 
# Example 3: Input: s = "(]" Output: false


def convert(string):
    list1=[]
    list1[:0]=string
    return list1

def characterString(characters:str)->bool:
    charList=convert(characters)
    charDict={
        '(':0,
        ')':0,
        '[':0,
        ']':0,
        '{':0,
        '}':0
    }
    for character in charDict:
        charDict[character]+=1

    if charDict['('] == charDict[')'] or charDict['['] == charDict[']'] or charDict['{'] == charDict['}']:
        return True
    else:
        return False
testChar = '()[]]'
print(characterString(testChar))