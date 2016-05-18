import os, glob, time, sys
from PIL import Image
from math import floor

def resizer():
    """opens all files in CWD, resizes to 600x400, compresses a little, and renames to
    GWD specs"""
    
    filetypes = ('*.png','*.jpg')
    pictures = []

    try:
        venue = sys.argv[1]
    except:
        print("Must Specify Venue Name as command line argument!")
        return
    
    for files in filetypes:
        #pulls out files in directory for matching types
        pictures.extend(glob.glob(files))

    i = 0    
    for pic in pictures:

        type = pic.split('.')[1]
        new_name = time.strftime("%Y-%m-%d")+"-"+venue+"-"+str(i)+"."+type
        os.rename(pic, new_name)
        i += 1
        
        img = Image.open(new_name)
        img = img.resize((600, 400), Image.ANTIALIAS)
        img.save(new_name, quality = 90) 
        
        
if __name__ == '__main__':
    resizer()
