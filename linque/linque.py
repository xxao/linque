#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import statistics
import random
from . import iters


class Linque(object):
    """
    Linque provides a functionality similar to .NET LINQ (Language Integrated
    Query) and IEnumerable. It allows chaining multiple queries on a sequence of
    items, mostly without evaluating the sequence until necessary. Therefore,
    each linq chain can only be called once to get a final result. To break this
    logic, the class can be initialized with 'evaluate' parameter set to True,
    to make sure all input data are stored as fully evaluated sequence such as
    list. A linq chain can then be reused for the cost of keeping all internal
    steps in memory as a list.
    """
    
    def __init__(self, source, evaluate=False):
        """
        Initializes a new instance of Linque.
        
        Args:
            source: iterable
                Sequence of items.
            
            evaluate: bool
                If set to True, items sequence is evaluated into list upon
                class init and for each method call as well.
        """
        
        self._source = list(source) if evaluate else source
        self._evaluate = evaluate
    
    
    def __iter__(self):
        """Gets items iterator."""
        
        return iter(self._source)
    
    
    def aggregate(self, accumulator, seed=None):
        """
        Applies accumulator function over current sequence.
        
        Args:
            accumulator: callable
                Accumulator function expecting two arguments (res, next).
            
            seed: any
                Initial aggregation value. If set to None, the first item is
                used.
        
        Returns:
            any
        """
        
        return iters.aggregate(self, accumulator, seed)
    
    
    def all(self, condition):
        """
        Determines whether all items of current sequence satisfy given
        condition.
        
        Args:
            condition: callable
                Condition to test.
        
        Returns:
            bool
        """
        
        return all(condition(d) for d in self)
    
    
    def any(self, condition=None):
        """
        Determines whether current sequence contains any item or whether any
        item of current sequence satisfies given condition.
        
        Args:
            condition: callable or None
                Condition to test.
        
        Returns:
            bool
        """
        
        if condition is None:
            return any(self)
        
        return any(condition(d) for d in self)
    
    
    def argmax(self, key=None):
        """
        Returns index of the maximum item in a sequence by using default
        comparer or specified item's key.
        
        Args:
            key: callable or None
                Item's key selector.
        
        Returns:
            int
        """
        
        return iters.argmax(self, key)
    
    
    def argmin(self, key=None):
        """
        Returns index of the minimum item in a sequence by using default
        comparer or specified item's key.
        
        Args:
            key: callable or None
                Item's key selector.
        
        Returns:
            int
        """
        
        return iters.argmin(self, key)
    
    
    def argsort(self, key=None, reverse=False):
        """
        Returns items indices that would sort current sequence by using
        default comparer or specified item's key.
        
        Args:
            key: callable or None
                Item's key selector.
            
            reverse: bool
                If set to True, sorting is reversed.
        
        Returns:
            Linque
        """
        
        def source():
            for item in iters.argsort(self, key, reverse=reverse):
                yield item
        
        result = (d for d in source())
        
        return Linque(result, self._evaluate)
    
    
    def choice(self, weights=None, seed=None):
        """
        Returns random item from current sequence.
        
        Args:
            weights: (float,) or None
                Relative probabilities for individual items to be selected.
            
            seed: int or None
                Seed to initialize random generator.
        
        Returns:
            any
        """
        
        if seed is not None:
            random.seed(seed)
        
        if weights is None:
            return random.choice(list(self))
        
        return random.choices(list(self), weights=weights, k=1)[0]
    
    
    def choices(self, count, weights=None):
        """
        Produces new sequence by randomly choosing number of items from current
        sequence. Each item can be selected multiple times.
        
        Args:
            count: int
                Number of choices to make.
            
            weights: (float,) or None
                Relative probabilities for individual items to be selected.
        
        Returns:
            Linque
        """
        
        def source():
            for item in random.choices(list(self), weights=weights, k=count):
                yield item
        
        result = (d for d in source())
        
        return Linque(result, self._evaluate)
    
    
    def chunk(self, size):
        """
        Splits current sequence into chunks of specified size.
        
        Args:
            
            size: int
                Maximum size of each chunk.
            
        Returns:
            Linque
        """
        
        chunks = iters.chunk(self, size)
        result = (Linque(c, self._evaluate) for c in chunks)
        
        return Linque(result, self._evaluate)
    
    
    def concat(self, items):
        """
        Produces new sequence by appending given items at the end of current
        sequence.
        
        Args:
            items: (any,)
                Items to append.
        
        Returns:
            Linque
        """
        
        result = iters.concat(self, items)
        
        return Linque(result, self._evaluate)
    
    
    def contains(self, value, key=None):
        """
        Determines whether current sequence contains specified item or value by using
        default comparer or specified item's key.
        
        Args:
            value: any
                Item or value to check.
            
            key: callable or None
                Item's key selector.
        
        Returns:
            bool
        """
        
        if key is not None:
            return value in (key(d) for d in self)
        
        return value in self
    
    
    def count(self, condition=None):
        """
        Returns number of items in current sequence satisfying given condition.
        
        Args:
            condition: callable or None
                Condition to test.
        
        Returns:
            int
        """
        
        return iters.count(self, condition)
    
    
    def distinct(self, key=None):
        """
        Produces new sequence by selecting distinct items from current sequence
        using default comparer or specified item's key. First occurrence of each
        item is used.
        
        Args:
            key: callable or None
                Item's key selector.
        
        Returns:
            Linque
        """
        
        result = iters.distinct(self, key)
        
        return Linque(result, self._evaluate)
    
    
    def each(self, action):
        """
        Applies specified function to every item in current sequence. Any
        return value of given function is ignored. Since this call fully
        evaluates current sequence, depending on the source, the items may no
        longer be available. This may or may not be desired behavior. Consider
        calling '.evaluate()' before calling this method.
        
        Args:
            action: callable
                Function to be applied.
        
        Returns:
            Linque
        """
        
        for item in self:
            action(item)
        
        return self
    
    
    def enumerate(self):
        """
        Produces new sequence by enumerating items of current sequence into
        (index, item) pairs.
        
        Returns:
            Linque
        """
        
        result = enumerate(self)
        
        return Linque(result, self._evaluate)
    
    
    def evaluate(self):
        """
        Evaluates all the iterators in current sequence and stores items as
        internal list.
        
        Returns:
            Linque
        """
        
        if not isinstance(self._source, (list, tuple)):
            self._source = list(self)
        
        return self
    
    
    def exclude(self, items, key=None):
        """
        Produces new sequence by excluding specified items from current sequence
        using default comparer or specified item's key.
        
        Args:
            items: (any,)
                Items to exclude.
            
            key: callable or None
                Item's key selector.
        
        Returns:
            Linque
        """
        
        result = iters.exclude(self, items, key)
        
        return Linque(result, self._evaluate)
    
    
    def first(self, condition=None, default=iters.UNDEFINED):
        """
        Returns the first item in current sequence that satisfies specified
        condition or raises error if no item found and no default value is
        provided.
        
        Args:
            condition: callable or None
                Condition to test.
            
            default: any
                Default value.
        
        Returns:
            any
        """
        
        return iters.first(self, condition, default)
    
    
    def flatten(self, selector=None):
        """
        Produces new sequence by selecting and flattening items data using
        specified selector.
        
        Args:
            selector: callable
                Item's data selector.
        
        Returns:
            Linque
        """
        
        if selector is None:
            result = (d2 for d1 in self for d2 in d1)
        else:
            result = (d2 for d1 in self for d2 in selector(d1))
        
        return Linque(result, self._evaluate)
    
    
    def group(self, key=None):
        """
        Produces new sequence by grouping items of current sequence according to
        default comparer or specified item's key and creates result values as
        (key, group) pairs.
        
        Args:
            key: callable or None
                Item's key selector.
        
        Returns:
            Linque
        """
        
        def source():
            for item in iters.group(self, key):
                yield item
        
        result = ((k, Linque(g, self._evaluate)) for k, g in source())
        
        return Linque(result, self._evaluate)
    
    
    def intersect(self, items, key=None):
        """
        Produces new sequence of shared unique items from current sequence and
        given items by using default comparer or specified item's key.
        
        Args:
            items: (any,)
                Items to intersect.
            
            key: callable or None
                Item's key selector.
        
        Returns:
            Linque
        """
        
        result = iters.intersect(self, items, key)
        
        return Linque(result, self._evaluate)
    
    
    def last(self, condition=None, default=iters.UNDEFINED):
        """
        Returns the last item in current sequence that satisfies specified
        condition or raises error if no item found and no default value is
        provided.
        
        Args:
            condition: callable or None
                Condition to test.
            
            default: any
                Default value.
        
        Returns:
            any
        """
        
        return iters.last(self, condition, default)
    
    
    def maximum(self, selector=None):
        """
        Returns maximum value in current sequence by specified items data
        selector.
        
        Args:
            selector: callable
                Item's data selector.
        
        Returns:
            any
        """
        
        if selector is None:
            return max(self)
        
        return max(selector(d) for d in self)
    
    
    def max(self, key=None):
        """
        Returns item having maximum value in current sequence by using default
        comparer or specified item's key.
        
        Args:
            key: callable or None
                Item's key selector.
        
        Returns:
            any
        """
        
        return max(self, key=key) if key is not None else max(self)
    
    
    def mean(self, selector=None):
        """
        Returns average value of current sequence by specified items data
        selector.
        
        Args:
            selector: callable
                Item's data selector.
        
        Returns:
            any
        """
        
        if selector is None:
            return statistics.mean(d for d in self)
        
        return statistics.mean(selector(d) for d in self)
    
    
    def median(self, selector=None):
        """
        Returns median value of current sequence by specified items data
        selector.
        
        Args:
            selector: callable
                Item's data selector.
        
        Returns:
            any
        """
        
        if selector is None:
            return statistics.median(d for d in self)
        
        return statistics.median(selector(d) for d in self)
    
    
    def minimum(self, selector=None):
        """
        Returns minimum value in current sequence by specified items data
        selector.
        
        Args:
            selector: callable
                Item's data selector.
        
        Returns:
            any
        """
        
        if selector is None:
            return min(self)
        
        return min(selector(d) for d in self)
    
    
    def min(self, key=None):
        """
        Returns item having minimum value in current sequence by using default
        comparer or specified item's key.
        
        Args:
            key: callable or None
                Item's key selector.
        
        Returns:
            any
        """
        
        return min(self, key=key) if key is not None else min(self)
    
    
    def rank(self, key=None, method='average', reverse=False):
        """
        Provides 1-based rank for each item of current sequence by using default
        comparer or specified item's key. The ties are resolved according to
        selected method.
        
        Args:
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
            Linque
        """
        
        def source():
            for item in iters.rank(self, key, method=method, reverse=reverse):
                yield item
        
        result = (d for d in source())
        
        return Linque(result, self._evaluate)
    
    
    def reverse(self):
        """
        Produces new sequence by inverting order of items in current sequence.
        
        Returns:
            Linque
        """
        
        def source():
            for item in reversed(list(self)):
                yield item
        
        result = (d for d in source())
        
        return Linque(result, self._evaluate)
    
    
    def sample(self, count):
        """
        Produces new sequence by randomly sampling number of items from current
        sequence. Each item can be selected only once.
        
        Args:
            count: int
                Number of items to sample.
        
        Returns:
            Linque
        """
        
        def source():
            for item in random.sample(list(self), count):
                yield item
        
        result = (d for d in source())
        
        return Linque(result, self._evaluate)
    
    
    def select(self, selector):
        """
        Produces new sequence by selecting items data by specified selector.
        
        Args:
            selector: callable
                Item's data selector.
        
        Returns:
            Linque
        """
        
        result = (selector(d) for d in self)
        
        return Linque(result, self._evaluate)
    
    
    def select_many(self, selector=None):
        """
        Produces new sequence by selecting and flattening items data using
        specified selector.
        
        Args:
            selector: callable
                Item's data selector.
        
        Returns:
            Linque
        """
        
        if selector is None:
            result = (d2 for d1 in self for d2 in d1)
        else:
            result = (d2 for d1 in self for d2 in selector(d1))
        
        return Linque(result, self._evaluate)
    
    
    def shuffle(self):
        """
        Produces new sequence by randomly shuffling items from current sequence.
        
        Returns:
            Linque
        """
        
        def source():
            items = list(self)
            random.shuffle(items)
            for item in items:
                yield item
        
        result = (d for d in source())
        
        return Linque(result, self._evaluate)
    
    
    def single(self, condition=None, default=iters.UNDEFINED):
        """
        Returns the single item in current sequence that satisfies specified
        condition or raises error if more items found. If no item is found,
        returns default value if provided or raises error.
        
        Args:
            condition: callable
                Condition to test.
            
            default: any
                Default value.
        
        Returns:
            any
        """
        
        return iters.single(self, condition, default)
    
    
    def skip(self, count):
        """
        Produces new sequence by bypassing specified number of items in current
        sequence and returns the remaining items.
        
        Args:
            count: int
                Number of items to skip.
        
        Returns:
            Linque
        """
        
        result = iters.skip(self, count)
        
        return Linque(result, self._evaluate)
    
    
    def skip_while(self, condition):
        """
        Produces new sequence by bypassing contiguous items from the start of
        current sequence until specified condition fails the first time.
        
        Args:
            condition: callable
                Condition to test.
        
        Returns:
            Linque
        """
        
        result = iters.skip_while(self, condition)
        
        return Linque(result, self._evaluate)
    
    
    def sort(self, key=None, reverse=False):
        """
        Produces new sequence by sorting elements of current sequence by using
        default comparer or specified item's key. If the key provides multiple
        columns, the sorting direction can be specified for each individual
        column.
        
        Args:
            key: callable or None
                Item's key selector.
            
            reverse: bool
                If set to True, sorting is reversed. This flag can be specified
                independently foreach key column.
        
        Returns:
            Linque
        """
        
        def source():
            for item in iters.multisort(self, key=key, reverse=reverse):
                yield item
        
        result = (d for d in source())
        
        return Linque(result, self._evaluate)
    
    
    def sum(self, selector=None):
        """
        Returns summed value in current sequence by specified items data
        selector.
        
        Args:
            selector: callable
                Item's data selector.
        
        Returns:
            any
        """
        
        if selector is None:
            return sum(self)
        
        return sum(selector(d) for d in self)
    
    
    def take(self, count):
        """
        Produces new sequence by selecting specified number of contiguous items
        from the start of current sequence.
        
        Args:
            count: int
                Number of items to take.
        
        Returns:
            Linque
        """
        
        result = iters.take(self, count)
        
        return Linque(result, self._evaluate)
    
    
    def take_while(self, condition):
        """
        Produces new sequence by selecting items from current sequence as long
        as specified condition is true.
        
        Args:
            condition: callable
                Condition to test.
        
        Returns:
            Linque
        """
        
        result = iters.take_while(self, condition)
        
        return Linque(result, self._evaluate)
    
    
    def to_dict(self, key, value=lambda d: d):
        """
        Evaluates items into dictionary.
        
        Args:
            key: callable
                Item's key selector.
            
            value: callable
                Item's value selector.
        
        Returns:
            dict
        """
        
        result = {}
        
        for item in self:
            k = key(item)
            if k in result:
                raise KeyError("Key is not unique.")
            result[k] = value(item)
        
        return result
    
    
    def to_list(self):
        """
        Evaluate items into list.
        
        Returns:
            list
        """
        
        return list(self)
    
    
    def to_set(self):
        """
        Evaluate items into set.
        
        Returns:
            set
        """
        
        return set(self)
    
    
    def to_tuple(self):
        """
        Evaluate items into tuple.
        
        Returns:
            tuple
        """
        
        return tuple(self)
    
    
    def union(self, items, key=None):
        """
        Produces new sequence of unique items from current sequence and given
        items by using default comparer or specified item's key.
        
        Args:
            items: (any,)
                Items to union.
            
            key: callable or None
                Item's key selector.
        
        Returns:
            Linque
        """
        
        result = iters.union(self, items, key)
        
        return Linque(result, self._evaluate)
    
    
    def where(self, condition):
        """
        Produces new sequence by selecting items by specified predicate.
        
        Args:
            condition: callable
                Condition to test.
        
        Returns:
            Linque
        """
        
        result = (d for d in self if condition(d))
        
        return Linque(result, self._evaluate)
    
    
    def zip(self, *sequences):
        """
        Produces new sequence by merging given sequences with current sequence
        as long as there are items available in all sequences.
        
        Args:
            sequences: ((any,),)
                Sequences to zip.
        
        Returns:
            Linque
        """
        
        result = zip(self, *sequences)
        
        return Linque(result, self._evaluate)
