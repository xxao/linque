#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

version = (4, 0, 2)

# import utils
from .iters import aggregate, bisect, chunk, concat, count
from .iters import argmax, argmin, argsort, index, multisort, rank
from .iters import first, last, single
from .iters import skip, skip_while, take, take_while
from .iters import distinct, exclude, group
from .iters import intersect, union

# import main class
from .linque import Linque


# create shortcuts
def linq(source, evaluate=False):
    """
    Initializes a new instance of Linque.
    
    Args:
        source: iterable
            Sequence of items.
        
        evaluate: bool
            If set to True, items sequence is evaluated into tuple upon
            class init and for each method call as well.
    """
    
    return Linque(source, evaluate)


linque = linq
