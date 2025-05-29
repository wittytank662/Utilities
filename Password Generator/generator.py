import random

chars = open("characters.txt", "r")

charList = [line.strip() for line in chars.readlines()]

length = int(input("How long do you want your password to be? (reccomended length: 16) "))

password = ""

count = 0

while count != length:
    index = random.randrange(0, len(charList))
    password = password + charList[index]
    count += 1
    
chars.close()

print(password)