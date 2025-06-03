def centerSomeText(someText):
    totalWidth = 78
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

print(a)



'''

═ 	║ 	╒ 	╓ 	╔ 	╕ 	╖ 	╗ 	╘ 	╙ 	╚ 	╛ 	╜ 	╝ 	╞ 	╟
╠ 	╡ 	╢ 	╣ 	╤ 	╥ 	╦ 	╧ 	╨ 	╩ 	╪ 	╫ 	╬ 


'''