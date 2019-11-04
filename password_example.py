print("What is your password?")

password = input()
counter = 0

while password != "swordfish":
    print("Wrong Password")
    counter = counter + 1
    password = input()
    if counter == 4:
        print("Too many attempts")
        break

if password == "swordfish":
    print("Access granted")

