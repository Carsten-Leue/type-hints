files = type_hints test *.py

test:
	pytest -s -v test/test_*.py --doctest-modules --cov type_hints --cov-config=.coveragerc --cov-report term-missing

lint:
	flake8 $(files)

fix:
	autopep8 --in-place -r $(files)

install:
	pip install -r requirements.txt -r test-requirements.txt

report:
	codecov

build: type_hints
	rm -rf dist
	python setup.py sdist bdist_wheel

publish:
	make build
	twine upload --config-file ~/.pypirc -r pypi dist/*

.PHONY: test
