test_text = """''' 
This is a comment block 
Multiple lines 
''' 
x = "hello"  # this is a comment 
y = 'world' 
print(x + " " + y) 
''' 
Another comment block 
''' 
z = "python" 
""" 

def format_code_blocks(text):
    # Split the text into lines
    lines = text.splitlines()
    
    # Initialize variables to track code blocks
    in_code_block = False
    formatted_lines = []
    
    for line in lines:
        stripped_line = line.strip()
        
        # Check for the start of a code block
        if stripped_line.startswith("'''") and not in_code_block:
            in_code_block = True
            formatted_lines.append("'''")
            continue
        
        # Check for the end of a code block
        if stripped_line.endswith("'''") and in_code_block:
            in_code_block = False
            formatted_lines.append("'''")
            continue
        
        # If inside a code block, add the line as is
        if in_code_block:
            formatted_lines.append(line)
        else:
            # If outside a code block, add the line as is
            formatted_lines.append(line)
    
    return "\n".join(formatted_lines)

print(format_code_blocks(test_text))