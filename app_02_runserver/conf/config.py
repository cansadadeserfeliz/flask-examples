import sys

DEBUG = False

try:
    if 'test' in sys.argv:
        from test_config import *
    else:
        from local_config import *

except ImportError, e:
    pass