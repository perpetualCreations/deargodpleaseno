"""
deargodpleaseno, revision 1.0

uninstall.py, does the following:
- remove deargodpleaseno directory from webroot
- remove entry for deargodpleaseno under robots.txt TODO for future release
- make sure all items are removed TODO do this before final release
- remove crontab entry
"""

from shutil import rmtree

with open("/etc/deargodpleaseno/webroot") as get_webroot:
    webroot = get_webroot.readline(0)
pass

input("**This is a destructive action, " + webroot + "/deargodpleaseno/" + " will be deleted along with its contents! Press enter to continue, otherwise press Ctrl+C.**")

rmtree(webroot + "/deargodpleaseno/")

print("Uninstall complete.")
