---
title: Python
description: Tips and useful libraries for python developers
image: "img/python.png"
categories:
  - programming
tags:
  - python
  - programming
---

## Interesting libraries

### [TQDM](https://github.com/tqdm/tqdm)


From tqdm's github repository:

> tqdm means "progress" in Arabic (taqadum, تقدّم) and an abbreviation for "I love you so much" in Spanish (te quiero demasiado).


 ![TQDM in action](https://raw.githubusercontent.com/tqdm/tqdm/master/images/tqdm.gif)

## Tools

### [uv](https://github.com/astral-sh/uv)

🚀 A single tool to replace pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, and more.
⚡️ 10-100x faster than pip.
* Provides comprehensive project management, with a universal lockfile.
* Runs scripts, with support for inline dependency metadata.
* Installs and manages Python versions.
* Runs and installs tools published as Python packages.
* Includes a pip-compatible interface for a performance boost with a familiar CLI.
* Supports Cargo-style workspaces for scalable projects.
* Disk-space efficient, with a global cache for dependency deduplication.
* Installable without Rust or Python via curl or pip.
* Supports macOS, Linux, and Windows.

### [pipdeptree](https://pypi.org/project/pipdeptree/)

A tool to generate a dependency tree from a virtualenv.

Useful to generate a clean `requirements.txt` or to clean up one that was generated with `pip freeze`.
Usage:

```
$ pipdeptree --exclude pip,pipdeptree,setuptools,wheel --warn silence | grep -E '^\w+' | tee requirements-clean.txt
Flask==0.10.1
gnureadline==8.0.0
Lookupy==0.1
pipdeptree==2.0.0b1
setuptools==47.1.1
wheel==0.34.2
```
