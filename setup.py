#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

from setuptools import setup, find_packages

# get version
from linque import version
version = '.'.join(str(x) for x in version)

# get description
with open("README.md", "r") as fh:
    long_description = fh.read()

# set classifiers
classifiers = [
    'Development Status :: 4 - Beta',
    'Programming Language :: Python :: 3 :: Only']

# main setup
setup(
    name = 'linque',
    version = version,
    description = 'Linear Query - Python replica of popular .NET LINQ utilities.',
    long_description = long_description,
    url = 'https://github.com/xxao/linque',
    author = 'Martin Strohalm',
    author_email = '',
    license = 'MIT',
    packages = find_packages(),
    classifiers = classifiers,
    zip_safe = False)
