#!/usr/bin/python

import shlex, subprocess, sys, importlib

# This function runs shlex.split on each command in a given list of apprun dictionaries
# See python docs for shlex for more details
def shlex_apprun_list(l):
    for i in l:
        i["command"] = shlex.split(i["command"])
    return l

if sys.argv[0] == 'python':
    pyfile = sys.argv[2]
else:
    pyfile = sys.argv[1]

if pyfile.endswith(".py"):
    module = pyfile[:-3]
else:
    module = pyfile

usermodule = importlib.import_module(module)

singlerun = shlex_apprun_list(usermodule.singlerun)

for i in singlerun:
    i['process'] = subprocess.Popen(i['command'])
    if not i['asynchronous']:
        i['process'].wait()
