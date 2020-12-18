"""
deargodpleaseno, revision 1.0

scan.py, does the following:
- looks for entries whose items have already been removed or expired
- checks deargodpleaseno under webroot for new items
"""

from os.path import isfile
from os.path import isdir
from os import listdir
from os import remove

with open("/etc/deargodpleaseno/entries") as fetch:
    index = 0
    entries = fetch.read().split("\n")
    while index <= int(len(entries)):
        if isfile(entries[index]) is False and isdir(entries[index]):
            entries.remove(entries[index])
        pass
        index += 1
    pass
pass

remove("/etc/deargodpleaseno/entries")

with open("/etc/deargodpleaseno/entries", "w") as dump:
    fetch.writelines(entries)
pass


