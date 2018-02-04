from PIL import Image
import imagehash
import os

#wait user input value
def wait():
    raw_input("Press Enter to exit...")
    exit(1)


#will calculator the picture hash value and save in dictionary
def hash_file(file):
    try:
        #hashes = []
        img = Image.open(file)
        hash_image=(str(imagehash.phash(img)))


        return hash_image
    except OSError:
        print("\tUnable to open {}".format(file), "red")
        return None

def file_list(list):
    list_length=len(list)
    total_list=[]
    for i in range(0,list_length):
        file_path=list[i][0]
        total_list.append(file_path)

    return total_list

def delete_file(list_value):
    list_length=len(list_value)
    for i in range(0,list_length):
        file_path=list_value[i]
        os.remove(file_path)

    return True

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
            diction_result={}
            for f in fileNames:
                result = os.path.join(dirPath, f)
                hash_value=hash_file(result)
                #diction_result.append(hash_value)
                #md5_result = md5(result)
                diction_result[result] = hash_value
                lengther += 1
                print "Data size:" + str(lengther)
        print diction_result
        result1 = {}
        for key, value in diction_result.items():
            if value not in result1.values():
                result1[key] = value
        set1=set(diction_result.items())
        set2=set(result1.items())
        total_result=set1-set2
        total_result_list=list(total_result)
        if total_result_list==[]:
            print "Dont need to dedup the photo"
            exit(1)
        delete_file_list=file_list(total_result_list)
        print "Script will delete the file = " +str(delete_file_list)
        print "If u confim delete the file please input y or Y "
        confirm=raw_input()
        if confirm == "Y" or "y":
            print "starting dedup the photo"
            delete_file_success=delete_file(delete_file_list)
            if delete_file_success==True:
                print "delete final"
            else:
                print "delete fail please check again"
        else:
            print "input error please try again"

    except Exception as error:
      print error


