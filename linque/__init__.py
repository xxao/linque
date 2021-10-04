#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

version = (1, 0, 0)

# import utils
from .iters import aggregate, bisect, chunk, concat, count, index
from .iters import first, last, skip, skip_while, take, take_while
from .iters import distinct, exclude, group, intersect, union

# import main class
from .linque import Linque
