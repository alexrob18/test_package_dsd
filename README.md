# dsd_package_test

[![PyPI](https://img.shields.io/pypi/v/dsd_package_test.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/dsd_package_test.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/dsd_package_test)][pypi status]
[![License](https://img.shields.io/pypi/l/dsd_package_test)][license]

[![Read the documentation at https://dsd_package_test.readthedocs.io/](https://img.shields.io/readthedocs/dsd_package_test/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/alexrob18/dsd_package_test/actions/workflows/python-test.yml/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/alexrob18/dsd_package_test/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/dsd_package_test/
[read the docs]: https://dsd_package_test.readthedocs.io/
[tests]: https://github.com/alexrob18/dsd_package_test/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/alexrob18/dsd_package_test
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Installation

You can install _dsd_package_test_ via [pip] from [PyPI]:

```console
$ pip install dsd_package_test
```

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide][Contributor Guide].

## License

Distributed under the terms of the [Apache 2.0 license][License],
_dsd_package_test_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue][Issue Tracker] along with a detailed description.


<!-- github-only -->

[command-line reference]: https://dsd_package_test.readthedocs.io/en/latest/usage.html
[License]: https://github.com/alexrob18/dsd_package_test/blob/main/LICENSE
[Contributor Guide]: https://github.com/alexrob18/dsd_package_test/blob/main/CONTRIBUTING.md
[Issue Tracker]: https://github.com/alexrob18/dsd_package_test/issues


## Building the Documentation

You can build the documentation locally by installing the documentation Conda environment:

```bash
conda env create -f docs/environment.yml
```

activating the environment

```bash
conda activate sphinx_dsd_package_test
```

and [running the build command](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#sphinx-build):

```bash
sphinx-build docs _build/html --builder=singlehtml --jobs=auto --write-all; open _build/html/index.html
```