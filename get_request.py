from requests import get

fl = get('https://stepic.org/media/attachments/course67/3.6.2/819.txt').text.splitlines()
print(len(fl))
