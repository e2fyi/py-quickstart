force_reload:

dev:
	pipenv install --dev
	pipenv run pip install -e .

dists: requirements sdist bdist wheels

docs: force_reload
	sphinx-build rst docs -b dirhtml -E -P

requirements:
	pipenv run pipenv_to_requirements

sdist: requirements
	pipenv run python setup.py sdist

bdist: requirements
	pipenv run python setup.py bdist

wheels: requirements
	pipenv run python setup.py bdist_wheel

publish: dists
	twine upload --verbose --disable-progress-bar dist/*

format:
	docformatter --in-place {{cookiecutter.namespace}}/**/*.py
	isort {{cookiecutter.namespace}} -rc
	black {{cookiecutter.namespace}}

check:
	isort {{cookiecutter.namespace}} -rc -c
	black --check {{cookiecutter.namespace}}
	pylint {{cookiecutter.namespace}}
	flake8
	mypy {{cookiecutter.namespace}}
	pydocstyle
	bandit -r {{cookiecutter.namespace}}

test: check
	pytest --cov={{cookiecutter.namespace}}

test-all: test dists
	twine check dist/*

test-only: env
	pytest --cov={{cookiecutter.namespace}}
