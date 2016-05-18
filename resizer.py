import os, glob

def resizer():
    """opens all files in CWD, resizes to 10% of original file, and renames to
    GWD specs"""
    
    filetypes = ('*.png','*.jpg')
    pictures = []

    for files in filetypes:
        pictures.extend(glob.glob(files))

    #open all files in directory
    for filename in pictures:
        print(filename)

if __name__ == '__main__':
    resizer()
