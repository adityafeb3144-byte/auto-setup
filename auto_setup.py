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
try :
    subprocess.run(shlex.split("git init"))
    subprocess.run(shlex.split("git add ."))
except :
    print("Git is not installed in the device")
    permission = input("Do you want to install Git [Y/N] : ")
    if permission.lower() == "y":

        subprocess.run(shlex.split("exception handling is done"))
