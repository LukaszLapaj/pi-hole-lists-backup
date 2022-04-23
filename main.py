import json
import os
from urllib import request
from urllib.parse import urlparse


def main():
    with open('adlist.json') as json_file:
        adlist = json.load(json_file)
        for item in adlist:
            url_path = urlparse(item["address"]).path
            filename = url_path.replace('/', '', 1).replace('/', '-')
            try:
                with request.urlopen(item["address"]) as response, open("backups/" + filename, 'wb') as out_file:
                    blacklist = response.read()
                    out_file.write(blacklist)
            except:
                print(filename + " error")

    backup_files = os.listdir('./backups')
    with open('merge.txt', 'w') as outfile:
        for file_name in backup_files:
            if file_name != 'merge.txt':
                with open('./backups/' + file_name) as infile:
                    outfile.write(infile.read())
            outfile.write("\n")

    os.system("./commit.sh")
    exit(0)


if __name__ == "__main__":
    main()
