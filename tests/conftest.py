import sys
from os.path import *

HERE = abspath(dirname(__file__))
SRC_DIR = abspath(join(dirname(__file__),'..','app'))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)