import re

text = input("full text: ")
keyword = input("key word: ")
print("------------------------------------")

for index in range(int(sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(keyword), text)))):
    text = text.replace("$" + keyword + "$", keyword + str(index+1), 1)

print(text)
      