import re

password = input("Enter your password: ")
while True:
    
    flag = 0

    if len(password) >= 8:
        flag = flag + 1
    if re.search(r"[$%@_!]",password):
        flag += 1
    if re.search(r"[A-Z]",password):
        flag += 1
    if re.search(r"[a-z]",password):
        flag += 1
    if re.search(r"[0-9]",password):
        flag += 1
    
    if flag == 5:
        print("password changed successfully")
        break
    else:
        print("wrong password")
        print("Enter your password again:")