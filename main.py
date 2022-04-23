import json
import os
from urllib.parse import urlparse
import requests


def main():
    with open('adlist.json') as json_file:
        adlist = json.load(json_file)
        for item in adlist:
            url_path = urlparse(item["address"]).path
            filename = url_path.replace('/', '', 1).replace('/', '-')
            try:
                response = requests.get(
                    item["address"],
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_15) AppleWebKit/537.36 '
                                      '(KHTML, like Gecko) Chrome/99.0.4859.164 Safari/537.36'
                    }
                )
                if response.status_code == 200:
                    with open("backups/" + filename, 'w') as out_file:
                        out_file.write(response.text)
            except:
                print(filename + " error")

    # backup_files = os.listdir('./backups')
    # with open('merge.txt', 'w') as outfile:
    #     for file_name in backup_files:
    #         if file_name != 'merge.txt':
    #             with open('./backups/' + file_name) as infile:
    #                 outfile.write(infile.read())
    #         outfile.write("\n")

    os.system("./commit.sh")
    exit(0)


if __name__ == "__main__":
    main()
