import re

def execute_rolvin(code):
    lines = code.strip().split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("rolvin "):
            content = re.match(r'rolvin "(.*)"', line)
            if content:
                print(content.group(1))
            else:
                print("Syntax Error: Use rolvin \"message\"")
        else:
            print("Unknown Command: ", line)

# Example Usage
code = """
rolvin "Hahaha"
"""
execute_rolvin(code)
