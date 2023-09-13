import os

def print_directory_tree(path, indent='', is_last=True):
    # Get the current directory or file name
    base_name = os.path.basename(path)

    # Determine the icon based on whether it's a directory or file
    icon = '📂' if os.path.isdir(path) else '📄'

    # Display the directory or file name with bold formatting
    tree_structure = f"{indent}{'' if is_last else '|'}-- {icon} {base_name}\n"

    if os.path.isdir(path):
        # List all items in the directory
        items = os.listdir(path)

        # Sort the items alphabetically
        items.sort()

        # Filter directories and files
        dirs = [item for item in items if os.path.isdir(os.path.join(path, item))]
        files = [item for item in items if os.path.isfile(os.path.join(path, item))]

        # Traverse subdirectories
        for i, dir_name in enumerate(dirs):
            is_last_item = (i == len(dirs) - 1)
            subdirectory = os.path.join(path, dir_name)
            tree_structure += print_directory_tree(subdirectory, indent + ('|   ' if not is_last else '    '), is_last_item)

        # Display files in the current directory
        for i, file_name in enumerate(files):
            is_last_item = (i == len(files) - 1)
            tree_structure += f"{indent}|-- 📄 {file_name}\n" if not is_last else f"{indent}    |-- 📄 {file_name}\n"

    return tree_structure






# Replace '/path/to/your/directory' with the directory you want to print
directory_to_print = 'Chicken-Disease-Classification'

# Create the directory tree structure
directory_tree = f"```\n{print_directory_tree(directory_to_print)}```"

# Print or save the directory tree structure to your README.md file
print(directory_tree)

# Define the filename where you want to save the directory tree
output_file = "directory_tree.md"  # You can specify any filename you prefer

# Save the directory tree to the specified file
with open(output_file, 'w') as file:
    file.write(directory_tree)

print(f"Directory tree saved to {output_file}")
