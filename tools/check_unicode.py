import re

def contains_non_latin_characters(text):
    pattern = re.compile(r"[^\u0000-\u007F]")  # 匹配非基本拉丁字符
    return bool(pattern.search(text))

# 示例测试
text1 = "Hello World%$#"
text2 = "你好，世界"
text3 = "Hello 你好，世界"

print(contains_non_latin_characters(text1))  # False
print(contains_non_latin_characters(text2))  # True
print(contains_non_latin_characters(text3))  # True