import os

# Create nested directories
os.makedirs("test_folder/subfolder", exist_ok=True)
print("Directories created.")

# List files and folders
items = os.listdir(".")
print("Current directory contents:")
for item in items:
    print(item)

# Find .txt files
txt_files = [f for f in items if f.endswith(".txt")]
print("TXT files:", txt_files)