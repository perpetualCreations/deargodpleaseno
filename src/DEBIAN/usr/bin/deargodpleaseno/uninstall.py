"""
deargodpleaseno, revision 1.0

uninstall.py, does the following:
- remove deargodpleaseno directory from webroot
- remove entry for deargodpleaseno under robots.txt TODO for future release
- remove crontab entry
"""

from shutil import rmtree
from subprocess import call

with open("/etc/deargodpleaseno/webroot") as get_webroot:
    webroot = get_webroot.readline(0)
pass

input("**This is a destructive action, " + webroot + "/deargodpleaseno/" + " will be deleted along with its contents! Press enter to continue, otherwise press Ctrl+C.**")

rmtree(webroot + "/deargodpleaseno/")

call("crontab -u mobman -l | grep -v 'dgpn --scan  >/dev/null 2>&1'  | crontab -u mobman -", shell = True)

print("Uninstall complete.")
