# deargodpleaseno (dgpn)
Command-line tool for automatically deleting files, webpages, and directories.

Intended for Apache web server owners who want to host a temporary page or file that will deleted after a specified amount of time.

A more up-to-date version of the documentation below is available at [dreamerslegacy.xyz](https://dreamerslegacy.xyz/projects/deargodpleaseno/docs.html).

## Install and Uninstall
deargodpleaseno is for Ubuntu systems, running Apache. 

Debian and other Debian-based systems can be used, however install with ignoring dependencies. Afterwards, install Python3 and Apache2.

Add the PPA hosting the Debian package.
```commandline
sudo add-apt-repository ppa:ppa.dreamerslegacy.xyz
```

Install package from PPA. `apt update` is required to retrieve package lists from the PPA.
```commandline
sudo apt update && sudo apt install deargodpleaseno
```

To uninstall,
```commandline
sudo dgpn --uninstall
```
Careful, this will remove the generated directory under the webroot, including any files and directories under the generated directory.  See below for more details.

Then fully remove the package.
```commandline
sudo apt remove deargodpleaseno
```

Purge configurations and other installed files.
```commandline
sudo apt purge deargodpleaseno
```

If there are no additional packages from the PPA you need or are installed, you can remove it.
```commandline
sudo add-apt-repository --remove ppa:ppa.dreamerslegacy.xyz
```

## How to Use
Move a file or directory under the deargodpleaseno directory in the webroot.

Open up your terminal, and run the command `dgpn --help`. You'll be greeted with a list of valid parameters.

This document will outline those parameters further, with given examples.

### `--add`
Specify a path after this parameter, for a directory or file that you wish to be added to the expiry queue.

Use `--bestbefore` in conjunction to specify an expiry time in hours. Without this parameter, the default expiry time will be assumed.
The default time can be edited under `/etc/deargodpleaseno/settings.cfg`, preconfigured to be 168 hours or a week.

This example below will add `/var/www/html/deargodpleaseno/temp.html` to the deletion queue with an expiry time of 24 hours.
```commandline
dgpn --add /var/www/html/deargodpleaseno/temp.html --bestbefore 24
```

### `--edit`
Specify a path after this parameter, for a directory or file whose expiry time you wish to be edited. The file or directory must be added first.

Requires `--bestbefore` in conjunction to specify a new expiry time in hours. Without this parameter, the command will be invalid.

This example below will change the expiry time of `/var/www/html/deargodpleaseno/secret.zip` to 1 hour.
```commandline
dgpn --edit /var/www/html/deargodpleaseno/secret.zip --bestbefore 1
```

### `--remove`
Specify a path after this parameter, for a directory or file that you wish to be removed from the deletion queue.

Does not require any additional parameters. The item removed from queue will not be deleted.

This example below will remove `/var/www/html/deargodpleaseno/spice.png` from deletion queue.
```commandline
dgpn --remove /var/www/html/deargodpleaseno/spice.png
```

### `--bestbefore`
Required for `--edit` and optional for `--add`. Specify an integer after this parameter, which notes the time until the item will expire in hours.

See `--add` and `--edit` for usage.

### `--uninstall`
Specify this parameter to uninstall deargodpleaseno. Remove deargodpleaseno fully with your package manager.

This will remove all entries from queue, and delete deargodpleaseno from the webroot. Be sure to preserve any items under the directory before running `--uninstall.`

An example below is shown.

```commandline
dgpn --uninstall
```

## Back-End
deargodpleaseno uses Linux's `at`.

It can be used to schedule commands in the future. The example below starts a package update in an hour.
```commandline
sudo apt update && sudo apt upgrade -y | at now + 1 hour
```

deargodpleaseno can and probably will clog up your `atq`. Exert caution when removing atjobs.

To remember which atjobs are responsible for removing which items, an `entries` files exists under `/etc/deargodpleaseno/entries` which records items and their atjob number.

They are formatted as `0|||/var/www/html/deargodpleaseno/itemtobedeleted.html`, 0 before the 3 pipes being the atjob number and the path afterwards the item in question.

If the entries and queue desync, reinstalling is the most efficient way of fixing it. Other options such as overwriting `entries` are possible, but aren't foolproof.

deargodpleaseno upon install will create its own directory under the specified webroot. It will then append:
```text
User-agent: *
Disallow: /deargodpleaseno/
```
...To your `robots.txt` file. This will prevent webcrawlers that obey user-agent rules from indexing the newly created directory. 

This of course isn't perfect, any webcrawlers that disregard user-agent rules or take several days or weeks to process new user-agent rules (looking at you SemRush bot) will render this ineffective.

It will create this rule even if the file does not exist, you are recommended to review your user-agent rules post-installation. 

## Conclusion

This concludes our walkthrough of using the DGPN command.

## Future

Future features such as .htaccess control will be coming in following releases.

## End
This is the end of the documentation for the DGPN package.

Please visit https://dreamerslegacy.xyz for other projects, and for contact info in the case of any inquiries.
