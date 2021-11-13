# My Implemented Package

Practice of development and deploy codes. 😄 <br>
This repo will be used to create a package by refering this structure.

Anyone can be install this library from pypi from this link: https://pypi.org/project/mipack/

```
pip install mipack
```

Q. How to manage packages? see from <a href="https://www.youtube.com/watch?v=Motr7UunBT4&list=PLjAFBrXBY3g59hczbnFa-xu1Tqrtzh1Yn&index=1&t=9s" target="_blank"><img src="https://img.shields.io/badge/YouTube-Dol AI-white?style=plastic&logo=youtube&logoColor=red"/>


## Tools 

Used tools as follows. 🔥

- [x] [github action](https://github.com/features/actions): continuous integration.
- [x] [sphinx](https://www.sphinx-doc.org/en/master): document is created along with package codes.
- [ ] [streamlit](https://streamlit.io/): streaming dashboard for exploration.
- [ ] [wandb](https://wandb.ai/site): daashboard for states of models.


## Deploy

Deploy to pypi as follows. 🥳
```
# setup.py version up
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
