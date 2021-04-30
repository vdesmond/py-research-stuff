import os
import codec_extract

title, author, language = [], [], []
path = "books/"
fileList = os.listdir(path)
for i in fileList:
    with open(os.path.join("books/" + i), "rb") as file:
        raw = file.read()
        print(codec_extract.get_file_encoding(os.path.join("books/" + i)))
        for i, line in enumerate(contents):
            if i == 9:
                title.append(line)
            elif i == 11:
                author.append(line)
            elif i == 15:
                language.append(line)
            elif i > 19:
                break
print(title)
print(author)
print(language)