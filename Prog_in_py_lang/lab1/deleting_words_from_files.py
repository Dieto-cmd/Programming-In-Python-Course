def delete_words_from_file(file_name,words):
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()

    for word in words:
        text = text.replace(word,"")

        with open("long-doc.txt", "w", encoding="utf-8") as file:
            file.write(text)
        print(f"Word '{word}' has been deleted from the file.")


words = ["line","the"]
delete_words_from_file("long-doc.txt",words)