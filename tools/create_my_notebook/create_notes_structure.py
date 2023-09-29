import os

# 定义章节数和目录名称的映射关系
chapter_mapping = {
    'Chapter-01': 'Python数据模型',
    'Chapter-02': '序列构成的数组',
    'Chapter-03': '字典和集合',
    # 添加更多章节映射关系
    'Chapter-22': '设计模式的实现',
}

# 创建主目录
main_directory = 'Fluent-Python-Notes'
os.makedirs(main_directory, exist_ok=True)

# 遍历章节数和目录名称的映射关系，逐个创建目录和文件
for chapter, chapter_name in chapter_mapping.items():
    chapter_directory = os.path.join(main_directory, chapter)
    os.makedirs(chapter_directory, exist_ok=True)

    # 创建章节概述的Markdown文件
    intro_file = os.path.join(chapter_directory, f'{chapter.lower()}-introduction.md')
    with open(intro_file, 'w') as f:
        f.write(f'# {chapter_name}\n\n')

    # 创建章节示例的Python文件
    examples_file = os.path.join(chapter_directory, f'{chapter.lower()}-examples.py')
    with open(examples_file, 'w') as f:
        f.write('# Examples\n\n')

    # 创建章节练习的Markdown文件
    exercises_file = os.path.join(chapter_directory, f'{chapter.lower()}-exercises.md')
    with open(exercises_file, 'w') as f:
        f.write(f'# {chapter_name} 练习\n\n')

print('目录和文件创建完成。')