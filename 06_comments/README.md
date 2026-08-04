Comments, Escape Sequences & Print Statement
Comments
Comments are used to explain code and are ignored by the Python interpreter.
Single-line comments start with #.
Multi-line comments are enclosed in ''' or """.
# This is a single-line comment
'''
This is a
multi-line comment
'''

Escape Sequences
Escape sequences are used to include special characters in strings.
Common escape sequences:
\n: Newline
\t: Tab
\\: Backslash
\": Double quote
\': Single quote
Example:
print("Hello\nWorld!")
print("This is a tab\tcharacter.")

Print Statement
The print() function is used to display output.
You can use sep and end parameters to customize the output.
print("Hello", "World", sep=", ", end="!\n")