import os
import sys
from os.path import basename
from zipfile import ZipFile
from PIL import Image

included_extensions = ['.jpg','.jpeg', '.bmp', '.png', '.JPG', '.JPEG', '.BMP', '.PNG']

def list_images():    
    file_names = [fn for fn in os.listdir('./photos/')
              if any(fn.endswith(ext) for ext in included_extensions)]
    print(file_names)
    return file_names   

def thumbnail_image(imageName):
    try:    
        imgPath = './photos/' + imageName
        img = Image.open(imgPath)
        img.thumbnail((1024, 768), resample=Image.NEAREST)
        img.save('./resize/' + imageName)
    except FileNotFoundError:
        print('Error: Provided image path is not found')    

def zip_files_in_dir(dirName, zipFileName):
   with ZipFile(zipFileName, 'w') as zipObj:
       for folderName, subfolders, filenames in os.walk(dirName):
           for filename in filenames:
                filePath = os.path.join(folderName, filename)
                zipObj.write(filePath, basename(filePath))

def main():
    try:
        os.remove( './resize_photos.zip')
        os.mkdir('./resize')
    except FileNotFoundError:
        print('Error: Provided zip path is not found')    

    for image in list_images():
        thumbnail_image(image)    
    zip_files_in_dir('resize', 'resize_photos.zip')    
    
    try:
        for image in list_images():
            os.remove('./resize/' + image)
        os.rmdir('./resize')
    except FileNotFoundError:
        print('Error: Provided image path is not found')    


if __name__ == "__main__":
    main()        
