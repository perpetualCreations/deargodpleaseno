CLI Tool for Scheduled Deletions
================================
:Latest Version - |version|:

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
------------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
* `Back to Projects </index.html##projects>`_

Install
-------
For other Debian and Debian-based operating systems, please ignore package requirements when installing, and install your distribution's latest version of Apache.
DGPN can be installed with APT or manually installed with a Debian package file.
Please see `preliminary documentation </index.html###ppa>`_ for how to add the PPA repository required for APT installation and updating.

.. code-block:: bash

   sudo apt install deargodpleaseno

.. parsed-literal::

   wget https://github.com/perpetualCreations/deargodpleaseno/releases/download/\ |release|\ /deargodpleaseno_\ |release|\ _all.deb
   sudo apt install /path/to/wheel/file/deargodpleaseno_\ |release|\ _all.deb

.. |release| replace:: |version|

Before using APT to uninstall DGPN, 

.. code-block:: bash

   sudo dgpn --uninstall

Exert caution, the generated directory under the webroot will be deleted, alongside all of its contents and subdirectories.
Fully remove DGPN with your package manager.

Outline
-------
Command-line tool for automatically deleting files and directories.
Intended for web server operators who want to host a temporary page or file that will deleted after a specified amount of time.

Usage
-----
Use,

.. code-block:: bash

   dgpn --help

To view all valid flags and parameters, and their usage, while in terminal.

Specify a path for a directory or file that you wish to be added to the expiry queue with --add.
Use --bestbefore in conjunction to specify an expiry time in hours. Without this parameter, the default expiry time will be assumed. 
The default time can be edited under /etc/deargodpleaseno/settings.cfg, preconfigured to be 168 hours or a week.
                
This example below will add /var/www/html/deargodpleaseno/temp.html to the deletion queue with an expiry time of 24 hours.

.. code-block:: bash
   
   sudo dgpn --add /var/www/html/deargodpleaseno/temp.html --bestbefore 24

Specify a path for a directory or file whose expiry time you wish to be edited with --edit. The file or directory must be added first.
Requires --bestbefore in conjunction to specify a new expiry time in hours. Without this parameter, the command will be invalid.

This example below will change the expiry time of /var/www/html/deargodpleaseno/secret.zip to 1 hour.
              
.. code-block:: bash
   
   sudo dgpn --edit /var/www/html/deargodpleaseno/secret.zip --bestbefore 1
   
Specify a path for a directory or file that you wish to be removed from the deletion queue with --remove.
Does not require any additional parameters. The item removed from queue will not be deleted.
                
This example below will remove /var/www/html/deargodpleaseno/spice.png from deletion queue.

.. code-block:: bash

   sudo dgpn --remove /var/www/html/deargodpleaseno/spice.png

Back-end
--------
deargodpleaseno uses Linux's at.
It can be used to schedule commands in the future. The example below starts a package update in an hour.

.. code-block:: bash

   sudo at now + 1 hour
   at> sudo apt update && sudo apt upgrade -y
   at> <EOT>

deargodpleaseno can and probably will clog up your atq. Exert caution when removing atjobs.
To remember which atjobs are responsible for removing which items, an entries files exists under /etc/deargodpleaseno/entries which records items and their atjob number.
They are formatted as 0|||/var/www/html/deargodpleaseno/itemtobedeleted.html, 0 before the 3 pipes being the atjob ID number, and path afterwards the item in question.
If the entries and queue desync, reinstalling and clearing atq with atrm is the most efficient way of fixing it. Other options such as overwriting entries are possible, but aren't foolproof.
deargodpleaseno upon install will create its directory under the specified webroot. It will then append:

.. code-block:: 

   User-agent: *
   Disallow: /deargodpleaseno/

...To your robots.txt file. This will prevent webcrawlers that obey user-agent rules from indexing the newly created directory.
This of course isn't perfect, any webcrawlers that disregard user-agent rules or take several days or weeks to process new user-agent rules (looking at you SemRush bot) will render this ineffective.
It will create this rule even if the file does not exist, you are recommended to review your user-agent rules post-installation. The same goes for post-uninstallation.
