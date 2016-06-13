#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

* File Name : get-list.py

* Purpose : Creating a new repository using Github API (PyGithub)

* Creation Date : 13-06-2016

* Copyright (c) 2016 Mandeep Singh <mandeeps708@gmail.com>

"""
from __future__ import print_function
from github import Github

# create your personal access token at https://github.com/settings/tokens and add one here.
token = ""

# Creating instance of main Github class. We may pass username as password as string arguments. May also be the Access token.
g = Github(token)

github_user = g.get_user()

# Name of the repository to be created at github_username account.
repository = "NameOfRepository"

# Repository creation.
repo = github_user.create_repo(repository)

# Even this repository has been created using this API.
print("Done!")
