import os
from os.path import join, getsize
import datetime
import pprint

directory = r'/Users/peter/Computrain/_InCompany/Defensie/Python Traject'


for root, dirs, files in os.walk(directory):

    dirs[:] = [d for d in dirs if not d.startswith('.') and not d.startswith('__')] 
    files[:] = [f for f in files if not f.startswith('.')] 

    # print('>>>>>>', root)
    # print(dirs)
    # print(files)

    entries = []
    for file in files:
        filepath = os.path.join(root, file)

        size = os.path.getsize(filepath)

        stat = os.stat(filepath)

        atime = datetime.datetime.fromtimestamp(stat.st_atime)
        mtime = datetime.datetime.fromtimestamp(stat.st_mtime)
        ctime = datetime.datetime.fromtimestamp(stat.st_ctime)

        d = {
            'dir': root,
            'file': file,
            'size': size,
            'atime': atime,
            'mtime': mtime,
            'ctime': ctime,
        }
        entries.append(d)

pprint.pprint(entries)
