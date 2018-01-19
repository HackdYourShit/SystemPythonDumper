import os


print("Welcome to the Python System Dumper by iSn0w and JohnVS!")
print("Soooo i think we'll have to say this ...")
print("this is made for learning 'how-to-do-it' only, and not for any bad things...")
print("first of all , please tell us your Operating system!")
print("Right now, we are mainly working on Linux, Windows and MacOS will maybe come later !")
OSC = input("macOS/Windows/Linux \n")
if OSC =="Linux":
    print("you've choosen Linux")
    print("please tell us the path")
    inspath = input("Path: ")
for root, dirs, files in os.walk(inspath):  
    for filename in files:
        print(filename)
