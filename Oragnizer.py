from os import listdir
from os.path import isfile, join
import os
import shutil

file_path = r"C:\Users\erand\Downloads"

files = [f for f in listdir(file_path) if isfile (join(file_path, f))]

file_list = []
filetype_dict = {}

for file in files:
    
    filetype = file.split('.')[1]
    
    if filetype not in file_list:
        
        file_list.append(filetype)
        
        new_folder_name = file_path+'/' + filetype + '_folder'
        
        filetype_dict[str(filetype)] = str (new_folder_name)
        
        if os.path.isdir(new_folder_name) == True :
            
            continue
        else:
            
            os.mkdir(new_folder_name)
             
i = 1

for file in files :
    
    src_path = file_path + '/' + file
    
    filetype = file.split('.')[1]
    
    if filetype in filetype_dict.keys():
        
        dest_path = filetype_dict [str(filetype)]
        
        shutil.move (src_path, dest_path)
        
    print(i, '. ', src_path + '>>>' + dest_path)
    
    i = i+1