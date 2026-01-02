import random 

# to get a random number in between certain range such that a <= number <= b
num = random.randint(1, 3)
print(f"Random Number : {num}")

# this give a floating point in range (0 to 1.0)
print(random.random())

# returns a random floating between 1 to 10
print(random.uniform(1, 10))

############### MODULES ##################
# 🔹 Module

# A module is a single Python file (.py) that contains:

# Functions
# Variables
# Classes
# It helps you organize code and reuse it across programs.

############### LIBRARIES #################
# 🔹 Library

# A library is a collection of related modules bundled together to solve a broader problem.

# 📁 Folder (library) → 📄 multiple files (modules)

# Examples:
# NumPy → numerical computing
# Pandas → data analysis
# Matplotlib → data visualization
# TensorFlow → machine learning