def centerSomeText(someText):
    totalWidth = 78
    textLen = len(someText)
    totalSpaces = totalWidth - textLen
    
    leftSpaces = totalSpaces // 2
    
    rightSpaces = totalSpaces - leftSpaces
    
    return f"║{" " * leftSpaces}{someText}{" " * rightSpaces}║"

def centerSomeText2(someText):
    totalWidth = 44
    textLen = len(someText)
    totalSpaces = totalWidth - textLen
    
    leftSpaces = totalSpaces // 2
    
    rightSpaces = totalSpaces - leftSpaces
    
    return f"║{" " * leftSpaces}{someText}{" " * rightSpaces}║"

a = f'''╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
{centerSomeText(input("What do you want to center? (78 char max): "))}
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
'''

b = f'''╔════════════════════════════════════════════╗
{centerSomeText2(input("What do you want to center? (42 char max)"))}
╠════════════════════════════════════════════╣
║ 1. Access Workouts                         ║
║ 2. Edit a Workout                          ║
║ 3. Add a Workout                           ║
║ 4. Exit                                    ║
╚════════════════════════════════════════════╝

'''

print(a)

print(b)



'''

═ 	║ 	╒ 	╓ 	╔ 	╕ 	╖ 	╗ 	╘ 	╙ 	╚ 	╛ 	╜ 	╝ 	╞ 	╟
╠ 	╡ 	╢ 	╣ 	╤ 	╥ 	╦ 	╧ 	╨ 	╩ 	╪ 	╫ 	╬ 


'''


