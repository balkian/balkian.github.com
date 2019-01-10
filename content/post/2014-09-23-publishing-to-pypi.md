---
title: Publishing on PyPi
date:   2014-09-27 10:00:00
tags:
  - github
  - python
  - pypi
---

Developing a python module and publishing it on Github is cool, but most
of the times you want others to download and use it easily. That is the
role of PyPi, the python package repository. In this post I show you how
to publish your package in less than 10 minutes.

Choose a fancy name
-------------------

If you haven't done so yet, take a minute or two to think about this.
To publish on PyPi you need a name for your package that isn't taken.
What's more, a catchy and unique name will help people remember your
module and feel more inclined to at least try it.

The package name should hint what your module does, but that's not
always the case. That's your call. I personally put uniqueness and
memorability over describing the functionality.

Create a .pypirc configuration file
-----------------------------------

```cfg
[distutils] # this tells distutils what package indexes you can push to
index-servers =
    pypi # the live PyPI
    pypitest # test PyPI

[pypi] # authentication details for live PyPI
repository = https://pypi.python.org/pypi
username = { your_username }
password = { your_password } # not necessary

[pypitest] # authentication details for test PyPI
repository = https://testpypi.python.org/pypi
username = { your_username }
```

As you can see, you need to register both in the [main pypi
repository](https://pypi.python.org/pypi?%3Aaction=register_form) and
the [testing
server](https://testpypi.python.org/pypi?%3Aaction=register_form). The
usernames and passwords might be different, that is up to you!

Prepare your package
--------------------

This should be the structure:

```
root-dir/    # Any name you want
    setup.py
    setup.cfg
    LICENSE.txt
    README.md
    mypackage/
        __init__.py
        foo.py
        bar.py
        baz.py
```

### setup.cfg

```cfg
[metadata]
description-file = README.md
```

The markdown README is the *de facto* standard in Github, but you can
also use rST (reStructuredText), the standard in the python community.

### setup.py

```python
from distutils.core import setup

setup(name = 'mypackage',
      packages = ['mypackage'], # this must be the same as the name above
      version = '{ version }',
      description = '{ description }',
      author = '{ name }',
      email = '{ email }',
      url = 'https://github.com/{user}/{package}', # URL to the github repo
      download_url = 'https://github.com/{user}/{repo}/tarball/{version}',
      keywords = ['websockets', 'display', 'd3'], # list of keywords that represent your package
      classifiers = [], )
```

You might notice that the download_url points to a Github URL. We could
host our package anywhere, but Github is a convenient option. To create
the tarball and the zip packages, you only need to tag a tag in your
repository and push it to github:

```bash
git tag {version} -m "{ Description of this tag/version}"
git push --tags origin master
```

Push to the testing/main pypi server
------------------------------------

It is advisable that you try your package on the test repository and fix
any problems first. The process is simple:

```shell
python setup.py register -r {pypitest/pypi} python setup.py sdist upload -r {pypitest/pypi}
```

If everything went as expected, you can now install your package through
pip and browse your package's page. For instance, check my senpy
package: <https://pypi.python.org/pypi/senpy>

```shell
pip install senpy
```
