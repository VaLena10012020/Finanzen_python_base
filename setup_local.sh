#!/bin/bash
pip install -r requirements/dev.txt
pre-commit install
pre-commit autoupdate
