import os
import subprocess
import shlex

name_dirt = input("Enter a Directory name : ")

os.mkdir(f"{name_dirt}")

data = open(f"{name_dirt}/solution.py","w")
data.close()

os.chdir(f"{name_dirt}")
import subprocess
subprocess.run(shlex.split("git init"))
subprocess.run(shlex.split("git add ."))