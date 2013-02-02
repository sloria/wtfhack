""" Settings for wtfhack """

from .base import *
try:
    from .local import *
except ImportError, exc:
    print '%s (did you rename settings/local-dist.py?)' % exc.args[0]