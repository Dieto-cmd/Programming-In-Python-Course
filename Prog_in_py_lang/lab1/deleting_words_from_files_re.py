import re

def delete_words_in_file_re(file_name,words):
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()
    pattern = '|'.join(words)
    text = re.sub(pattern,'',text)
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(text)


words = ["line", "file"]
delete_words_in_file_re("long-doc.txt",words)
