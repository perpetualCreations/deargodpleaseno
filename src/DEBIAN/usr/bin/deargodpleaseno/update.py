"""
deargodpleaseno, revision 1.0

update.py, does the following:
- check github repository for new releases
"""

import requests

if "1.0" not in requests.get("https://github.com/perpetualCreations/deargodpleaseno/releases/latest", allow_redirects = True).url:
    print("New update available, please see github.com/perpetualCreations/deargodpleaseno/releases/latest.")
pass
