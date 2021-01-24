# Finanzen_python_base
Base package for python services

[![Build Status](https://travis-ci.com/VaLena10012020/Finanzen_Entgelt.svg?branch=main)](https://travis-ci.com/VaLena10012020/Finanzen_python_base)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

## Development
### Prerequesites
run script to install requirements and configure pre-commit 
```
./setup_local.sh
```

### Tests and code quality

Run test suite with:
```sh
pytest
```

flake8 is implemented as a pre-commit hook. Hence, it is automatically conducted 
upon each commit. In addition, it is possible to trigger linting manually with the following command:
```
pre-commit run --all-files
```
