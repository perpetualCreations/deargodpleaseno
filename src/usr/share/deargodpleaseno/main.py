"""
deargodpleaseno, revision 1.0

main.py, does the following:
- run install
 - if not already existing, creates deargodpleaseno directory in webroot
 - edits or generates robots.txt to disable obeying user-agents from viewing deargodpleaseno's directory
- run uninstall
 - remove deargodpleaseno directory from webroot
 - remove entry for deargodpleaseno under robots.txt TODO for future release
 - make sure all items are removed
- add and remove items from deargodpleaseno's managed folder
- edit items from deargodpleaseno's managed folder
"""

import argparse
from subprocess import run
import configparser
from os import mkdir
from shutil import rmtree
from sys import exit as terminate
from os.path import isdir
from os.path import isfile

arguments = argparse.ArgumentParser(description = "Operate deargodpleaseno, use dgpn --help for a list of commands.")
arguments.add_argument("--install", dest = "install", action = "store_const", const = True, help = "Install deargodpleaseno.")
arguments.add_argument("--uninstall", dest = "uninstall", action = "store_const", const = True, help = "Uninstall deargodpleaseno. You'll still have to use your package manager to fully remove deargodpleaseno.")
arguments.add_argument("--add", dest = "add", type = str, help = "Add item to atq for deletion, by specifying path. If --bestbefore is not used in conjunction, default expiry time will be assumed. This is a destructive action.")
arguments.add_argument("--edit", dest = "edit", type = str, help = "Edit expiry time for item by specifying path. Requires specified new expiry, use --bestbefore.")
arguments.add_argument("--remove", dest = "remove", type = str, help = "Removes item from atq for deletion, by specif.")
arguments.add_argument("--bestbefore", dest = "expire", type = int, help = "Specify hours until expiry, optional for --add and required for --edit.")
parameters = arguments.parse_args()

if parameters.install is True:
    webroot = input("Enter webroot: ")
    try:
        mkdir(webroot + "/deargodpleaseno")
    except FileExistsError:
        pass
    pass
    with open(webroot, "a") as edit_user_agent_rules: edit_user_agent_rules.write("\n\nUser-agent: *\nDisallow: /deargodpleaseno/")
    with open("/etc/deargodpleaseno/webroot", "w") as dump_webroot: dump_webroot.write(webroot)
    print("Install complete.")
    terminate(0)
elif parameters.uninstall is True:
    with open("/etc/deargodpleaseno/webroot") as get_webroot: webroot = get_webroot.readline(0)
    input("**This is a destructive action, " + webroot + "/deargodpleaseno/" + " will be deleted along with its contents! Press enter to continue, otherwise press Ctrl+C.**")
    rmtree(webroot + "/deargodpleaseno/")
    with open("/etc/deargodpleaseno/entries") as fetch:
        if fetch.read() != "":
            index = 0
            while index <= len(fetch.read().split("\n")):
                run("sudo atrm " + fetch.read().split("\n")[index].split("|||")[0], shell = True)
                index += 1
            pass
        pass
    pass
    print("Uninstall complete.")
    terminate(0)
else:
    if parameters.expire is None:
        config_fetch = configparser.ConfigParser()
        config_fetch.read("/etc/deargodpleaseno/settings.cfg")
        parameters.expire = config_fetch["expire"]["time"]
    pass
    if parameters.add == "/" or parameters.edit == "/": raise Exception("Target item was root.")
    elif parameters.add is not None and isdir(parameters.add) is False and isfile(parameters.add) is False: raise SyntaxError("Item path is invalid!")
    elif parameters.edit is not None:
        if isdir(parameters.edit) is False and isfile(parameters.edit) is False: raise SyntaxError("Item path is invalid!")
        elif parameters.expire is None: raise SyntaxError("User requested item expiry edit, however no expiry time was specified! Use --bestbefore to specify one.")
        with open("/etc/deargodpleaseno/entries") as fetch: entries = fetch.read()
        index = 0
        while index <= len(entries.split("\n")):
            try:
                if entries.split("\n")[index].split("|||")[1] == parameters.edit:
                    run("sudo atrm " + entries.split("\n")[index].split("|||")[0], shell = True)
                    regenerated = entries.split("\n")
                    regenerated.remove(entries.split("\n")[index].split("|||")[0] + "|||" + entries.split("\n")[index].split("|||")[1])
                    with open("/etc/deargodpleaseno/entries", "w") as rebuild: rebuild.writelines(regenerated)
                pass
            except IndexError: pass
            index += 1
        pass
        capture = run("sudo at now + " + str(parameters.expire) + " hours <<EOF\n" + "sudo rm -r " + parameters.edit + "\nEOF", shell = True, capture_output = True).stderr.decode(encoding = "utf-8")
        with open("/etc/deargodpleaseno/entries", "a") as dump: dump.write("\n" + capture.split("\n")[1].split()[1] + "|||" + parameters.edit)
        print("Edited item expiry time.")
        terminate(0)
    elif parameters.remove is not None and isdir(parameters.remove) is False and isfile(parameters.remove) is False: raise SyntaxError("Item path is invalid!")
    elif parameters.add is None and parameters.edit is None and parameters.remove is None: raise SyntaxError("No action was specified. Use --add, --edit, or --remove to specify one, remember to type in the item path after the parameter.")
    elif parameters.add is not None:
        capture = run("sudo at now + " + str(parameters.expire) + " hours <<EOF\n" + "sudo rm -r " + parameters.add + "\nEOF", shell = True, capture_output = True).stderr.decode(encoding = "utf-8")
        with open("/etc/deargodpleaseno/entries", "a") as dump: dump.write("\n" + capture.split("\n")[1].split()[1] + "|||" + parameters.add)
        print("Added item.")
        terminate(0)
    elif parameters.remove is not None:
        with open("/etc/deargodpleaseno/entries") as fetch: entries = fetch.read()
        index = 0
        while index <= len(entries.split("\n")):
            try:
                if entries.split("\n")[index].split("|||")[1] == parameters.remove:
                    run("sudo atrm " + entries.split("\n")[index].split("|||")[0], shell = True)
                    regenerated = entries.split("\n")
                    regenerated.remove(entries.split("\n")[index].split("|||")[0] + "|||" + entries.split("\n")[index].split("|||")[1])
                    with open("/etc/deargodpleaseno/entries", "w") as rebuild: rebuild.writelines(regenerated)
                pass
            except IndexError: pass
            index += 1
        pass
        print("Removed item.")
        terminate(0)
    pass
pass
