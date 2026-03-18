import shutil
import os

# Ensure directories exist
os.makedirs("test_folder/subfolder", exist_ok=True)

# Move file
if os.path.exists("backup_sample.txt"):
    shutil.move("backup_sample.txt", "test_folder/subfolder/backup_sample.txt")
    print("File moved.")
else:
    print("File not found.")