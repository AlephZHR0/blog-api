import os

for file in os.listdir(os.getcwd()):
    if not file.startswith("."):
        if os.path.isdir(file):
            print(f"/{file}")
            for subfile in os.listdir(file):
                print(f"    /{file}/{subfile}")
        else:
            print(f"/{file}")