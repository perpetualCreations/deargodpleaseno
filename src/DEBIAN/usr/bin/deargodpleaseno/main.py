"""
deargodpleaseno, revision 1.0

main.py, does the following:
- run install.py and uninstall.py
- add and remove items from deargodpleaseno's managed folder
- edit items from deargodpleaseno's managed folder
- display help
- check for updates
"""

import argparse
import subprocess
from sys import exit as terminate

arguments = argparse.ArgumentParser(description = "Operate deargodpleaseno, use dgpn --help for a list of commands.")
arguments.add_argument("--install", dest = "install", action = "store_const", const = True, help = "Run install script for deargodpleaseno.")
arguments.add_argument("--uninstall", dest = "uninstall", action = "store_const", const = True, help = "Run uninstall script for deargodpleaseno. You'll still have to use your package manager to fully remove deargodpleaseno.")
arguments.add_argument("--scan", dest = "scan", action = "store_const", const = True, help = "Force scan of deargodpleaseno directory under webroot for new items. Will assume default expiry time.")
arguments.add_argument("--add", dest = "add", type = str, help = "Add item to deargodpleaseno directory under webroot, by specifying path. If --bestbefore is not used in conjunction, default expiry time will be assumed.")
arguments.add_argument("--edit", dest = "edit", type = str, help = "Edit expiry time for item in deargodpleaseno directory under webroot, by specifying path. Requires specified new expiry, use --bestbefore.")
arguments.add_argument("--remove", dest = "remove", type = str, help = "Remove item from deargodpleaseno directory under webroot, by specifying path. This is a destructive action, the item will be deleted! If a directory is specified, any files and subdirectories under it will be deleted.")
arguments.add_argument("--bestbefore", dest = "expire", type = int, help = "Specify hours until expiry, optional for --add and required for --edit.")
parameters = arguments.parse_args()

if parameters.install is True:
    print("Called install.")
    subprocess.Popen("python install.py", shell = True)
    terminate(0)
elif parameters.uninstall is True:
    print("Called uninstall.")
    subprocess.Popen("python uninstall.py", shell = True)
    terminate(0)
elif parameters.scan is True:
    print("Started scan for new items in dgpn's directory under webroot.")
    subprocess.Popen("python scan.py", shell = True)
elif parameters.expire is not None:
    if parameters.edit is not None:
        print("Edited item expiry time.")
        # TODO AT edit
    pass
elif paramters.add is not None:
    print("Added item.")
    # TODO AT append
elif parameters.remove is not None:
    input("**This is a destructive action, the item will be deleted! Press enter to continue, otherwise press Ctrl+C.**")
    # TODO AT edit
pass
