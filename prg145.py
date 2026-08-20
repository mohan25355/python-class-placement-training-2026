import shutil
folder="C:\\Users\\HP\\OneDrive\\Desktop\\New folder (3)"
try:
    shutil.rmtree(folder)
    print("deleted")
except FileNotFoundError:
    print("folder not found")
except OSError:
    print("folder is not empty")