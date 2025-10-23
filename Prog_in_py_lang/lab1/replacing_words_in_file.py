
def replace_words_in_file(file_name,words):
    with open(file_name,"r",encoding="utf-8") as file:
        text = file.read()

    for word in words:
        text = text.replace(word,words[word])
    
    with open(file_name,"w",encoding="utf-8") as file: 
        file = file.write(text)

words ={"This": "That", "is": "are"}
replace_words_in_file("long-doc.txt",words)