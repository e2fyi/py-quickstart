#!/usr/bin/env python
# noqa
# pylint: skip-file
"""The setup script."""

from setuptools import setup

with open("requirements.txt", "r") as filein:
    requirements = filein.readlines()

with open("requirements-dev.txt", "r") as filein:
    requirements_dev = filein.readlines()

with open("version.txt", "r") as filein:
    version = filein.read()

with open("README.md", "r") as filein:
    readme = filein.read()

setup_requirements: list = [
    "setuptools >= 41.0.0",
    "wheel >= 0.26",
]

setup(
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="{{cookiecutter.package_desc}}",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="",
    include_package_data=True,
    package_data={"": ["version.txt", "requirements.txt", "requirements-dev.txt"]},
    keywords="{{cookiecutter.package_keywords}}",
    name="{{cookiecutter.package_name}}",
    packages=["{{cookiecutter.namespace}}.{{cookiecutter.module_name}}"],
    setup_requires=setup_requirements,
    python_requires=">=3.6",
    install_requires=requirements,
    tests_require=requirements_dev,
    version=version,
)
