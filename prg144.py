import os
folder="C:\\Users\\HP\\OneDrive\\Desktop\\New folder (59)"
try:
    os.rmdir(folder)
    print("deleted")
except FileNotFoundError:
    print("folder not found")
except OSError:
    print("folder is not empty")