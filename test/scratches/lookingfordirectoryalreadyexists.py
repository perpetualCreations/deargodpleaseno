"""
Testing for error that occurs if mkdir is targeting a directory that already exists.
"""

from os import mkdir
mkdir("testdir")
