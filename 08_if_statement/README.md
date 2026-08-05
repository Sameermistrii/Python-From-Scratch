If-Else Conditional Statements
If-Else Conditional Statements
What are Conditional Statements?
Conditional statements allow you to execute code based on certain conditions.
Python uses if, elif, and else for decision-making.
Syntax:
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition2 is True
else:
    # Code to execute if all conditions are False

Example:
age = 18
 
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")



Match Case Statements in Python
What is Match-Case?
Match-case is a new feature introduced in Python 3.10 for pattern matching.
It simplifies complex conditional logic.
Syntax:
match value:
    case pattern1:
        # Code to execute if value matches pattern1
    case pattern2:
        # Code to execute if value matches pattern2
    case _:
        # Default case (if no patterns match)

Example:
status = 404
 
match status:
    case 200:
        print("Success!")
    case 404:
        print("Not Found")
    case _:
        print("Unknown Status")