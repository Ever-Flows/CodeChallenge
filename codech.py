import os
import random
import glob
import sys
from shutil import copyfile

# Function to create Directory "dirName" and print error if it exists
def createDirectory(dirName): 
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ") 
    except FileExistsError:
        print("Directory " , dirName ,  " already exists. Stopping the program - please cleanup the directories before restarting")
        sys.exit()

# Function to create random string of length stringLength
def createRandomString(stringLength):
    ranstring = ""
    alphanumeric = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'       
    for i in range(stringLength):
        ranstring += random.choice(alphanumeric)
    return ranstring 

# Function to process files in fileList. Process includes - 
# 1. Copy files to destinationDirectory
# 2. go thorught the files and replace characters in charList with "teradata"
def processFiles(fileList,destinationDirectory):
    charList=['a','b','c']
    for logs in fileList:
        dest = os.path.join(destinationDirectory,os.path.basename(logs))
        copyfile(logs,dest)
        with open(dest,'r') as f:
            fileBuffer = f.read()
        with open(dest,'w') as f:
            for c in charList:
                fileBuffer = fileBuffer.replace(c,'teradata')
            f.write(fileBuffer)

def main(param):
    if (param == "debug"):
        debug=1
    else:
        debug=0
    log_directory = "teradata_logs"
    new_log_dir1 = "new_log_dir1"
    new_log_dir2 = "new_log_dir2"
    # Requirement #1 - Create the three directories
    createDirectory(log_directory)
    createDirectory(new_log_dir1)
    createDirectory(new_log_dir2)
    if(debug):
        print("Requirement 1    : Create three directories - Done")

    #Requirement #2 - Create between 10 and 100 files both 10 and 100 exclusive
    number_files=random.randint(11,100)
    for i in range(number_files): 
        # Requirement #2(a) - Create filename as specified in requirements document
        filename = "teradata_logs_" + str(i+1).zfill(3) + ".log"
        # Requirement #2(b) - Create String with Length between 10 and 70 - both 10 and 70 exclusive
        string_length = random.randint(11,70)
        # Write the string into the file in "teradata_logs" sub-folder
        complete_filename = os.path.join("teradata_logs",filename)
        try:
            open(complete_filename,"w+").write(createRandomString
            (string_length))
        except:
            print("Error creating file: "+ complete_filename + " and writing to it - Please check")
    if(debug):
        print("Requirement 2    : Create random number of files between 10 and 100 \n      Requirement 2(a): Create filenames 001 to 00x as specified \n      Requirement 2(b): Create random alphanumeric string of length between 10 and 70\n      - Done"  )
    # Requirement #3 Sort files in teradata_logs sub-folder and create two lists with file names for new_log_dir1 and new_log_dir2

    src_files = os.path.join(log_directory,"teradata_logs_???.log")
    src_files_sorted = sorted([f for f in glob.glob(src_files)])
    # Files for new_log_dir1
    copy_files_dir1 = src_files_sorted[:-3]
    # Files for new_log_dir2
    copy_files_dir2 = src_files_sorted[-3:]

    #Requirement #3 copy files to new_log_dir1 and Requirement #5 replace 'a','b','c' with 'teradata'
    processFiles(copy_files_dir1,new_log_dir1)

    if(debug):
        print("Requirement 3 & 5: Create folder new_log_dir1,\n     move all but last 3 files as sorted on filename to new_log_dir1\n     and replace occurences of 'a','b' and 'c' with 'teradata' \n     - Done")
    
    # Requirement #4 - Copy files as specified in requirement doc for new_log_dir2
    for logs in copy_files_dir2:
         dest = os.path.join(new_log_dir2,os.path.basename(logs))
         copyfile(logs,dest)
    if(debug):
        print("Requirement 4    : Copy files as specified into folder new_log_dir2 - Done")

    # Requirement 6 and 7 - to check for number of occurences of teradata and print to stderr if zero occurences
                    
    count=0
    for logs in copy_files_dir1:
        dest = os.path.join(new_log_dir1,os.path.basename(logs))
        file_buffer = open(dest,'r').read()
        count = count+file_buffer.count('teradata')
    
    if (count>0):
        print("The word teradata occurs " + str(count) + " times in the folder new_log_dir1")
    else:
        print("No occurences of the word teradata in new_log_dir1",file=sys.stderr)
        
    if(debug):
        print("Requirement 6 & 7: Count occurences of 'teradata' in files in folder\n       new_log_dir1 - if zero print stderr else print count - Done")   
# call main function    
if __name__ == '__main__':
    if(len(sys.argv)==2):
        if(sys.argv[1] == 'debug' ):
            main('debug')
        else:
            main('regular')
    else:
        main('regular')