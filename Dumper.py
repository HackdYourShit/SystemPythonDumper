import os
import shutil 
import time
import zipfile
import sys
import subprocess

try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use Python 3 or newer")

color.write("This tool was made by iSn0w and JohnVS!","KEYWORD")
print("Soooo i think we'll have to say this ...")
print("this is made for learning 'how-to-do-it' only, and not for any bad things...")
print("first of all , please tell us your Operating system!")
print("Right now, we are mainly working on Linux, Windows and MacOS will maybe come later !")
startscr = input("type in start or help \n")
if startscr == "help":
    print("this is the help menu")
    print("For making folders writable , start up the system Terminal and type in:")
    print("Sudo CHMOD +X <Folder-Name>")
elif startscr == "start":
    
    OSC = input("macOS/Windows/Linux \n")
    if OSC =="Win":
            inspath = input()
            subprocess.Popen('explorer "C:'+inspath+'"')
    if OSC =="Linux":
        print("you've choosen Linux")
        inspath = input("specify the target directory: ")
        dirlist = os.listdir(inspath)
        from pprint import pprint
        pprint(dirlist)
    if os.access(inspath, os.W_OK) is not True:
            print("Folder not writable, for a tutorial how to make it dumpable type in help when starting up the script")
    else :
            os.system('start "C:\'' + inspath +'"')
            print("Folder writable! got full access to it")
            print("now you are able to run some commands ! type in 'help' for a full list !")
            navi = input()
            if navi == "help":
                print("Copy <File>     Copies a file to the clipboard")
                print("Paste           Pastes a file from the clipboard")
                print("Dump            brings you into the dumping menu")
                print("cd              jumps in or out a folder")
     
                   
    
