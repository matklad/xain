#!/usr/bin/env python
"""When executed as:
$ ./scripts/get_requires_from_setup.py [extra_require.keys]
The required dependencies as well one or more selected `extra_require`
will be printed. This is used in our docker build process
"""

import distutils.core
import sys
from os.path import abspath, dirname, realpath

dir_path = dirname(realpath(__file__))
setup_py_path = abspath(dir_path + "/../setup.py")

# Extract arguments and than set them to just the file itself
# as otherwise some scripts might be triggered through the
# distutils.core.run_setup call
args = sys.argv[1:]
sys.argv = sys.argv[:1]

setup = distutils.core.run_setup(setup_py_path)

if not set(args).issubset(set(setup.extras_require)):
    print(f"Valid choices are none up to all of: {set(setup.extras_require)}")
    exit(1)

all_requires = setup.install_requires

for extra in args:
    all_requires += setup.extras_require[extra]

print(" ".join(set(all_requires)))
