#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

version = (2, 0, 0)

# import utils
from .iters import aggregate, bisect, chunk, concat, count, index
from .iters import first, first_or_default, last, last_or_default, single
from .iters import skip, skip_while, take, take_while
from .iters import distinct, distinct_by, exclude, exclude_by, group, group_by
from .iters import intersect, intersect_by, union, union_by

# import main class
from .linque import Linque
