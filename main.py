import os
from filecmp import cmp
import clearScreen

WORKING_DIR = '../../../Downloads/Segmentation'
CURRENT_DIR = os.getcwd()

def get_files(working_dir):
    '''Get all the files from the root dir and the sub dirs'''
    all_files = []
    for (relative_dir,sub_dirs,files) in os.walk(working_dir):
        # print(os.path.abspath(relative_dir), sub_dirs)
        temp_path = os.path.abspath(relative_dir)
        for file in files:
            temp_file = os.path.join(temp_path, file)
            if(file[0] != '.'):
                all_files.append(temp_file)
                # print(temp_file)

    # print(all_files)
    return all_files


def find_duplicate(files):
    '''Compare all files and find the duplicates. Also print them.'''
    duplicate_files = []
    for file1 in files:
        for file2 in files:
            if file1 != file2:
                isDuplicate = cmp(file1, file2, shallow=False)  # shallow or deep search
                # print(file1 + "--" + file2 + " " , isDuplicate)
                if isDuplicate and (file2, file1) not in duplicate_files:
                    duplicate_files.append((file1, file2))

    # Print Duplicate Files
    clearScreen.clear_screen()
    if len(duplicate_files):
        print("Duplicate Files Found!\n")
        print("Duplicate Files:\n")
        for duplicate in duplicate_files:
            print(duplicate)
    else:
        print("No Duplicate Files Found!")


if __name__ == '__main__':
    files = get_files(WORKING_DIR)
    find_duplicate(files)
