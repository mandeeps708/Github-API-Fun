#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

* File Name : get-list.py

* Purpose : Fetch file list using Github API (PyGithub)

* Creation Date : 13-06-2016

* Copyright (c) 2016 Mandeep Singh <mandeeps708@gmail.com>

"""
from __future__ import print_function
from github import Github

# Creating instance of main Github class. We may pass username as password as string arguments.
g = Github()

github_username = "FreeCAD"

# Name of the repository residing at github_username account.
repository = "FreeCAD-addons"

# Repository instance.
repo = g.get_user(github_username).get_repo(repository)

# Iterations to fetch file names of the repository.
for x in repo.get_dir_contents(""):
    print(x.name)
