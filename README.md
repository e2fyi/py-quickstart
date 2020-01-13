# e2fyi/py-quickstart

This is an opininated [cookiecutter](https://cookiecutter.readthedocs.io/)
project template for a namespaced python package.

```bash
# install cookiecutter
pip install cookiecutter

# create a new project folder with the template
cookiecutter git+ssh://git@github.com/e2fyi/py-quickstart.git
```

> ### Important cookiecutter params:
>
> `python_version`: general python version to use (e.g. 2.7, 3.6, or 3.7) - this is use for `mypy`, `black`, etc.
> `pyenv_python_version`: specific python version to use (e.g. 3.7.4) - this is use to setup the pyenv environment (use `pyenv install --list` to see the list of available python).

## Overview

It provides a `Makefile` to run some of the common tasks (e.g. format, test):

```bash
# autoformat codes with docformatter, isort, and black
make format

# check style, formats, and code complexity
make check

# check style, formats, code complexity, and run unit tests
make test

# test everything including building the package and check the sdist
make test-all

# run unit test only
make test-only

# generate and update the requirements.txt and requirements-dev.txt
make requirements

# generate the docs with sphinx and autoapi extension
make docs

# generate distributions
make dists

# publish to pypi with twine (twine must be configured)
make publish
```

[`pipenv`](https://pipenv-fork.readthedocs.io/en/latest/) is also the package
manager used for this project template. It is recommended for the `venv` to be
created inside the project folder (set env variable `PIPENV_VENV_IN_PROJECT=1`
to enable this).

Optionally, it is also recommended to setup [`pyenv`](https://github.com/pyenv/pyenv)
and [`direnv`](https://direnv.net/) for your dev environment:

- `pyenv`: to manage different version of pythons
- `direnv`: to manage and load profiles for each project directory

This is an example workflow to setup your project env after creating the project
folder with the cookiecutter template:

```bash
# enter project folder
cd <package_name>

# check active pyenv python version
pyenv version

# if you get message like "pyenv: version `X.X.X' is not installed"
# install appropriate python version with pyenv
pyenv install --list                # see list of available python versions
pyenv install <python_version>      # install the stated python version

# install pipenv if not installed
pip install pipenv

# setup venv with pipenv using the active pyenv python
pipenv install --python=$(pyenv which python)

# enable direnv - i.e. pipenv venv will be automatically loaded when you
# enters the project folder
direnv allow

# if needed, reload the profile
direnv reload
```

[`black`](https://black.readthedocs.io/en/stable/) is selected as the main code
formatter.
