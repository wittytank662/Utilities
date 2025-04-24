def centerSomeText(someText):
    textLen = len(someText)
    numOfSpaces = int((78-textLen)/2)
    
    return f"*{" "*numOfSpaces}{someText}{" "*numOfSpaces}*"

a = f'''********************************************************************************
*                                                                              *
{centerSomeText("someText1")}
*                                                                              *
********************************************************************************
'''

print(a)