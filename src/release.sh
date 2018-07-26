#!/usr/bin/env bash
rm -rf dist/
python setup.py register sdist
twine upload dist/*