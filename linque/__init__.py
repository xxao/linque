#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

version = (3, 0, 0)

# import utils
from .iters import aggregate, bisect, chunk, concat, count
from .iters import argmax, argmin, argsort, index, rank
from .iters import first, last, single
from .iters import skip, skip_while, take, take_while
from .iters import distinct, exclude, group
from .iters import intersect, union

# import main class
from .linque import Linque
