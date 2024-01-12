import os
import re
import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"


def is_valid_string(s):
    pattern = r"^[a-zA-Z_-]+$"
    if re.match(pattern, s):
        return True
    else:
        return False


if not is_valid_string(project_slug):
    print(
        f"{ERROR_COLOR}ERROR: {project_slug=} is not a valid name for a project.{RESET_ALL}"
    )
    sys.exit(1)
else:
    print(f"{MESSAGE_COLOR}Valid project name!{RESET_ALL}\n\n")

print(f"Creating project at {os.getcwd()}")
print(f"{MESSAGE_COLOR}Let's do it! You're are going to create something awesome!")
