#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

* File Name : get-submodules.py

* Purpose : Fetching only sub-modules & corresponding details from a github repo.

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
print("Fetching repository details...")

# Iterations to fetch submodule entries and their info.
for x in repo.get_dir_contents(""):
    # if(x.type == "submodule"):
        # print(x.url)

    #Checks if the instance is a submodule, then fetches it's details. 
    if(x.raw_data.get("type") == "submodule"):
        print(x.name)
        print(x.raw_data.get("submodule_git_url"))
