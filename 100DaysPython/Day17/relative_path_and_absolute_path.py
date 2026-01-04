# Absolute Path
# - A fixed path from the file system root to the file
# - Independent of the current working directory
# - Safest option for file access in real projects
# - BASE_DIR = os.path.dirname(__file__)  → directory of the current Python file

# Relative Path
# - Resolved relative to the current working directory (os.getcwd())
# - "./" refers to the directory from which the script is executed
# - Can break if the program is run from a different location
# - Suitable only for quick scripts or controlled environments
