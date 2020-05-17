import os
from setuptools import setup, find_packages

NAME = 'pylearn'
DESCRIPTION = 'My python learn'
AUTHOR = 'HyperAndy'
EMAIL = 'hitwangzijian@163.com'
URL = ''
PYTHON_REQUIRES = '>=3.6.0'
VERSON = '0.0.1'
LISENSE = 'License :: OSI Approved :: Apache Software License'

# What packages are required for this module to be executed?
REQUIRED = [
    # 'xxx', 'xxx', 'xxx',
    'argparse', 'easydict', 'torch'
]

# What packages are optional?
EXTRAS = {
    # 'feature': ['xxx'],
}

# cli tools function
ENTRY_POINTS = {
    # 'console_scripts': ['pylearn = xxx'],
}

# define version
if os.path.exists(os.path.join(os.path.dirname(__file__), 'VERSION')):
    # print(__file__)
    with open(os.path.join(os.path.dirname(__file__), 'VERSION'), 'rb') as f:
        VERSION = f.read().decode('ascii').strip()

setup(
    name=NAME,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    license=LISENSE,
    package=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires=PYTHON_REQUIRES,
    install_requires=REQUIRED,
    entry_points=ENTRY_POINTS,
)
