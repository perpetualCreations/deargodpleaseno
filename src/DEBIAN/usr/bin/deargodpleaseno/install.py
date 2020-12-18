"""
deargodpleaseno, revision 1.0

install.py, does the following:
- if not already existing, creates deargodpleaseno directory in webroot
- edits or generates robots.txt to disable obeying user-agents from viewing deargodpleaseno's directory
"""

from os import mkdir

webroot = input("Enter webroot: ")

try:
    mkdir(webroot + "/deargodpleaseno")
except FileExistsError:
    pass
pass

with open(webroot, "w") as edit_user_agent_rules:
    edit_user_agent_rules.write("User-agent: *\nDisallow: /deargodpleaseno/")
pass

with open("/etc/deargodpleaseno/webroot", "w") as dump_webroot:
    dump_webroot.write(webroot)
pass

print("Install complete.")
