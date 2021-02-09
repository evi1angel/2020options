import os, fnmatch
"""
def list_files(filepath, filetype):
   paths = []
   for root, dirs, files in os.walk(filepath):
      for file in files:
         if file.lower().endswith(filetype.lower()):
            paths.append(os.path.join(root, file))
   return(paths)




# *.mp3 files from the rootPath (“/”)
rootPath = '/'
pattern = '*.mp3'
for root, dirs, files in os.walk(rootPath):
   for filename in fnmatch.filter(files, pattern):
      print(os.path.join(root, filename))





images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
matches = []
      for root, dirnames, filenames in os.walk("C:\"):
         for extensions in images:
              for filename in fnmatch.filter(filenames, extensions): \
                  matches.append(os.path.join(root, filename))




for path, dirs, files in os.walk("./data"):
    for file in files:
        pieces = list(os.path.splitext(file))
        pieces[0] = pieces[0][:-4]
        newFile = "".join(pieces)
        os.rename(os.path.join(path, file), os.path.join(path, newFile))

"""
for path, dirs, files in os.walk("D:\\jon\\test\\"):  #infotrend\\2011_2015_1d_json\\"):
    for file in files:
        pieces = list(os.path.splitext(file))
        pieces[0] = pieces[0][:-4]
        newFile = "".join(pieces)         # this strips off last 4 char of a file name 
        os.rename(os.path.join(path, file), os.path.join(path, newFile))