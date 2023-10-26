import os
import sys

import json

DEFAULT_BASE_PATH = '../docs'

def create_note_struct(file_name):
   
    with open(file_name, 'r', encoding='utf-8') as f:
        notes = json.load(f)

        note_name = notes['note_name']

        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_path = os.path.dirname(current_dir)

        # 如果当前note文文件夹不存在则创建
        note_base_path = os.path.join(parent_path, DEFAULT_BASE_PATH)
        note_path = os.path.join(note_base_path, note_name)
    
        if not os.path.exists(note_path):
            print(note_path)
            os.mkdir(note_path)

        try:
            for chapter in notes['chapters']:

                chapter_number = chapter['chapter_number']
                chapter_title = chapter['chapter_title']
                chapter_filename = chapter['file_name']
                
                folder_name = chapter_number.replace('/', '')
                markdown_file_name = f'{chapter_title}.md'.replace('/', '')
                python_file_name = f'{chapter_filename}.py'.replace('/', '')
                            
                # 创建章节编号文件夹
                chapter_path = os.path.join(note_path, folder_name)
                print(chapter_path)
                if not os.path.exists(chapter_path):            
                    os.makedirs(chapter_path)
                
                # 创建空的Markdown文件
                markdown_file_path = os.path.join(chapter_path, markdown_file_name)
                if not os.path.exists(markdown_file_path):
                    with open(markdown_file_path, 'w', encoding='utf-8') as md_file:
                        md_file.write('')
                
                # 创建空的Python文件
                python_file_path = os.path.join(chapter_path, python_file_name)
                if not os.path.exists(python_file_path):
                    with open(python_file_path, 'w', encoding='utf-8') as py_file:
                        py_file.write('')

                # print(f'chapter_path: {chapter_path}, markdown_file_path: {chapter_path}, python_file_path{python_file_path}')
        except Exception as e:
            print(e)

if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        if os.path.exists(file_path):
            create_note_struct(file_path)    
        else:
            raise FileNotFoundError('path not exist: {0}'.format(file_path))
    except(IndexError, FileNotFoundError):
        print('param not find or Path params path not Exist')