# My Implemented Package

Practice of development and deploy codes.
This repo will be used to create a package by refering this structure.

Anyone can be install this library from pypi from this link: https://pypi.org/project/mipack/

```
pip install mipack
```

## Tools

Used tools as follows.

* [github action](https://github.com/features/actions): continuous integration.
* [sphinx](https://www.sphinx-doc.org/en/master): document is created along with package codes.
* [streamlit](https://streamlit.io/): streaming dashboard for exploration.
* [wandb](https://wandb.ai/site): daashboard for states of models.


## Deploy

Deploy to pypi as follows.
```
# setup.py version up
# doc/conf.py version up
python setup.py bdist_wheel
python -m twine upload dist/*.whl
```

## Documentation

Update documentation using sphinx.
```
sphinx-apidoc -f -o docs mipack
```

Serving the documetation.
```
sphinx-autobuild --host [IP] --port [PORT] docs docs/_build/html
```
