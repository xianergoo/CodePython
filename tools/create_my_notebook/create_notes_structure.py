import os
import json

def create_note_struct(file_name):
    # if not os.path.exists(file_name):
    #     os.mkdir(file_name)
    with open(file_name, 'r', encoding='utf-8') as f:
        chapters = json.load(f)
        for chapter in chapters['chapters']:
            chapter_number = chapter['chapter_number']
            chapter_title = chapter['chapter_title']
            chapter_filename = chapter['file_name']
            
            folder_name = f'Chapter_{chapter_number}'
            markdown_file_name = f'{chapter_title}.md'
            python_file_name = f'{chapter_filename}.py'
            
            # 创建章节编号文件夹
            if not os.path.exists(folder_name):
                pass
                # os.makedirs(folder_name)
            
            # 创建空的Markdown文件
            markdown_file_path = os.path.join(folder_name, markdown_file_name)
            if not os.path.exists(markdown_file_path):
                # with open(markdown_file_path, 'w', encoding='utf-8') as md_file:
                #     md_file.write('')
                pass
            
            # 创建空的Python文件
            python_file_path = os.path.join(folder_name, python_file_name)
            if not os.path.exists(python_file_path):
                # with open(python_file_path, 'w', encoding='utf-8') as py_file:
                #     py_file.write('')
                pass
            
            print(f'Chapter {chapter_number}: Created folder, markdown file, and python file.')

if __name__ == '__main__':
    create_note_struct('fluent_python_note.json')