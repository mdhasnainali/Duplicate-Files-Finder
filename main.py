import os
from filecmp import cmp
import clearScreen

current_dir = os.getcwd()
checking_dir = os.path.join(current_dir, 'files')  # directory that need to check
files = os.listdir(checking_dir)
files = [file_name for file_name in files if (file_name[0]
         != '.') and os.path.isfile(os.path.join(checking_dir,file_name))]

# print(files)


duplicate_files = []

for file1 in files:
    for file2 in files:
        if file1 != file2:
            file1_path = os.path.join(checking_dir, file1)
            file2_path = os.path.join(checking_dir, file2)
            isDuplicate = cmp(file1_path, file2_path, shallow=False)  # shallow or deep search
            # print(file1 + "--" + file2 + " " , isDuplicate)
            if isDuplicate and (file2, file1) not in duplicate_files:
                duplicate_files.append((file1, file2))


clearScreen.clear_screen()
if len(duplicate_files):
    print("Duplicate Files Found!\n")
    print("Duplicate Files:")
    for duplicate in duplicate_files:
        print(duplicate)
else:
    print("No Duplicate Files Found!")
