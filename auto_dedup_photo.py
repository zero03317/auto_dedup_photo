from PIL import Image
import imagehash
import os
import itertools

#wait user input value
def wait():
    raw_input("Press Enter to exit...")
    exit(1)


#will calculator the picture hash value and save in dictionary
def hash_file(file):
    try:
        hashes = []
        img = Image.open(file)
        hashes.append(str(imagehash.phash(img)))
        hashes.append(file)

        return hashes
    except OSError:
        print("\tUnable to open {}".format(file), "red")
        return None




if __name__ == '__main__':
    try:
        print "Please input source path (example:C:\\f1)"
        source_path = raw_input()
        if os.path.isdir(source_path):
            print "source path correct"
        else:
            print "path no exists pls try again"
            wait()
        for dirPath, dirNames, fileNames in os.walk(source_path):
            lengther = 0
            diction_result=[]
            for f in fileNames:
                result = os.path.join(dirPath, f)
                hash_value=hash_file(result)
                diction_result.append(hash_value)
                #md5_result = md5(result)
                #diction_result[f] = md5_result
                lengther += 1
                print "Data size:" + str(lengther)
        print diction_result
        
    except Exception as error:
      print error


