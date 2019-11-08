import os
import glob

path = '/Users/seita/Desktop/'
screenshots = path + 'screenshots'
pics = path + 'pics'
pdfs = path + 'pdfs'

# organize scattered files

if not os.path.isdir(screenshots):
    os.mkdir(screenshots)
if not os.path.isdir(pics):
    os.mkdir(pics)
if not os.path.isdir(pdfs):
    os.mkdir(pdfs)

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if 'スクリーンショット' in file:
            os.rename(os.path.join(r, file), screenshots + '/' + file)
        elif '.JPG' in file:
            os.rename(os.path.join(r, file), pics + '/' + file)
        elif '.jpg' in file:
            os.rename(os.path.join(r, file), pics + '/' + file)
        elif '.jpeg' in file:
            os.rename(os.path.join(r, file), pics + '/' + file)
        elif '.png' in file:
            os.rename(os.path.join(r, file), pics + '/' + file)
        elif '.pdf' in file:
            os.rename(os.path.join(r, file), pdfs + '/' + file)
        else:
            files.append(os.path.join(r, file))

for f in files:
    print(f)
print('--------------------')

# --------  use glob

# files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]
#
# for f in files:
#     print(f)
# print('--------------------')
#
# files = [f for f in glob.glob(path + "**/", recursive=True)]
#
# for f in files:
#     print(f)
#
# print('--------------------')
