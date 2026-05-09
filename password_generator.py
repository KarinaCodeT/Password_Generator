import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%"
length = int(input("Password length: "))
password = ""
for i in range(length):
    password += random.choice(letters)
print("Generated password:", password)
