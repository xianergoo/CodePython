import os

def merge_language_files(folder_path=None):
    if folder_path is None:
        folder_path = os.getcwd()  # 获取当前文件夹路径
    
    # 获取文件夹中的所有子文件夹
    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]
    
    # 遍历每个子文件夹
    for subfolder in subfolders:
        config_file_path = os.path.join(subfolder, subfolder.split('/')[-1] + '.config')
        translation_file_path = os.path.join(subfolder, subfolder.split('/')[-1] + '.translation')
        
        if os.path.exists(config_file_path) and os.path.exists(translation_file_path):
            # 读取当前语言文件的配置信息
            with open(config_file_path, 'r') as config_file:
                config_data = config_file.read()
            
            # 读取当前语言文件的翻译文本
            with open(translation_file_path, 'r') as translation_file:
                translation_data = translation_file.read()
            
            # 提取当前语言文件的英文和翻译文本
            english_texts = []
            translated_texts = []
            lines = translation_data.split('\n')
            i = 0
            while i < len(lines):
                line = lines[i]
                if line.startswith('# English Text'):
                    english_text = line[2:].strip()
                    translated_text = lines[i+1].strip() if i+1 < len(lines) else ''
                    english_texts.append(english_text)
                    translated_texts.append(translated_text)
                    i += 2
                else:
                    i += 1
            
            # 对英文文本进行排序
            sorted_texts = sorted(zip(english_texts, translated_texts))
            sorted_english_texts, sorted_translated_texts = zip(*sorted_texts)
            
            # 更新当前语言文件的翻译文本
            with open(translation_file_path, 'w') as translation_file:
                for eng_text, trans_text in sorted_texts:
                    translation_file.write('# ' + eng_text + '\n')
                    if trans_text:
                        translation_file.write(trans_text + '\n')
                    translation_file.write('\n')
            
            # 更新其他语言文件的翻译文本（排除已经包含的英文内容）
            for other_subfolder in subfolders:
                if other_subfolder != subfolder:
                    other_translation_file_path = os.path.join(other_subfolder, other_subfolder.split('/')[-1] + '.translation')
                    with open(other_translation_file_path, 'r+') as other_translation_file:
                        other_translation_data = other_translation_file.read()
                        if not any(eng_text in other_translation_data for eng_text, _ in sorted_texts):
                            other_translation_file.seek(0, os.SEEK_END)
                            other_translation_file.write('\n')
                            for eng_text, _ in sorted_texts:
                                other_translation_file.write('# ' + eng_text + '\n')
                                other_translation_file.write('\n')
            
            print(f"Merged language files in {subfolder}")
        else:
            print(f"Skipping {subfolder} due to missing config or translation file")

# 调用函数进行语言文件合并（默认为当前文件夹）
merge_language_files()