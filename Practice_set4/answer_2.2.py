""" Both Length and Width """
def calculate_area(length, width):
    return length*width

print(calculate_area(3,4))
""" Only Length  """

def calculate_area(length, width=10):
    return length*width
    
print(calculate_area(7))