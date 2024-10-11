def solution(paragraphs, width):
    # Create the top and bottom border
    border = "*" * width
    result = [border]
    
    # Iterate through each paragraph
    for para in paragraphs:
        # Join the words of the paragraph with spaces
        line = " ".join(para)
        
        # If the line is longer than the width, slice it
        if len(line) > width - 2:
            line = line[:width - 2]
        
        # Calculate left and right padding for center alignment
        total_padding = width - 2 - len(line)
        left_padding = total_padding // 2
        right_padding = total_padding - left_padding
        
        # Create the final line with padding and surround with "*"
        formatted_line = "*" + " " * left_padding + line + " " * right_padding + "*"
        result.append(formatted_line)
    
    # Add the bottom border
    result.append(border)
    
    return result

# Example usage:
paragraphs = [["hello", "world"], ["How", "areYou", "doing"], ["Please look", "and aling", "to center"]]
width = 16
output = solution(paragraphs, width)

# Print the result
for line in output:
    print(line)
