from distutils.core import setup 
from setuptools import find_packages


with open("pypi_readme.rst", "r") as f:
    long_description = f.read()

# Package meta-data.
NAME = "pyprecip"
DESCRIPTION = "A climate data processing library."
URL = "https://github.com/ma0513207162/pyprecip"
EMAIL = "ma0513207162@163.com"
AUTHOR = "hasang"
REQUIRES_PYTHON = '>=3.7.0'
VERSION = '0.0.1'

# What packages are required for this module to be executed?
REQUIRED = [
    # 'requests', 'maya', 'records',
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

setup(
    name = NAME, 
    version = VERSION, 
    description = DESCRIPTION, 
    long_description = long_description, 
    author = AUTHOR, 
    author_email = EMAIL, 
    python_requires = REQUIRES_PYTHON, 
    url = URL, 
    packages = find_packages(), 
    install_requires = REQUIRED,
    extras_require = EXTRAS,
    include_package_data = True,
    license = "MIT", 
                
    classifiers = [
        'License :: OSI Approved :: MIT License',         
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries'
    ]
)


