---
date: '2023-11-13T18:21:46+01:00'
title: 'Nix Recipe for Python Projects'
tags:
 - nix
 - python
---


This is a quick and easy recipe to add a `default.nix` to any Python project with a `requirements.txt` file:

<!--more-->

```nix
with import <nixpkgs> { };

let
  pythonPackages = python311Packages;
in pkgs.mkShell rec {
  name = "impurePythonEnv";
  venvDir = "./.venv";
  buildInputs = [
    # A python interpreter including the 'venv' module is required to bootstrap
    # the environment.
    pythonPackages.python

    # This execute some shell code to initialize a venv in $venvDir before
    # dropping into the shell
    pythonPackages.venvShellHook

    # Those are dependencies that we would like to use from nixpkgs, which will
    # add them to PYTHONPATH and thus make them accessible from within the venv.
    pythonPackages.numpy
    pythonPackages.requests

    # In this particular example, in order to compile any binary extensions they may
    # require, the python modules listed in the hypothetical requirements.txt need
    # the following packages to be installed locally:
    taglib
    openssl
    git
    libxml2
    libxslt
    libzip
    zlib
  ];

  # Now we can execute any commands within the virtual environment.
  # This is optional and can be left out to run pip manually.
  postShellHook = ''
    pip install -r requirements.txt
  '';

}
```


Now, you will get a clean environment by running:

```
nix-shell
```
