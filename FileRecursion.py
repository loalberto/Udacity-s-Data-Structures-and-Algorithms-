import os


def list_all_dir(list_of_paths, path):
    if list_of_paths is None or path is None:
        return None

    if os.path.isfile(path) and not path.endswith('.c'):
        return
    if not os.path.isfile(path):
        for item in os.listdir(path):
            list_all_dir(list_of_paths, os.path.join(path, item))
    if os.path.isfile(path) and path.endswith('.c'):
        list_of_paths.append(path)

    return


path = './'
paths = []
list_all_dir(paths, path)
print(paths)

# This will return an empty list
path = None
paths = []
list_all_dir(path, paths)
print(paths)

# This will return None
path = None
paths = None
list_all_dir(path, path)
print(paths)

# Let us print the files in the directory in which you are running this script
print (os.listdir("."))

# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))
