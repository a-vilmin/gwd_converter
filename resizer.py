import os, glob, time, sys
from wand.image import Image
from math import floor

def resizer():
    """opens all files in CWD, resizes to 10% of original file, and renames to
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
        with Image(filename = pic) as img:
            wid = float(img.width)
            hi = float(img.height)
            print(str(wid) + " " + str(hi))
            #img.resize(floor(wid * .1), floor(hi * .1))
            img.save(filename = pic)
        
        type = pic.split('.')[1]
        new_name = time.strftime("%Y-%m-%d")+"-"+venue+"-"+str(i)+"."+type
        os.rename(pic, new_name)
        i += 1
        
if __name__ == '__main__':
    resizer()
