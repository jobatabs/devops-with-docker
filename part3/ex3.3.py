#!/usr/bin/python3

import os
import subprocess
import sys

subprocess.run(["git", "clone", f"https://github.com/{sys.argv[1]}.git", "dest"])

os.chdir("dest")

subprocess.run(["docker", "buildx", "build", ".", "-t", sys.argv[2]])

subprocess.run(["docker", "push", sys.argv[2]])
