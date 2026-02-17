🚀 Git Project Initializer Script

A Python automation script that:

Creates a new directory

Generates a solution.py file inside it

Initializes a Git repository

Automatically stages all files

Installs Git (if not already installed)

📌 What This Script Does

Prompts the user to enter a directory name

Creates the directory (if it doesn’t already exist)

Creates an empty solution.py file inside it

Checks if Git is installed

If Git is installed:

Runs git init

Runs git add .

If Git is NOT installed:

Asks for permission to install

Installs Git depending on OS:

Windows (winget)

macOS (brew)

Linux (apt)

🛠 Technologies Used

Python

os module

subprocess module

shlex module

shutil module

Git
