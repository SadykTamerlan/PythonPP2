import shutil
import os

# Copy file
shutil.copy("sample.txt", "copy_sample.txt")
print("File copied.")

# Create backup
shutil.copy("sample.txt", "backup_sample.txt")
print("Backup created.")

# Delete file safely
if os.path.exists("copy_sample.txt"):
    os.remove("copy_sample.txt")
    print("File deleted.")
else:
    print("File not found.")