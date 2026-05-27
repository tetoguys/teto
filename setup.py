import re
from setuptools import setup, find_packages
from os import path

PACKAGE_NAME = "teto"
HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "README.md"), "r", encoding="utf-8") as f:
    README = f.read()

with open(path.join(HERE, "requirements.txt"), "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

with open(path.join(HERE, PACKAGE_NAME, "__init__.py"), encoding="utf-8") as fp:
    VERSION = re.search('__version__ = "([^"]+)"', fp.read()).group(1)


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author="woohyun_jng",
    author_email="woohyun.jng08@gmail.com",
    description="Unofficial wrapper for tetr.io API",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/tetoguys/teto",
    install_requires=requirements,
    packages=find_packages(exclude=[]),
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
