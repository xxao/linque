#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import statistics
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
    
    def __init__(self, items, evaluate=False):
        """
        Initializes a new instance of Linque.
        
        Args:
            items: iterable
                Sequence of items.
            
            evaluate: bool
                If set to True, items sequence is evaluated into tuple upon
                class init and for each method call as well.
        """
        
        self._items = list(items) if evaluate else items
        self._evaluate = evaluate
    
    
    def __iter__(self):
        """Gets items iterator."""
        
        return iter(self._items)
    
    
    def aggregate(self, accumulator, seed=None):
        """
        Applies accumulator function over current sequence. This call fully
        evaluates current sequence.
        
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
        condition. This call does not evaluate current sequence.
        
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
        item of current sequence satisfies given condition. This call does not
        evaluate current sequence.
        
        Args:
            condition: callable or None
                Condition to test.
        
        Returns:
            bool
        """
        
        if condition is None:
            return any(self)
        
        return any(condition(d) for d in self)
    
    
    def argsort(self, reverse=False):
        """
        Returns items indices that would sort current sequence by using
        default comparer. This call fully evaluates current sequence.
        
        Args:
            reverse: bool
                If set to True, sorting is reversed.
        
        Returns:
            Linque
        """
        
        result = iters.argsort(self, reverse=reverse)
        
        return Linque(result, self._evaluate)
    
    
    def argsort_by(self, key, reverse=False):
        """
        Returns items indices that would sort current sequence by using
        specified item's key. This call fully evaluates current sequence.
        
        Args:
            key: callable
                Item's key selector.
            
            reverse: bool
                If set to True, sorting is reversed.
        
        Returns:
            Linque
        """
        
        result = iters.argsort_by(self, key, reverse=reverse)
        
        return Linque(result, self._evaluate)
    
    
    def chunk(self, size):
        """
        Splits current sequence into chunks of specified size. This call does
        not evaluate current sequence.
        
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
        sequence. This call does not evaluate current sequence.
        
        Args:
            items: (any,)
                Items to append.
        
        Returns:
            Linque
        """
        
        result = iters.concat(self, items)
        
        return Linque(result, self._evaluate)
    
    
    def contains(self, item):
        """
        Determines whether current sequence contains specified item by using
        default comparer. This call partially evaluates current sequence.
        
        Args:
            item: any
                Item to check.
        
        Returns:
            bool
        """
        
        return item in self
    
    
    def contains_by(self, value, key):
        """
        Determines whether current sequence contains item with given value by
        using specified item's key. This call partially evaluates current sequence.
        
        Args:
            value: any
                Value to check.
            
            key: callable
                Item's key selector.
        
        Returns:
            bool
        """
        
        return value in (key(d) for d in self)
    
    
    def count(self, condition=None):
        """
        Returns number of items in current sequence satisfying given condition.
        This call fully evaluates current sequence.
        
        Args:
            condition: callable or None
                Condition to test.
        
        Returns:
            int
        """
        
        return iters.count(self, condition)
    
    
    def distinct(self):
        """
        Produces new sequence by selecting distinct items from current sequence
        using default comparer. First occurrence of each item is used. This call
        does not evaluate current sequence.
        
        Returns:
            Linque
        """
        
        result = iters.distinct(self)
        
        return Linque(result, self._evaluate)
    
    
    def distinct_by(self, key):
        """
        Produces new sequence by selecting distinct items from current sequence
        using specified item's key. First occurrence of each item is used. This
        call does not evaluate current sequence.
        
        Args:
            key: callable
                Item's key selector.
        
        Returns:
            Linque
        """
        
        result = iters.distinct_by(self, key)
        
        return Linque(result, self._evaluate)
    
    
    def each(self, action):
        """
        Applies specified function to every item in current sequence. Note that
        this does not replace the items, so it works only with objects. Any
        return value of given function is ignored. This call fully evaluates
        current sequence.
        
        Args:
            action: callable
                Function to be applied.
        
        Returns:
            Linque
        """
        
        self.evaluate()
        
        for item in self:
            action(item)
        
        return self
    
    
    def enumerate(self):
        """
        Produces new sequence by enumerating items of current sequence into
        (index, item) pairs. This call does not evaluate current sequence.
        
        Returns:
            Linque
        """
        
        result = enumerate(self)
        
        return Linque(result, self._evaluate)
    
    
    def evaluate(self):
        """
        Evaluates all the iterators in current sequence and stores items as
        internal list. This method is essential if current Linque instance
        should be reused.
        
        Returns:
            Linque
        """
        
        if not isinstance(self._items, (list, tuple)):
            self._items = list(self)
        
        return self
    
    
    def exclude(self, items):
        """
        Produces new sequence by excluding specified items from current sequence
        using default comparer. This call does not evaluate current sequence.
        
        Args:
            items: (any,)
                Items to exclude.
        
        Returns:
            Linque
        """
        
        result = iters.exclude(self, items)
        
        return Linque(result, self._evaluate)
    
    
    def exclude_by(self, items, key):
        """
        Produces new sequence by excluding specified items from current sequence
        using selected item's key. This call does not evaluate current sequence.
        
        Args:
            items: (any,)
                Items to exclude.
            
            key: callable
                Item's key selector.
        
        Returns:
            Linque
        """
        
        result = iters.exclude_by(self, items, key)
        
        return Linque(result, self._evaluate)
    
    
    def first(self, condition=None):
        """
        Returns the first item in current sequence that satisfies specified
        condition or raises error if no item found. This call partially
        evaluates current sequence.
        
        Args:
            condition: callable or None
                Condition to test.
        
        Returns:
            any
        """
        
        return iters.first(self, condition)
    
    
    def first_or_default(self, condition=None, default=None):
        """
        Returns the first item in current sequence that satisfies specified
        condition or specified default value if no item found. This call
        partially evaluates current sequence.
        
        Args:
            condition: callable or None
                Condition to test.
            
            default: any
                Default value.
        
        Returns:
            any
        """
        
        return iters.first_or_default(self, condition, default)
    
    
    def flatten(self, selector=None):
        """
        Produces new sequence by selecting and flattening items data using
        specified selector. This call does not evaluate current sequence.
        
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
    
    
    def group(self):
        """
        Produces new sequence by grouping items of current sequence according to
        default comparer and creates result values as (key, group) pairs.
        This call fully evaluates current sequence.
        
        Returns:
            Linque
        """
        
        groups = iters.group(self)
        result = [(k, Linque(g, self._evaluate)) for k, g in groups]
        
        return Linque(result, self._evaluate)
    
    
    def group_by(self, key):
        """
        Produces new sequence by grouping items of current sequence according to
        specified key selector and creates result values as (key, group) pairs.
        This call fully evaluates current sequence.
        
        Args:
            key: callable
                Item's key selector.
        
        Returns:
            Linque
        """
        
        groups = iters.group_by(self, key)
        result = [(k, Linque(g, self._evaluate)) for k, g in groups]
        
        return Linque(result, self._evaluate)
    
    
    def intersect(self, items):
        """
        Produces new sequence of shared unique items from current sequence and
        given items by using default comparer. This call does not evaluate
        current sequence.
        
        Args:
            items: (any,)
                Items to intersect.
        
        Returns:
            Linque
        """
        
        result = iters.intersect(self, items)
        
        return Linque(result, self._evaluate)
    
    
    def intersect_by(self, items, key):
        """
        Produces new sequence of shared unique items from current sequence and
        given items by using selected item's key. This call does not evaluate
        current sequence.
        
        Args:
            items: (any,)
                Items to intersect.
            
            key: callable
                Item's key selector.
        
        Returns:
            Linque
        """
        
        result = iters.intersect_by(self, items, key)
        
        return Linque(result, self._evaluate)
    
    
    def last(self, condition=None):
        """
        Returns the last item in current sequence that satisfies specified
        condition or raises error if no item found. This call fully evaluates
        current sequence.
        
        Args:
            condition: callable or None
                Condition to test.
        
        Returns:
            any
        """
        
        return iters.last(self, condition)
    
    
    def last_or_default(self, condition=None, default=None):
        """
        Returns the last item in current sequence that satisfies specified
        condition or specified default value if no item found. This call
        fully evaluates current sequence.
        
        Args:
            condition: callable or None
                Condition to test.
            
            default: any
                Default value.
        
        Returns:
            any
        """
        
        return iters.last_or_default(self, condition, default)
    
    
    def max(self, selector=None):
        """
        Returns maximum value in current sequence by specified items data
        selector. This call fully evaluates current sequence.
        
        Args:
            selector: callable
                Item's data selector.
        
        Returns:
            any
        """
        
        if selector is None:
            return max(self)
        
        return max(selector(d) for d in self)
    
    
    def max_by(self, key):
        """
        Returns item having maximum value in current sequence by using default
        comparer or specified item's key. This call fully evaluates current
        sequence.
        
        Args:
            key: callable
                Item's key selector.
        
        Returns:
            any
        """
        
        return max(self, key=key)
    
    
    def mean(self, selector=None):
        """
        Returns average value of current sequence by specified items data
        selector. This call fully evaluates current sequence.
        
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
        selector. This call fully evaluates current sequence.
        
        Args:
            selector: callable
                Item's data selector.
        
        Returns:
            any
        """
        
        if selector is None:
            return statistics.median(d for d in self)
        
        return statistics.median(selector(d) for d in self)
    
    
    def min(self, selector=None):
        """
        Returns minimum value in current sequence by specified items data
        selector. This call fully evaluates current sequence.
        
        Args:
            selector: callable
                Item's data selector.
        
        Returns:
            any
        """
        
        if selector is None:
            return min(self)
        
        return min(selector(d) for d in self)
    
    
    def min_by(self, key):
        """
        Returns item having minimum value in current sequence by using default
        comparer or specified item's key. This call fully evaluates current
        sequence.
        
        Args:
            key: callable
                Item's key selector.
        
        Returns:
            any
        """
        
        return min(self, key=key)
    
    
    def rank(self, method='average', reverse=False):
        """
        Provides 1-based rank for each item of current sequence by using default
        comparer. The ties are resolved according to selected method. This call
        fully evaluates current sequence.
        
        Args:
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
        
        result = iters.rank(self, method=method, reverse=reverse)
        
        return Linque(result, self._evaluate)
    
    
    def rank_by(self, key, method='average', reverse=False):
        """
        Provides 1-based rank for each item of current sequence by using
        selected item's key. The ties are resolved according to selected
        method. This call fully evaluates current sequence.
        
        Args:
            key: callable
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
        
        result = iters.rank_by(self, key, method=method, reverse=reverse)
        
        return Linque(result, self._evaluate)
    
    
    def reverse(self):
        """
        Produces new sequence by inverting order of items in current sequence.
        This call fully evaluates current sequence.
        
        Returns:
            Linque
        """
        
        result = reversed([d for d in self])
        
        return Linque(result, self._evaluate)
    
    
    def select(self, selector):
        """
        Produces new sequence by selecting items data by specified selector.
        This call does not evaluate current sequence.
        
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
        specified selector. This call does not evaluate current sequence.
        
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
    
    
    def single(self, condition=None):
        """
        Returns the single item in current sequence that satisfies specified
        condition or raises error if none or more items found. This call fully
        evaluates current sequence.
        
        Args:
            condition: callable
                Condition to test.
        
        Returns:
            any
        """
        
        return iters.single(self, condition)
    
    
    def single_or_default(self, condition=None, default=None):
        """
        Returns the single item in current sequence that satisfies specified
        condition or specified default value if no item found. Raises error if
        more items found. This call fully evaluates current sequence.
        
        Args:
            condition: callable
                Condition to test.
            
            default: any
                Default value.
        
        Returns:
            any
        """
        
        return iters.single_or_default(self, condition, default)
    
    
    def skip(self, count):
        """
        Produces new sequence by bypassing specified number of items in current
        sequence and returns the remaining items. This call partially evaluates
        current sequence.
        
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
    
    
    def sort(self, reverse=False):
        """
        Produces new sequence by sorting elements of current sequence by using
        default comparer. This call fully evaluates current sequence.
        
        Args:
            reverse: bool
                If set to True, sorting is reversed.
        
        Returns:
            Linque
        """
        
        result = sorted(self, reverse=reverse)
        
        return Linque(result, self._evaluate)
    
    
    def sort_by(self, key, reverse=False):
        """
        Produces new sequence by sorting elements of current sequence by using
        selected item's key. This call fully evaluates current sequence.
        
        Args:
            key: callable
                Item's key selector.
            
            reverse: bool
                If set to True, sorting is reversed.
        
        Returns:
            Linque
        """
        
        result = sorted(self, key=key, reverse=reverse)
        
        return Linque(result, self._evaluate)
    
    
    def sum(self, selector=None):
        """
        Returns summed value in current sequence by specified items data
        selector. This call fully evaluates current sequence.
        
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
        from the start of current sequence. This call partially evaluates
        current sequence.
        
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
        as specified condition is true. This call partially evaluates current
        sequence.
        
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
        Evaluates items into dictionary. This call fully evaluates current
        sequence.
        
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
        Evaluate items into list. This call fully evaluates current sequence.
        
        Returns:
            list
        """
        
        return list(self)
    
    
    def to_set(self):
        """
        Evaluate items into set. This call fully evaluates current sequence.
        
        Returns:
            set
        """
        
        return set(self)
    
    
    def to_tuple(self):
        """
        Evaluate items into tuple. This call fully evaluates current sequence.
        
        Returns:
            tuple
        """
        
        return tuple(self)
    
    
    def union(self, items):
        """
        Produces new sequence of unique items from current sequence and given
        items by using default comparer. This call does not evaluate current
        sequence.
        
        Args:
            items: (any,)
                Items to union.
        
        Returns:
            Linque
        """
        
        result = iters.union(self, items)
        
        return Linque(result, self._evaluate)
    
    
    def union_by(self, items, key):
        """
        Produces new sequence of unique items from current sequence and given
        items by using selected item's key. This call does not evaluate current
        sequence.
        
        Args:
            items: (any,)
                Items to union.
            
            key: callable
                Item's key selector.
        
        Returns:
            Linque
        """
        
        result = iters.union_by(self, items, key)
        
        return Linque(result, self._evaluate)
    
    
    def where(self, condition):
        """
        Produces new sequence by selecting items by specified predicate. This
        call does not evaluate current sequence.
        
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
        as long as there are items available in all sequences. This call does
        not evaluate current sequence.
        
        Args:
            sequences: ((any,),)
                Sequences to zip.
        
        Returns:
            Linque
        """
        
        result = zip(self, *sequences)
        
        return Linque(result, self._evaluate)
