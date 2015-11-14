import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name = "dburi",
        version = "3.3",
        author = "ruifengyun",
        author_email = "rfyiamcool@163.com",
        description = "use python parse database uri ,return format ",
        license = "MIT",
        keywords = ["database uri","fengyun"],
        url = "https://github.com/rfyiamcool",
        packages = find_packages(),
        long_description = read('README.md'),
        install_requires=['ConfigParser'],
        classifiers = [
             'Development Status :: 4 - Beta',
             'Intended Audience :: Developers',
             'License :: OSI Approved :: MIT License',
             'Programming Language :: Python :: 2.7',
             'Programming Language :: Python :: 3.0',
             'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)

