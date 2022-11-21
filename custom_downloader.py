#create a file named custom_repo next to the script
#then type the alias, type the '=' character and the url to download like this:
#example: alias=https://example.com/image.png

import wget

name = input("name: ")
url = ""

with open("./custom_repo") as file_in:
    for line in file_in:
        if (line.split('=')[0] == name):
            url = line.split('=')[1]
            break
            
file_name = wget.download(url)