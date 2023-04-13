print("hello world")

name =input("enter your name: ")
time = float(input("Enter the current time: "))

if (time<=12):
    print("Good Morning",name)
elif(time<=16):
    print("Very good afternoon",name)
elif(time<=20):
    print("very good evening",name)
else:
    print("Good night",name)