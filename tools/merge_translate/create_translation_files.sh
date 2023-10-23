#!/bin/bash

# 创建文件夹
mkdir language_folder1 language_folder2 language_folder3

# 创建配置文件和翻译文件
for folder in language_folder1 language_folder2 language_folder3; do
    config_file="${folder}/${folder}.config"
    translation_file="${folder}/${folder}.translation"

    # 创建配置文件
    echo "# English Config" > "$config_file"
    echo "Some configuration settings for $folder" >> "$config_file"

    # 创建翻译文件
    echo "# English Text 1" > "$translation_file"
    echo "Some translation for English Text 1" >> "$translation_file"
    echo "" >> "$translation_file"
    echo "# English Text 2" >> "$translation_file"
    echo "Some translation for English Text 2" >> "$translation_file"
    echo "" >> "$translation_file"
    echo "# English Text 3" >> "$translation_file"
    echo "Some translation for English Text 3" >> "$translation_file"
    echo "" >> "$translation_file"

    echo "Created translation files for $folder"
done
