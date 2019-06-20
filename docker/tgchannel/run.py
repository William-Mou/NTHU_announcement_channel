import os 
for root, dirs, files in os.walk("./crawler"):
    for f in files:
        fullpath = os.path.join(root, f)
        if fullpath[-3:] == ".py":
            os.system("python " + fullpath)
