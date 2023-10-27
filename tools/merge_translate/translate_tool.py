import os
from tqdm import tqdm


def find_translate_path(folder_path):
    target_files = []
    for path_name, folders, files in os.walk(folder_path):
        target_suffix = ''
        for filename in files:   

            if os.path.splitext(filename)[0] == 'config':  
                target_suffix = os.path.splitext(filename)[-1]   

            if (target_suffix != '' 
                and filename.endswith(target_suffix) 
                and os.path.splitext(filename)[0] != 'config'):
                target_files.append(os.path.join(path_name, filename)) 

    print(target_files)             
    return target_files
    

def merge_translate(file_list):
    base_translate_lines = []

    def read_file(file):
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            file_lines = []
            i = 0
            for line in lines:
                if line.startswith('#') and line.strip() not in base_translate_lines:
                    file_lines.append(line)
            f.close()
            return file_lines
        
    def merge_translate_file(file):

        cur_tranlsate_lines = dict()
        with open(file, 'r+', encoding='utf-8') as f:
            cur_file_lines = f.readlines()      
            i = 0
            for line in base_translate_lines:
                if line.startswith('#') and (line[1:].strip() != ''):
                    if line in cur_file_lines:
                        index = cur_file_lines.index(line)
                        translated_text = cur_file_lines[index+1].strip() if index + 1 < len(cur_file_lines) else ''
                    else:
                        translated_text = ''

                    cur_tranlsate_lines['#' + line[1:].strip()] = translated_text.strip()

            f.close()

        sorted_keys = sorted(cur_tranlsate_lines.keys())
        with open(file, 'w', encoding='utf-8') as f:
            for key in sorted_keys:
                f.write(key + '\n')
                f.write(cur_tranlsate_lines[key] + '\n')
                f.write('\n')
            f.close()
  

    # for file in file_list:
    for file in tqdm(file_list, desc="Read base file", unit="file"):
        base_translate_lines = base_translate_lines + read_file(file)
    # with open('file.txt', 'w', encoding='utf-8') as f:
    #     f.writelines(base_translate_lines)
    
    # for file in file_list:
    #     merge_translate_file(file)
    for file in tqdm(file_list, desc="Processing files", unit="file"):
        merge_translate_file(file)
    
    # print(len(base_translate_lines))
    return base_translate_lines
    # if len(base_translate_lines) > 0:
    #     with open('new_translate.mlf', 'w', encoding='utf-8') as f:
    #         f.writelines(base_translate_lines)
    #         f.close()




target_files = find_translate_path('.')
merge_lines = merge_translate(target_files)




