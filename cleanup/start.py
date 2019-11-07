import os
import glob

path = '/Users/seita/Desktop/'


# ----------- use os

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.png' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)
print('--------------------')

# --------  use glob

files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]

for f in files:
    print(f)
print('--------------------')

files = [f for f in glob.glob(path + "**/", recursive=True)]

for f in files:
    print(f)

print('--------------------')
