import re

def replace_words_in_file_re(file_name,words):
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()
    words_to_be_replaced = []
    for word in words:
        text = re.sub(word,words[word],text)
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(text)

words = {"Line": "Cosmos", "That": "This"}
replace_words_in_file_re("long-doc.txt",words)