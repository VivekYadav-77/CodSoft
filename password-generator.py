import calheading
import random
letters = list("abcdefghijklmnopqrstuvwxyz")
symbols = ['()',"(","%",'@','!','&','+','$','[]','{',"}"]
numbers = ['2','4','7','9','5','3','6','8','1']
print(calheading.logo2)
password = []
z = input("write the  difficulty level of password you want HARD OR EASY: ").lower()
def easy(password,symbols,letters):
    l = int(input("how many letters you want in your password : "))
    for i in range(l):
        L = random.choice(letters)
        password+=L
    n = int(input("how many numbers you want in your password: "))
    for b in range(n):
        N = random.choice(numbers)
        password+=N
    random.shuffle(password)
    gpassword = ""
    for i in password:
        gpassword+=i
    print(f"your password is - \n {gpassword}\n")
def difficult(password,symbols,letters):
    l = int(input("how many letters you want in your password : "))
    for i in range(l):
        L = random.choice(letters)
        password+=L
    s = int(input("how many symbols you want in your password: "))
    for k in range(s):
        S = random.choice(symbols)
        password+=S
    n = int(input("how many numbers you want in your password: "))
    for b in range(n):
        N = random.choice(numbers)
        password+=N
    random.shuffle(password)
    gpassword = ""
    for i in password:
        gpassword+=i
    print(f"your password is - \n {gpassword}\n")
if(z=="hard"):
    difficult(password,symbols,letters)
elif(z=="easy"):
    easy(password,symbols,letters)
else:
    print("invalid input")
    