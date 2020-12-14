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

arguments = argparse.ArgumentParser(description = "Operate deargodpleaseno, use dgpn --help for a list of commands.")
arguments.add_argument("--install", dest = "install", action = "store_const", const = True, help = "Run install script for deargodpleaseno.")
arguments.add_argument("--uninstall", dest = "uninstall", action = "store_const", const = True, help = "Run uninstall script for deargodpleaseno. You'll still have to use your package manager to fully remove deargodpleaseno.")
arguments.add_argument("--scan", dest = "scan", action = "store_const", const = True, help = "Force scan of deargodpleaseno directory under webroot for new items. Will assume default expiry time.")
arguments.add_argument("--add", dest = "add", type = str, help = "Add item to deargodpleaseno directory under webroot, by specifying path. If --bestbefore is not used in conjunction, default expiry time will be assumed.")
arguments.add_argument("--edit", dest = "edit", type = str, help = "Edit expiry time for item in deargodpleaseno directory under webroot, by specifying path. Requires specified new expiry, use --bestbefore.")
arguments.add_argument("--remove", dest = "remove", type = str, help = "Remove item from deargodpleaseno directory under webroot, by specifying path. This is a destructive action, the item will be deleted! If a directory is specified, any files and subdirectories under it will be deleted.")
arguments.add_argument("--bestbefore", dest = "expire", type = int, help = "Specify minutes until expiry, optional for --add and required for --edit.")
arguments.add_argument("--update", dest = "update", action = "store_const", const = True, help = "Check Github repository for new releases. Packages are not released into the main Debian repository.")
parameters = arguments.parse_args()


