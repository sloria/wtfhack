""" Settings for wtfhack """

from .base import *
try:
    from .local import *
except ImportError, exc:
    exc.args = tuple(
        ['%s (did you rename settings/local-dist.py?)' % exc.args[0]])
    raise exc
