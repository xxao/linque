#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

from itertools import islice

UNDEFINED = object()


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


def argmax(sequence, key=None):
    """
    Returns index of the maximum item in a sequence by using default comparer
    or specified item's key.
    
    Args:
        sequence: iterable
            Sequence of items to sort.
        
        key: callable or None
            Item's key selector.
    
    Returns:
        int
            Index of the maximum item.
    """
    
    items = [key(d) for d in sequence] if key is not None else sequence
    
    if not hasattr(items, '__len__'):
        items = list(items)
    
    return max(range(len(items)), key=items.__getitem__)


def argmin(sequence, key=None):
    """
    Returns index of the minimum item in a sequence by using default comparer
    or specified item's key.
    
    Args:
        sequence: iterable
            Sequence of items to sort.
        
        key: callable or None
            Item's key selector.
    
    Returns:
        int
            Index of the minimum item.
    """
    
    items = [key(d) for d in sequence] if key is not None else sequence
    
    if not hasattr(items, '__len__'):
        items = list(items)
    
    return min(range(len(items)), key=items.__getitem__)


def argsort(sequence, key=None, reverse=False):
    """
    Returns items indices that would sort a sequence by using default comparer
    or specified item's key.
    
    Args:
        sequence: iterable
            Sequence of items to sort.
        
        key: callable or None
            Item's key selector.
        
        reverse: bool
            If set to True, sorting is reversed.
    
    Returns:
        (int,)
            Indexes of sorted items.
    """
    
    items = [key(d) for d in sequence] if key is not None else sequence
    
    if not hasattr(items, '__len__'):
        items = list(items)
    
    return sorted(range(len(items)), key=items.__getitem__, reverse=reverse)


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
        
        key: callable or None
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


def exclude(sequence, items, key=None):
    """
    Excludes specified items from a sequence by using default comparer or
    specified item's key.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        items: iterable
            Items to exclude.
        
        key: callable or None
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


def first(sequence, condition=None, default=UNDEFINED):
    """
    Returns the first item in a sequence that satisfies specified condition or
    raises error if no item found and no default value is provided.
    
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
    
    if condition is not None:
        items = (d for d in sequence if condition(d))
    else:
        items = (d for d in sequence)
    
    if default is not UNDEFINED:
        return next(items, default)
    
    return next(items)


def group(sequence, key=None):
    """
    Groups items of a sequence according to default comparer or specified
    item's key and creates result values as (key, group) pairs.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        key: callable or None
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
    
    i = -1
    for item in sequence:
        i += 1
        if condition(item):
            return i
    
    raise ValueError()


def intersect(sequence, items, key=None):
    """
    Produces a sequence of shared unique items from given sequences by using
    default comparer or specified item's key.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        items: iterable
            Items to intersect with.
        
        key: callable or None
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


def last(sequence, condition=None, default=UNDEFINED):
    """
    Returns the last item in a sequence that satisfies specified condition or
    raises error if no item found and no default value is provided.
    
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
    
    if condition is not None:
        items = (d for d in sequence if condition(d))
    else:
        items = (d for d in sequence)
    
    item = default
    for item in items:
        pass
    
    if item is UNDEFINED:
        raise StopIteration
    
    return item


def multisort(sequence, key=None, reverse=False, _n=0):
    """
    Produces new sequence by sorting elements of current sequence by using
    default comparer or specified item's key. If the key provides multiple
    columns, the sorting direction can be specified for each individual column.
    
    Args:
        sequence: iterable
            Sequence of items to sort.
        
        key: callable or None
            Item's key selector.
        
        reverse: bool or (bool,)
            If set to True, sorting is reversed. This flag can be specified
            independently foreach key column.
    
    Returns:
        list(any)
            Sorted sequence.
    """
    
    # simple sort
    if reverse is True or reverse is False:
        return sorted(sequence, key=key, reverse=reverse)
    
    # initial sort
    sequence = sorted(sequence, key=key, reverse=reverse[_n])
    
    # no need for further sorts
    if len(sequence) < 2 or all(reverse[_n:]) or not any(reverse[_n:]):
        return sequence
    
    # get keys
    keys = sequence if key is None else list(map(key, sequence))
    
    # re-sort same keys
    final = []
    i = 0
    while i < len(keys):
        
        # get same
        k = keys[i][:_n+1]
        j = i+1
        while j < len(keys) and k == keys[j][:_n+1]:
            j += 1
        
        # sort same
        if j - i > 1:
            final += multisort(sequence[i:j], key, reverse, _n+1)
        else:
            final.append(sequence[i])
        
        i = j
    
    return final


def rank(sequence, key=None, method='average', reverse=False):
    """
    Provides 1-based rank for each item of a sequence by using default
    comparer or specified item's key. The ties are resolved according to
    selected method.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        key: callable or None
            Item's key selector.
        
        method: str
            Method used to assign ranks to tied items.
                'average' - tied values are assigned by their average rank
                'min' - tied values are assigned by their minimum rank
                'max' - tied values are assigned by their maximum rank
                'dense' - like 'min' but without rank gaps
                'ordinal' - distinct rank for all values
        
        reverse: bool
            If set to True, sorting is reversed.
    
    Returns:
        (int,)
            Items' ranks.
    """
    
    items = [key(d) for d in sequence] if key is not None else sequence
    
    if not hasattr(items, '__len__'):
        items = list(items)
    
    size = len(items)
    idxs = sorted(range(size), key=items.__getitem__, reverse=reverse)
    
    items = [items[r] for r in idxs]
    ranks = [0]*size
    
    dupls = 0
    sums = 0
    lost = 0
    
    if method == 'average':
        for i in range(size):
            dupls += 1
            sums += i
            if i == size - 1 or items[i] != items[i + 1]:
                for j in range(i - dupls + 1, i + 1):
                    ranks[idxs[j]] = sums / dupls + 1
                dupls = 0
                sums = 0
    
    elif method == 'min':
        for i in range(size):
            dupls += 1
            if i == size - 1 or items[i] != items[i + 1]:
                for j in range(i - dupls + 1, i + 1):
                    ranks[idxs[j]] = i + 1 - dupls + 1
                dupls = 0
    
    elif method == 'max':
        for i in range(size):
            dupls += 1
            if i == size - 1 or items[i] != items[i + 1]:
                for j in range(i - dupls + 1, i + 1):
                    ranks[idxs[j]] = i + 1
                dupls = 0
    
    elif method == 'dense':
        for i in range(size):
            dupls += 1
            sums += i
            if i == size - 1 or items[i] != items[i + 1]:
                for j in range(i - dupls + 1, i + 1):
                    ranks[idxs[j]] = i + 1 - lost
                dupls = 0
            else:
                lost += 1
    
    elif method == 'ordinal':
        for i in range(size):
            ranks[idxs[i]] = i + 1
    
    return ranks


def single(sequence, condition=None, default=UNDEFINED):
    """
    Returns the single item in a sequence that satisfies specified condition or
    raises error if more items found. If no item is found, returns default
    value if provided or raises error.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        condition: callable
            Condition to test.
        
        default: any
            Default value.
    
    Returns:
        any
            Single valid item.
    """
    
    items = [d for d in sequence if condition(d)] if condition is not None else sequence
    
    if not hasattr(items, '__len__'):
        items = list(items)
    
    if len(items) == 1:
        return items[0]
    
    if len(items) == 0 and default is not UNDEFINED:
        return default
    
    raise ValueError


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
    comparer or specified item's key.
    
    Args:
        sequence: iterable
            Sequence of items to go through.
        
        items: iterable
            Items to union with.
        
        key: callable or None
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
