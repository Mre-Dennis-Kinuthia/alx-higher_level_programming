#!/usr/bin/env python3.8
# Import the compiled module
import hidden_4.pcy

# Get a list of all the names defined in the module
names = dir(hidden_4)

# Sort the names in alphabetical order
names.sort()

# Print the names, one per line
for name in names:
    # Only print names that do not start with __
    if not name.startswith("__"):
        print(name)
