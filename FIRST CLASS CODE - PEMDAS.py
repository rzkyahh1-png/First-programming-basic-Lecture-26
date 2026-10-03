#First Class Programming Basic

print("Hello world")

pi = 3.14159
radius = 2.2

area = pi * (radius**2)
print (area)

radius = radius + 1
area = pi * (radius**2)
print (area)

area = pi * (radius**2)
radius = radius + 1
print(radius)

hi = "Hello there"
name = " I'm Kiya"
intro = hi + name 
print(intro)

x = 4
print(x)
x_str = str (x) 
print("my fav number is", x, "." , "x =" , x)

b = x_str + x_str
print(b)

#input value 
text = input ("Enter your word")
print(5*text)

number = int(input("enter your number"))
total = number + number
print(total)

# if else code 
x = float(input("Input your score"))
y = 8
if x>y :
    print("yeayy you're passed the test")
elif x<y:
    print("Try again, gammbatte")
print("Thank youu")


#Remainder code 
num = int(input("input your number"))
if num % 2 == 0:
    print("yeaa, your number is even")
else:
    print("yeayy your number is odd")

#While loops code
n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
while n == "right" or n == "Right":
    n = input("You are in the Lost Forest\n****************\n******       ***\n  (â•¯Â°â–¡Â°ï¼‰â•¯ï¸µ â”»â”â”»\n****************\n****************\nGo left or right? ")
print("\nYou got out of the Lost Forest!\n\o/")


n = 0
while n < 5:
    print(n)
    n = n+1