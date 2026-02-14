Project Automator 🚀
A Python-based utility script designed to streamline the initial setup of new coding projects. With a single command, it creates a structured environment and initializes version control.

🛠 Features
Automatic Directory Creation: Prompts for a project name and builds the folder instantly.

Boilerplate Generation: Automatically creates a solution.py file so you can start coding immediately.

Git Integration: Initializes a new Git repository and stages your initial files automatically.

🚀 How to Use
1. Prerequisites
Ensure you have Python 3.x and Git installed on your system.

2. Running the Script
Open your terminal or command prompt.

Navigate to the folder where auto_setup.py is located.

Run the script using:

Bash
python auto_setup.py
Enter your desired project name when prompted.

📂 Project Structure
After running the script, your new project directory will look like this:

Plaintext
[Your Project Name]/
├── .git/            # Initialized Git repository
└── solution.py      # Your main Python script
📝 Code Overview
The script utilizes the following Python modules:

os: To handle directory creation and navigation.

subprocess: To execute Git commands directly from the script.

shlex: To safely split command strings for the shell.

💡 Future Improvements
Add a .gitignore file automatically.

Allow the user to choose between different file templates (e.g., .js, .cpp).

Add error handling for cases where a directory already exists.
