import os
import subprocess
import shlex

while True:
    name_dirt = input("Enter a Directory name : ")
    try :
        os.mkdir(f"{name_dirt}")
        break
    except FileExistsError :
        print("Directory already exists ")
        print("Please try again")
        
data = open(f"{name_dirt}/solution.py","w")
data.close()

os.chdir(f"{name_dirt}")
while True:
    try :
        subprocess.run(shlex.split("git init"))
        subprocess.run(shlex.split("git add ."))
        break
    except :
        print("Git is not installed in the device")
        permission = input("Do you want to install Git [Y/N] : ")
        if permission.lower() == "y":
            device = input("Enter your input for device \nWindows : W\nmacOS : M\nLinux : N")
            if device.lower() == "w":
                subprocess.run(shlex.split("winget install --id Git.Git -e --source winget"))
            elif device.lower() == "m":
                subprocess.run(shlex.split("brew install git"))
            else:
                subprocess.run(shlex.split("sudo apt-get update"))
                subprocess.run(shlex.split("sudo apt-get install git"))
