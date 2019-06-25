import os
import shutil

#自动获取工程文件当前位置
current_path = os.path.dirname(__file__)

#遍历目录的内容
def get_all_files(current_path):
    files = os.listdir(current_path)
    list_dir = []
    for file in files:
        list_dir.append(file)
    return list_dir

#传入当前路径，实例化
files_list = get_all_files(current_path)

#预设文件夹，即各类型文件归档的存放地
images = '照片'
folders = '文件夹'
documents = '文档'
zips = '压缩包'
others = 'others'
frontends = '前端文件'
backends = '后端文件'

#启动脚本时检查预设文件夹是否存在，无则创建
folders_list = [images, folders, documents, zips, others, backends, frontends]

for list in folders_list:
    if list not in files_list:
        os.makedirs(list)

#判断文件格式以便归档
images_list = ['.jpg', '.png', '.bmg', '.tif', '.gif']
documents_list = ['.doc', '.docx', '.wps', '.ppt', '.xls', '.xlsx', '.txt', '.md']
zips_list = ['.zip', '.rar']
others_list = ['.bat']
frontends_list = ['.html', '.htm', '.css']
backends_list = ['.php', 'java', '.py']


def attrs(splitext):
    splitext = splitext.lower()
    if splitext in images_list:
        return "1"
    elif splitext in documents_list:
        return "2"
    elif splitext in zips_list:
        return "3"
    elif splitext in others_list:
        return "4"
    else:
        return "5"

#文件归档（除文件夹）
for file in files_list:    
    split_text = os.path.splitext(file)
    attr = attrs(split_text[1])
    
    if attr == "1":
        new_path = os.path.join(current_path, images, file)
        shutil.move(file, new_path)
    elif attr == "2":
        new_path = os.path.join(current_path, documents, file)
        shutil.move(file, new_path)
    elif attr == "3":
        new_path = os.path.join(current_path, zips, file)
        shutil.move(file, new_path)
    elif attr == "4":
        new_path = os.path.join(current_path, others, file)
        shutil.move(file, new_path)

#文件夹归档    
for file in files_list:
    if os.path.isdir(file) and file not in folders_list:
        new_path = os.path.join(current_path, folders, file)
        shutil.move(file, new_path)
