import os
import shutil

"""
Set constants
"""

# Set the presuposed folders for storing files object.
images = '照片'
folders = '文件夹'
documents = '文档'
zips = '压缩包'
others = 'others'
frontends = '前端文件'
backends = '后端文件'

# listing all the presuposed folders.
folders_list = [images, folders, documents, zips, others, backends, frontends]

# sort the file_attr, use to judge the file which folder should be sorted into.
images_type = ['.jpg', '.png', '.bmg', '.tif', '.gif']
documents_type = ['.doc', '.docx', '.wps', '.ppt', '.pptx', '.xls', '.xlsx', '.txt', '.md']
zips_type = ['.zip', '.rar', '.7z']
frontends_type = ['.html', '.htm', '.css']
backends_type = ['.php', '.java', '.py']
others_type = ['.bat']


"""Direction of improvement:

Round 1: moving around
    1. More meaningful variable naming (e.g. images_type rathan than images_list)
    2. More structural
    3. Change comments from Chinese to English.

Round 2: 
    1. Tidy up. 
    2. Rewrite the structure of folder list (images...others, images_type...others_type). 
        Maybe use tuple instead of list.
    3. Rewrite function bodies to be more structural.
    4. Use of exception."""

def get_cwd():
    """Return the current working directory."""    
    curr_file = os.path.abspath(__file__)
    curr_folder = os.path.dirname(curr_file)
    return curr_folder

def get_all_files(current_path):
    """Return a list containing files of current_path."""    
    # TODO: check if I need list_dir stuffs.
    files = os.listdir(current_path)
    list_dir = []
    for file in files:
        list_dir.append(file)
    return list_dir

def create_folder(files, folders):
    """Create if folder does not exist."""
    # Checking in the current_path, create the presuposed folder that not matching.    
    for item in folders:
        if item not in files: # Not matching in the current_path, then create one.
            os.makedirs(item)

def place_files(cwd, files):
    """Sort and archive files in given path."""
    # except for folder
    for file in files:    
        split_text = os.path.splitext(file)
        attr = attrs(split_text[1])
        
        if attr == "1":
            new_path = os.path.join(cwd, images, file)
            shutil.move(file, new_path)
        elif attr == "2":
            new_path = os.path.join(cwd, documents, file)
            shutil.move(file, new_path)
        elif attr == "3":
            new_path = os.path.join(cwd, zips, file)
            shutil.move(file, new_path)
        elif attr == "4":
            new_path = os.path.join(cwd, others, file)
            shutil.move(file, new_path)
        elif attr == "5":
            new_path = os.path.join(cwd, frontends, file)
            shutil.move(file, new_path)
        elif attr == "6":
            new_path = os.path.join(cwd, backends, file)
            shutil.move(file, new_path)
    print("File placement is completed.")

def place_folder(cwd, files, folders_list):
    """Place folder"""    
    for item in files:
        if os.path.isdir(item) and item not in folders_list:
            new_path = os.path.join(cwd, folders, item)
            shutil.move(item, new_path)
    print("Folder placement is completed.")

def attrs(splitext):
    splitext = splitext.lower()
    if splitext in images_type:
        return "1"
    elif splitext in documents_type:
        return "2"
    elif splitext in zips_type:
        return "3"
    elif splitext in others_type:
        return "4"
    elif splitext in frontends_type:
        return "5"
    elif splitext in backends_type:
        return "6"
    else:
        return "7"


# get the current_path 
cwd = get_cwd()
# go through all the files object
all_files = get_all_files(cwd)
# check the presuposed folders 
create_folder(all_files, folders_list)
# sort and archive the files except for folder
place_files(cwd, all_files)
# sort and archive the folders
place_folder(cwd, all_files, folders_list)