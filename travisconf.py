# settings needed to build on Travis-CI

import os
import sys
sys.path.append(os.curdir)
from publishconf import *

# I think we are having issues with going outside of our root directory.
OUTPUT_PATH = 'output/'  # default
