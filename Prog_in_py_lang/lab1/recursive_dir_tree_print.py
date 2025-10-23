import os

def recursive_dir_tree_print(directory, level=0):
    items = os.listdir(directory)
    for item in items:
        full_path = os.path.join(directory, item)
        print("    " * level + f"- {item}")  # Space depending on level

        if os.path.isdir(full_path):
            recursive_dir_tree_print(full_path, level + 1)

recursive_dir_tree_print("C:/Users/48510/OneDrive/Pulpit/CppPlayground")
