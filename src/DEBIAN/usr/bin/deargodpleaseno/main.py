"""
deargodpleaseno, revision 1.0

main.py, does the following:
- run install
 - if not already existing, creates deargodpleaseno directory in webroot
 - edits or generates robots.txt to disable obeying user-agents from viewing deargodpleaseno's directory
- run uninstall
 - remove deargodpleaseno directory from webroot
 - remove entry for deargodpleaseno under robots.txt TODO for future release
 - make sure all items are removed TODO do this before final release
- add and remove items from deargodpleaseno's managed folder
- edit items from deargodpleaseno's managed folder

TODO add safety checks, optimize imports, modularize into functions
"""

import argparse
import subprocess
import configparser
from os import remove
from os import mkdir
from shutil import rmtree
from sys import exit as terminate

arguments = argparse.ArgumentParser(description = "Operate deargodpleaseno, use dgpn --help for a list of commands.")
arguments.add_argument("--install", dest = "install", action = "store_const", const = True, help = "Install deargodpleaseno.")
arguments.add_argument("--uninstall", dest = "uninstall", action = "store_const", const = True, help = "Uninstall deargodpleaseno. You'll still have to use your package manager to fully remove deargodpleaseno.")
arguments.add_argument("--add", dest = "add", type = str, help = "Add item to atq for deletion, by specifying path. If --bestbefore is not used in conjunction, default expiry time will be assumed. This is a destructive action.")
arguments.add_argument("--edit", dest = "edit", type = str, help = "Edit expiry time for item by specifying path. Requires specified new expiry, use --bestbefore.")
arguments.add_argument("--remove", dest = "remove", type = str, help = "Removes item from atq for deletion, by specif.")
arguments.add_argument("--bestbefore", dest = "expire", type = int, help = "Specify hours until expiry, optional for --add and required for --edit.")
parameters = arguments.parse_args()

if arguments.expire is None:
    config_fetch = configparser.ConfigParser
    config_fetch.read("/etc/deargodpleaseno/settings.cfg")
    arguments.expire = config_fetch["expire"]["time"]
pass

if parameters.install is True:
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
    terminate(0)
elif parameters.uninstall is True:
    with open("/etc/deargodpleaseno/webroot") as get_webroot:
        webroot = get_webroot.readline(0)
    pass
    input("**This is a destructive action, " + webroot + "/deargodpleaseno/" + " will be deleted along with its contents! Press enter to continue, otherwise press Ctrl+C.**")
    rmtree(webroot + "/deargodpleaseno/")
    print("Uninstall complete.")
    terminate(0)
elif parameters.expire is not None:
    if parameters.edit is not None:
        with open("/etc/deargodpleaseno/entries") as fetch:
            index = 0
            while index <= len(fetch.read().split("\n")):
                if fetch.read().split("\n")[index].split("|||")[1] == parameters.edit:
                    subprocess.call("sudo atrm " + fetch.read().split("\n")[index].split("|||")[0])
                    regenerated = fetch.read().split("\n")
                    regenerated.remove(fetch.read().split("\n")[index].split("|||")[0] + "|||" + fetch.read().split("\n")[index].split("|||")[1])
                pass
            pass
        pass
        remove("/etc/deargodpleaseno/entries")
        with open("/etc/deargodpleaseno/entries", "w") as rebuild:
            rebuild.writelines(regenerated)
        pass
        capture = None
        subprocess.call("sudo rm -r " + parameters.expire + " | at now + " + str(arguments.expire) + " hours", shell = True, stdout = capture)
        with open("/etc/deargodpleaseno/entries", "w") as dump:
            dump.write(capture.split("\n")[1].split()[1] + "|||" + parameters.expire)
        pass
        print("Edited item expiry time.")
    pass
elif paramters.add is not None:
    capture = None
    subprocess.call("sudo rm -r " + parameters.add + " | at now + " + str(arguments.expire) + " hours", shell = True, stdout = capture)
    with open("/etc/deargodpleaseno/entries", "w") as dump:
        dump.write(capture.split("\n")[1].split()[1] + "|||" + parameters.add)
    pass
    print("Added item.")
elif parameters.remove is not None:
    with open("/etc/deargodpleaseno/entries") as fetch:
        index = 0
        while index <= len(fetch.read().split("\n")):
            if fetch.read().split("\n")[index].split("|||")[1] == parameters.remove:
                subprocess.call("sudo atrm " + fetch.read().split("\n")[index].split("|||")[0])
                regenerated = fetch.read().split("\n")
                regenerated.remove(fetch.read().split("\n")[index].split("|||")[0] + "|||" + fetch.read().split("\n")[index].split("|||")[1])
            pass
        pass
    pass
    remove("/etc/deargodpleaseno/entries")
    with open("/etc/deargodpleaseno/entries", "w") as rebuild:
        rebuild.writelines(regenerated)
    pass
    print("Removed item.")
pass
