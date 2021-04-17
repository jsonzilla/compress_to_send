import os
import sys
from os.path import basename
from zipfile import ZipFile
from PIL import Image

included_extensions = ['.jpg','.jpeg', '.bmp', '.png', '.JPG', '.JPEG', '.BMP', '.PNG']

def list_images():
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, r'./photos/')
    file_names = [fn for fn in os.listdir(path)
              if any(fn.endswith(ext) for ext in included_extensions)]
    return file_names   

def thumbnail_image(imageName):
    try:
        dirname = os.path.dirname(__file__)
        inPath = os.path.join(dirname, r'./photos/')
        imgPath = inPath + imageName
        img = Image.open(imgPath)
        img.thumbnail((1024, 768), resample=Image.NEAREST)
        outPath = os.path.join(dirname, r'./resize/')
        img.save(outPath + imageName)
    except FileNotFoundError:
        print('Error: Provided image path is not found')    

def zip_files_in_dir(dirName, zipFileName):
   with ZipFile(zipFileName, 'w') as zipObj:
       for folderName, subfolders, filenames in os.walk(dirName):
           for filename in filenames:
                filePath = os.path.join(folderName, filename)
                zipObj.write(filePath, basename(filePath))

def main():
    dirname = os.path.dirname(__file__)
    try:
        outPath = os.path.join(dirname, './resize_photos.zip')
        os.remove(outPath)
        outPath = os.path.join(dirname, './resize')
        os.mkdir(outPath)
    except FileNotFoundError:
        print('Error: Provided zip path is not found')    

    for image in list_images():
        thumbnail_image(image)    
    zip_files_in_dir('resize', 'resize_photos.zip')    
    
    try:
        for image in list_images():
            outPath = os.path.join(dirname, './resize/' + image)
            os.remove(outPath)
        outPath = os.path.join(dirname, './resize')
        os.rmdir(outPath)
    except FileNotFoundError:
        print('Error: Provided image path is not found')    


if __name__ == "__main__":
    main()        