"""
Small task to test tqdm
"""

import requests

print(requests.get("https://dreamerslegacy.xyz/index.html").text)