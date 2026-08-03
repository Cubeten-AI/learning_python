#reading writing to the txt file
# Step 1: Open in append and read mode
with open("tr6gyf.txt", "a+") as file:
    # Move cursor to the beginning to read existing content
    file.seek(0)
    content = file.read()
    print("--- Here are the Content ---")
    print(content)
    
    # Write new lines to the end of the file
    file.write("\nHello, World!\n")
    file.write("This is a new line of text.\n")

# Step 2: Open again in read-only mode to verify the changes
with open("tr6gyf.txt", "r") as file:
    lines = file.readlines()
    print("--- Updated Lines List ---")
    print(lines)
