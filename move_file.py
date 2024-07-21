import time, os, sys, shutil

path_name = './cleaned_data(50_50)'
target_path_name = './image_data'

os.makedirs(target_path_name, exist_ok=True)

file_list=[]
for x in os.listdir(path_name):
    list1 = x.split('.')
    if list1[-1] == 'png':
        list2 = list1[0].split('_')
        char_path = target_path_name+'/'+list2[0]
        if not os.path.exists(char_path):
            os.makedirs(char_path)
            file_list.append(list2[0])
        shutil.move(path_name+'/'+x, char_path+'/'+list2[1]+'.png')
    
with open('./labels.txt', 'w', encoding='utf8') as f:
    f.write('\n'.join(file_list))
            

    
    