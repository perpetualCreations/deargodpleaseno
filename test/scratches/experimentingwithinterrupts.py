"""
Testing to see if an interrupt will terminate the entire process or just a subprocess.
"""

from subprocess import call

call(input("press ctrl+c"))

print("if you're reading this...")
