from PIL import Image
# import fs
import os
from PIL import Image
rootdir = 'C:/Users/jaime/Desktop/Projects/Python/pyImgConverter/input'
targetdir = 'C:/Users/jaime/Desktop/Projects/Python/pyImgConverter/output/'

target = input('What extension are we converting? (ex: jpg, png, gif): ')
dest = input('What are we converting to? (ex: jpg, png, gif): ')
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith("." + target):
            print(filepath)
            print(file)
            im = Image.open(filepath)
            dest_file_name = file.split(".")
            new_file = (dest_file_name[0]+'.' + dest)
            im.save(targetdir + new_file)