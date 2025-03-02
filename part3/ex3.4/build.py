#!/usr/bin/python3

import os
import subprocess
import sys

print(f"Cloning repo git@github.com:{sys.argv[1]}.git to /usr/src/app/dest")

subprocess.run(["git", "clone", f"https://github.com/{sys.argv[1]}.git", "/usr/src/app/dest"])

print(f"Changing to cloned repo directory {os.getcwd()}/dest")

os.chdir(os.getcwd() + "/dest")

print(f"Build image with tag {sys.argv[2]}")

subprocess.run(["docker", "buildx", "build", ".", "-t", sys.argv[2]])

subprocess.run(["docker", "login", "-u", os.environ["DOCKER_USER"], "-p", os.environ["DOCKER_PWD"]])

subprocess.run(["docker", "push", sys.argv[2]])
