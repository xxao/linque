#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

from itertools import islice


def aggregate(sequence, func, seed=None):
    """
    Applies accumulator function over a sequence.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        func: callable
            Accumulator function expecting two arguments (res, next).
        
        seed: any
            Initial aggregation value. If set to None, the first item is
            used.
    
    Returns:
        any
    """
    
    res = seed
    
    for i, item in enumerate(sequence):
        if i == 0 and seed is None:
            res = item
            continue
        res = func(res, item)
    
    return res


def bisect(sequence, value, key=None, side='left'):
    """
    Uses binary search to find index where if given value inserted, the order
    of items is preserved. The collection of items is assumed to be sorted in
    ascending order. In fact it gives the index of first equal or next higher
    value.
    
    Args:
        sequence: list or tuple
            Collection of items ordered by searched value.
        
        value: int or float
            Value to be searched.
        
        key: callable or None
            Function to be used to get specific value from item.
        
        side: str
            If 'left' is used, index of the first suitable location is
            returned. If 'right' is used, the last such index is returned.
    
    Returns:
        int
            Index of the exact or next higher item.
    """
    
    has_key = key is not None
    lo = 0
    hi = len(sequence)
    
    if side == 'left':
        while lo < hi:
            mid = (lo + hi) // 2
            if value <= (key(sequence[mid]) if has_key else sequence[mid]):
                hi = mid
            else:
                lo = mid + 1
    
    elif side == 'right':
        while lo < hi:
            mid = (lo + hi) // 2
            if value < (key(sequence[mid]) if has_key else sequence[mid]):
                hi = mid
            else:
                lo = mid + 1
    
    else:
        message = "Unknown side specified! -> '%s'" % side
        raise ValueError(message)
    
    return lo


def chunk(sequence, size):
    """
    Splits sequence into chunks of specified size.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        size: int
            Maximum size of each chunk.
    
    Returns:
        iter((any,),)
            Iterator over items chunks.
    """
    
    items = (d for d in sequence)
    return iter(lambda: tuple(islice(items, size)), ())


def concat(*sequences):
    """
    Chains given sequences into a single sequence.
    
    Args:
        sequences: iterable
            Sequences to be chained.
    
    Returns:
        iter(any)
            Iterator over all items.
    """
    
    for sequence in sequences:
        for item in sequence:
            yield item


def count(sequence, condition=None):
    """
    Returns number of item in a sequence satisfying given condition.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        condition: callable or None
            Condition to test.
    
    Returns:
        int
            Number of valid items.
    """
    
    if condition is None:
        return sum(1 for _ in sequence)
    
    return sum(1 for d in sequence if condition(d))


def distinct(sequence, key=None):
    """
    Iterates over distinct items in a sequence by using default comparer or
    specified item's key. First occurrence of each item is used.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        key: callable
            Item's key selector.
    
    Returns:
        iter(any)
            Iterator over distinct items.
    """
    
    has_key = key is not None
    seen = set()
    
    for item in sequence:
        k = key(item) if has_key else item
        
        if k not in seen:
            seen.add(k)
            yield item


def exclude(sequence, items, key=lambda d: d):
    """
    Excludes specified items from a sequence by using default comparer or
    selected item's key.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        items: iterable
            Items to exclude.
        
        key: callable
            Item's key selector.
    
    Returns:
        iter(any)
            Iterator over remaining items.
    """
    
    has_key = key is not None
    keys = set((key(d) if has_key else d for d in items))
    
    for item in sequence:
        k = key(item) if has_key else item
        
        if k not in keys:
            yield item


def first(sequence, condition=None, default=None):
    """
    Returns the first item in a sequence that satisfies specified condition or
    specified default value if no item found.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        condition: callable
            Condition to test.
        
        default: any
            Default value.
    
    Returns:
        any
            First valid item.
    """
    
    if condition is None:
        return next((d for d in sequence), default)
    
    return next((d for d in sequence if condition(d)), default)


def group(sequence, key=None):
    """
    Groups sequence of a sequence according to specified key selector and creates
    result values as (key, group) pairs.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        key: callable
            Item's key selector.
    
    Returns:
        ((any, (any,)),)
            Grouped items as (key, group) pairs.
    """
    
    has_key = key is not None
    keys = []
    groups = {}
    
    for item in sequence:
        k = key(item) if has_key else item
        
        if k not in groups:
            keys.append(k)
            groups[k] = []
        
        groups[k].append(item)
    
    return [(k, tuple(groups[k])) for k in keys]


def index(sequence, condition):
    """
    Returns index of the first item in a sequence that satisfies specified
    condition.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        condition: callable
            Condition to test.
    
    Returns:
        int
            Index of the first valid item.
    """
    
    for i, item in enumerate(sequence):
        if condition(item):
            return i
    
    raise ValueError()


def intersect(sequence, items, key=lambda d: d):
    """
    Produces a sequence of shared unique items from given sequences by using
    default comparer or selected item's key.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        items: iterable
            Items to intersect with.
        
        key: callable
            Item's key selector.
    
    Returns:
        iter(any)
            Iterator over intersecting items.
    """
    
    has_key = key is not None
    keys = set((key(d) if has_key else d for d in items))
    
    for item in sequence:
        k = key(item) if has_key else item
        
        if k in keys:
            keys.remove(k)
            yield item


def last(sequence, condition=None, default=None):
    """
    Returns the last item in a sequence that satisfies specified condition or
    specified default value if no item found.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        condition: callable
            Condition to test.
        
        default: any
            Default value.
    
    Returns:
        any
            Last valid item.
    """
    
    sequence = reversed(list(sequence))
    
    return first(sequence, condition, default)


def skip(sequence, n):
    """
    Bypasses specified number of items in a sequence and returns the remaining
    items.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        n: int
            Number of items to skip.
    
    Returns:
        iter(any)
            Iterator over remaining items.
    """
    
    return (d for i, d in enumerate(sequence) if i >= n)


def skip_while(sequence, condition):
    """
    Bypasses contiguous items from the start of a sequence until specified
    condition fails the first time.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        condition: callable
            Condition to test.
    
    Returns:
        iter(any)
            Iterator over taken items.
    """
    
    failed = False
    for item in sequence:
        if not failed:
            failed = not condition(item)
            if not failed:
                continue
        
        yield item


def take(sequence, n):
    """
    Selects specified number of contiguous items from the start of a sequence.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        n: int
            Number of items to take.
    
    Returns:
        iter(any)
            Iterator over taken items.
    """
    
    items = (d for d in sequence)
    
    i = 0
    while i < n:
        yield next(items)
        i += 1


def take_while(sequence, condition):
    """
    Selects contiguous items from the start of a sequence until specified
    condition fails.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        condition: callable
            Condition to test.
    
    Returns:
        iter(any)
            Iterator over taken items.
    """
    
    for item in sequence:
        if condition(item):
            yield item
        else:
            return


def union(sequence, items, key=None):
    """
    Produces a sequence of unique items from given sequences by using default
    comparer or selected item's key.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        items: iterable
            Items to union with.
        
        key: callable
            Item's key selector.
    
    Returns:
        iter(any)
            Iterator over unionized items.
    """
    
    has_key = key is not None
    keys = set()
    
    for item in concat(sequence, items):
        k = key(item) if has_key else item
        
        if k not in keys:
            keys.add(k)
            yield item
