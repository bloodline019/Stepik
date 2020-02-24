from requests import get

fl = get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
while fl.text.split()[0] != "We":
    fl = get('https://stepic.org/media/attachments/course67/3.6.3/' + fl.text.split()[0])
print(fl.text)
