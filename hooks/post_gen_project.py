import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", "Initial commit"])

print(f"{MESSAGE_COLOR}Create a virtual environment...{RESET_ALL}")

subprocess.call(["python", "-m", "venv", "venv"])

print(
    f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun! with data{RESET_ALL}"
)
