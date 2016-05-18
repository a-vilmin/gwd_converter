import os, glob, time, sys

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
    for filename in pictures:
        
        type = filename.split('.')[1]
        new_name = time.strftime("%Y-%m-%d")+"-"+venue+"-"+str(i)+"."+type
        os.rename(filename, new_name)
        i += 1
        
if __name__ == '__main__':
    resizer()
