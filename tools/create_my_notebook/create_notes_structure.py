import os
import json

def create_note_struct(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        chapters = json.load(f)
        for chapter in chapters['chapters']:
            chapter_number = chapter['chapter_number']
            chapter_title = chapter['chapter_title']
            chapter_filename = chapter['file_name']
            print(f'{chapter_number}: {chapter_title}-{chapter_filename}')

if __name__ == '__main__':
    create_note_struct('fluent_python_note.json')