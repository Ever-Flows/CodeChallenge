# CodeChallenge - Date 10/14/2018
This git is a repsonse to Code challenge received on 10/12/2018

# Requirements
The requirements of the code challenge are in the [pdf file](https://github.com/Ever-Flows/CodeChallenge/blob/master/Automation%20Code%20Challenge%20ver%205%5B2%5D.pdf) in this repository. 

# Setup
Assumption 
* **Anaconda is installed** - on MAC type - brew install conda

# Steps for setup
No new modules need to be installed
* **Create codech environment** type in terminal window: conda create -n codech python=3.6
* **Activate environment** type in terminal window: source activate codech
* **Check modules** - Compare with modules in [modules.txt](https://github.com/Ever-Flows/CodeChallenge/blob/master/modules.txt)

# Usage
* *python codech.py* runs the code and meets all requirements outlined in the requirements pdf files.
* *python codech.py debug* helps with the debug by printing output of different steps

# Other Files
* **clearfiles.sh** for MAC - executing this shell script deletes all files and sub-folders to allow running the codech.py program again

# Test environment
* On Apple Mac

# Sample output for python codech.py
Directory  teradata_logs  Created

Directory  new_log_dir1  Created 

Directory  new_log_dir2  Created 

The word teradata occurs 48 times in the folder new_log_dir1

# Sample output for python codech.py debug
Directory  teradata_logs  Created 
Directory  new_log_dir1  Created 
Directory  new_log_dir2  Created 
Requirement 1    : Create three directories - Done
Requirement 2    : Create random number of files between 10 and 100 
      Requirement 2(a): Create filenames 001 to 00x as specified 
      Requirement 2(b): Create random alphanumeric string of length between 10 and 70
      - Done
Requirement 3 & 5: Create folder new_log_dir1,
     move all but last 3 files as sorted on filename to new_log_dir1
     and replace occurences of 'a','b' and 'c' with 'teradata' 
     - Done
Requirement 4    : Copy files as specified into folder new_log_dir2 - Done
The word teradata occurs 173 times in the folder new_log_dir1
Requirement 6 & 7: Count occurences of 'teradata' in files in folder
       new_log_dir1 - if zero print stderr else print count - Done








