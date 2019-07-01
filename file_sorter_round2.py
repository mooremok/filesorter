import os
import shutil

# Name the folders
folders_name = {
    'images': '照片',    
    'documents': '文档',
    'zips': '压缩包',    
    'frontends': '前端文件',
    'backends': '后端文件',
    'others': 'others',
    'folders': '文件夹',
}

folders_type = {
    'images_type': ['.jpg', '.png', '.bmg', '.tif', '.gif'],
    'documents_type': ['.doc', '.docx', '.wps', '.ppt', '.pptx', '.xls', '.xlsx', '.txt', '.md'],
    'zips_type': ['.zip', '.rar', '.7z'],
    'frontends_type': ['.html', '.htm', '.css'],
    'backends_type': ['.php', '.java', '.py'],
    'others': ['.bat'],
}

def get_cwd():
    """Return the current working directory."""
    return os.getcwd()

def get_all_files(cwd):
    """Return a list containing files in current working directory"""
    return os.listdir(cwd)

# Handle the folders_name & folders_type to a list for late using
class FileOperation():
    def __init__(self):        
        self.folders = folders_name.values()
        self.folders_type = folders_type.values()

    def folder_name(self):
        """Return a list of folder name""" 
        folders = []
        for folder in self.folders:
            folders.append(folder)
        return folders
    
    def folder_type(self): 
        """Return a list of folder type"""
        types = []
        for type in self.folders_type:
            types.append(type)
        return types 

# While run the script, create the folders if not exist.   
def create_folder(folder_name, all_files):
    for i in folder_name:
        if i not in all_files:
            os.makedirs(i)

# Sort all_files
class Sorter():
    """Sort the files except for folder """
    def palce_file(self, cwd, all_files, folder_type, folder_name):
        for file in all_files:
            suffix = os.path.splitext(file)[1]

            if suffix in folder_type[0]:
                new_path = os.path.join(cwd, folder_name[0], file)
                shutil.move(file, new_path)
            elif suffix in folder_type[1]:
                new_path = os.path.join(cwd, folder_name[1], file)
                shutil.move(file, new_path)
            elif suffix in folder_type[2]:
                new_path = os.path.join(cwd, folder_name[2], file)
                shutil.move(file, new_path)
            elif suffix in folder_type[3]:
                new_path = os.path.join(cwd, folder_name[3], file)
                shutil.move(file, new_path)
            elif suffix in folder_type[4]:
                new_path = os.path.join(cwd, folder_name[4], file)
                shutil.move(file, new_path)
            elif suffix in folder_type[5]:
                new_path = os.path.join(cwd, folder_name[5], file)
                shutil.move(file, new_path)

    """Sort the folder """
    def palce_folder(self, cwd, all_files, folder_name):
        for i in all_files:
            if os.path.isdir(i) and i not in folder_name:
                new_path = os.path.join(cwd, folder_name[6], i)
                shutil.move(i, new_path)

# The current working directory.
cwd = get_cwd()

# The all files in the current working directory.
all_files = get_all_files(cwd)

# FileOperation
file_operation = FileOperation()
folder_name = file_operation.folder_name()
folder_type = file_operation.folder_type()

# While run the script, create the folders if not exist.
create_folder = create_folder(folder_name, all_files)


# Begin to sort
sorts = Sorter()
sort_files = sorts.palce_file(cwd, all_files, folder_type, folder_name)
sort_folder = sorts.palce_folder(cwd, all_files, folder_name)
