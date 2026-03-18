"""
Init file for CIFT.
Used for namespace flattening.
"""

from cift import err
from cift import types
from cift.parser import Symbol
from cift.parser import Seq
from cift.parser import Or
from cift.parser import Maybe
from cift.parser import Many
from cift.parser import CSTNode
from cift.parser import Parser
import cift.grammar
import cift.astextra
import cift.semir
import cift.debug
from cift.shorthand import parse
from cift.shorthand import parse_string

# The function of `__all__` is:
#
# 0. To tell Python what precisely to import when
#   someone calls `from cift import *`
#   (we don't really care about this)
#
# 1. To tell Ruff that the imports above are here for
#   namespace flattening, and not useless
#
# 2. To tell MyPy that we WANT users of cift to access these
#   objects, that they are meant to be public and not some
#   internal implementation detail.
#
# HINT: instead of manually copy-pasting,
# HINT: use `scripts/patch_init.py`
# HINT: to fill out this field

__all__ = [
    "err",
    "types",
    "Symbol",
    "Seq",
    "Or",
    "Maybe",
    "Many",
    "CSTNode",
    "Parser",
    "grammar",
    "astextra",
    "semir",
    "debug",
    "parse",
    "parse_string",
    ]

