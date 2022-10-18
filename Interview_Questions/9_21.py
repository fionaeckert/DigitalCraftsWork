# Given a string consisting of 0-9,
#     find the string that is created using
#     a standard phone keypad
#     | 1        | 2 (abc) | 3 (def)  |
#     | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
#     | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
#     |     *    | 0 ( )   |     #    |
#     You can ignore 1, and 0 corresponds to space
#     >>> keypad_string("12345")
#     'adgj'
#     >>> keypad_string("4433555555666")
#     'hello'
#     >>> keypad_string("2022")
#     'a b'
#     >>> keypad_string("")
#     ''
#     >>> keypad_string("111")
#     ''
#     '''

numberString = '234'

def keypadString(numberString)->list:
    numberDict = {"2":"a","22":"b","222":"c",
                "3":"d","33":"e","333":"f",
                "4":"g","44":"h","444":"i",
                "5":"j","55":"k","555":"l",
                "6":"m","66":"n","666":"o",
                "7":"p","77":"q","777":"r","7777":"s",
                "8":"t","88":"u","888":"v",
                "9":"w","99":"x","999":"y","9999":"z", "0":" "}
    wordReturned = []
    for b in range(len(numberString)):
        for c in range(b + 1,len(numberString)):
            for d in range(b + 2,len(numberString)):
                for e in range(b + 3, len(numberString)): 
                    if(numberString[b] == numberString[c] == numberString[d] == numberString[e]):
                        wordReturned.append(numberDict.get(numberString[b]+numberString[c]+numberString[d]+numberString[e]))    
                    break
    for y in range(len(numberString)):
        for z in range(y + 1,len(numberString)):
            for a in range(y + 2,len(numberString)):
                if(numberString[y] == numberString[z] == numberString[a]):
                    wordReturned.append(numberDict.get(numberString[y]+numberString[z]+numberString[a]))
                    break
    for x in range(len(numberString)):
        for i in range(x + 1,len(numberString)):
            if(numberString[x] == numberString[i]):
                wordReturned.append(numberDict.get(numberString[x]+numberString[i]))
                break
    for f in range(len(numberString)):
        for g in range(f+1,len(numberString)):
            if(numberString[f]!=numberString[g]):
                wordReturned.append(numberDict.get(numberString[f]))
                wordReturned.append(numberDict.get(numberString[g]))
    print(wordReturned)
keypadString(numberString)