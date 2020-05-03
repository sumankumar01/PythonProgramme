import os
import fnmatch

for root, dirs, files in os.walk(r"C:\Users\kumar",topdown=True):
    for name in files:
        print(os.path.join(root, name))
    print("*" * 40)
    for name in dirs:
        print(os.path.join(root, name))


