#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

version = (1, 0, 0)

# import utils
from .iters import aggregate, count, bisect, index
from .iters import first, last, skip, skip_while, take, take_while, chunk, chain
from .iters import distinct_by, group_by, union_by, intersect_by, exclude_by

# import main class
from .linque import Linque
