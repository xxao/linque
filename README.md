# LinQue - Linear Query

The *LinQue* library can be seen as a Python equivalent of popular .NET LINQ (Language Integrated Query). It allows
chaining multiple queries on a sequence of items without evaluating the sequence until necessary.

```python
from linque import Linque

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

result = Linque(words) \
    .select(lambda d: d.upper()) \
    .distinct() \
    .sort() \
    .group_by(lambda d: len(d)) \
    .sort_by(lambda d: d[0]) \
    .flatten(lambda d: d[1]) \
    .to_list() \

print(result)

# ['DOG', 'FOX', 'THE', 'LAZY', 'OVER', 'BROWN', 'JUMPS', 'QUICK']
```

Similar to .NET, *LinQue* internally uses iterators only and does not evaluate the source sequence until necessary.
Depending on whether the source sequence itself is fully evaluated (i.e. list or tuple) or not (i.e. iterator), a Linque
instance can be safely reused or used just in a single chained query. By default, type of the source sequence is not
changed and the instance behaves accordingly. This behavior can be changed by initializing it with the 'evaluate' flag
set to True, to keep results of each step as internal list. This is automatically applied to all derived instances as
well. To evaluate just current state, the 'evaluate' method should be called.

```python
from linque import Linque

# using iterator as source
linq = Linque(d for d in range(10))
s = linq.sum()  # this call evaluates the sequence
print(linq.to_list())  # there are no 'next' items available anymore

# []

# using fully evaluated source
linq = Linque(list(range(10)))
s = linq.sum()
print(linq.to_list())

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# force source evaluation
linq = Linque((d for d in range(10)), True)
s = linq.sum()
print(linq.to_list())

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# evaluate current instance
linq = Linque(d for d in range(10))
linq.evaluate()
s = linq.sum()
print(linq.to_list())

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Installation

The *LinQue* library is fully implemented in Python. No additional compiler is necessary. After downloading the source
code just run the following command from the *linque* folder:

```$ python setup.py install```

or simply by using pip

```$ pip install linque```


## Available Methods

### .aggregate(accumulator, seed)
Applies accumulator function over current sequence. This call fully evaluates current sequence. This functionality is
also available as a *linque.aggregate(sequence, func, seed)* utility function.

```python
data = (97, 103, 103, 114, 101, 103, 97, 116, 101)
result = Linque(data).aggregate(lambda r, d: r+chr(d), "")
print(result)

# 'aggregate'
```

### .all(condition)
Determines whether all items of current sequence satisfy given condition. This call does not evaluate current sequence.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result = Linque(data).all(lambda d: d > -5)
print(result)

# True
```

### .any(condition)
Determines whether current sequence contains any item or whether any item of current sequence satisfies given condition.
This call does not evaluate current sequence.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result = Linque(data).any(lambda d: d > 5)
print(result)

# True
```

### .chunk(item)
Determines whether current sequence contains specified item by using default comparer. This call does not evaluate
current sequence. This functionality is also available as a *linque.chunk(\*sequences)* utility function.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result = Linque(data).chunk(3).select(lambda d: d.to_tuple()).to_list()
print(result)

# [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9,)]
```

### .concat(items)
Produces new sequence by appending given items at the end of current sequence. This call does not evaluate current
sequence. This functionality is also available as a *linque.concat(\*sequences)* utility function.

```python
data1 = (0, 1, 2, 3, 4)
data2 = (5, 6, 7, 8, 9)
result = Linque(data1).concat(data2).to_list()
print(result)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### .contains(item)
Determines whether current sequence contains specified item by using default comparer. This call partially evaluates
current sequence.

```python
data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
result = Linque(data).contains((1, 10))
print(result)

# True
```

### .count(condition)
Returns number of items in current sequence satisfying given condition. This call fully evaluates current sequence.
This functionality is also available as a *linque.count(sequence, condition)* utility function.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result = Linque(data).count(lambda d: d > 4)
print(result)

# 5
```

### .distinct()
Produces new sequence by selecting distinct items from current sequence using default comparer. First occurrence of each
item is used. This call does not evaluate current sequence. This functionality is also available as a
*linque.distinct(sequence, items)* utility function.

```python
data = ((0, 1), (0, 1), (0, 2), (1, 1), (1, 2))
result = Linque(data).distinct().to_list()
print(result)

# [(0, 1), (0, 2), (1, 1), (1, 2)]
```

### .distinct_by(key)
Produces new sequence by selecting distinct items from current sequence using specified item's key. First occurrence of
each item is used. This call does not evaluate current sequence. This functionality is also available as a
*linque.distinct_by(sequence, items, key)* utility function.

```python
data = ((0, 1), (0, 1), (0, 2), (1, 1), (1, 2))
result = Linque(data).distinct_by(lambda d: d[1]).to_list()
print(result)

# [(0, 1), (0, 2)]
```

### .each(action)
Applies specified function to every item in current sequence. Note that this does not replace the items, so it works
only with objects. Any return value of given function is ignored. This call fully evaluates current sequence.

```python
def action(d):
    d[1] = str(d[0])


data = ([0, None], [1, None], [2, None], [3, None], [4, None])
result = Linque(data).each(action).to_list()
print(result)

# [[0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4']]
```

### .enumerate()
Produces new sequence by enumerating items of current sequence into (index, item) pairs. This call does not evaluate
current sequence.

```python
data = (5, 6, 7, 8, 9)
result = Linque(data).enumerate().to_list()
print(result)

# [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
```

### .evaluate()
Evaluates all the iterators in current sequence and stores items as internal list. This method is essential if current
Linque instance should be reused.

```python
linq = Linque(d for d in range(10))
linq.sum()
print(linq.to_list())

# []

linq = Linque(d for d in range(10))
linq.evaluate()
linq.sum()
print(linq.to_list())

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### .exclude(items)
Produces new sequence by excluding specified items from current sequence using default comparer. This call does not
evaluate current sequence. This functionality is also available as a
*linque.exclude(sequence, items)* utility function.

```python
data1 = ((0, 1), (0, 1), (0, 2), (1, 2), (0, 3), (0, 4))
data2 = ((0, 1), (1, 2), (1, 2), (1, 3))
result = Linque(data1).exclude(data2).to_list()
print(result)

# [(0, 2), (0, 3), (0, 4)]
```

### .exclude_by(items, key)
Produces new sequence by excluding specified items from current sequence using selected item's key. This call does not
evaluate current sequence. This functionality is also available as a
*linque.exclude_by(sequence, items, key)* utility function.

```python
data1 = ((0, 1), (0, 1), (0, 2), (1, 2), (0, 3), (0, 4))
data2 = ((0, 1), (1, 2), (1, 2), (1, 3))
result = Linque(data1).exclude_by(data2, lambda d: d[1]).to_list()
print(result)

# [(0, 4)]
```

### .first(condition)
Returns the first item in current sequence that satisfies specified condition or raises error if no item found. This
call partially evaluates current sequence. This functionality is also available as a
*linque.first(sequence, condition)* utility function.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result = Linque(data).first(lambda d: d > 4)
print(result)

# 5
```

### .first_or_default(condition, default)
Returns the first item in current sequence that satisfies specified condition or specified default value if no item
found. This call partially evaluates current sequence. This functionality is also available as a
*linque.first_or_default(sequence, condition, default)* utility function.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result = Linque(data).first_or_default(lambda d: d > 10, -1)
print(result)

# -1
```

### .flatten(selector)
Produces new sequence by selecting and flattening items data using specified selector. This call does not evaluate
current sequence.

```python
data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
result = Linque(data).flatten().to_list()
print(result)

# [0, 0, 1, 10, 2, 20, 3, 30, 4, 40]
```

### .group()
Produces new sequence by grouping items of current sequence according to default comparer and creates result
values as (key, group) pairs. This call fully evaluates current sequence. This functionality is also available as a
*linque.group(sequence)* utility function.

```python
data = ((0, 1), (0, 1), (0, 2), (1, 1))
result = Linque(data).group().to_dict(lambda d: d[0], lambda d: d[1].to_list())
print(result)

# {
#     (0, 1): [(0, 1), (0, 1)], 
#     (0, 2): [(0, 2)],
#     (1, 1): [(1, 1)]
# }
```

### .group_by(key)
Produces new sequence by grouping items of current sequence according to specified key selector and creates result
values as (key, group) pairs. This call fully evaluates current sequence. This functionality is also available as a
*linque.group_by(sequence, key)* utility function.

```python
data = ((0, 1), (0, 1), (0, 2))
result = Linque(data).group_by(lambda d: d[1]).to_dict(lambda d: d[0], lambda d: d[1].to_list())
print(result)

# {
#     1: [(0, 1), (0, 1), (1, 1)], 
#     2: [(0, 2)],
# }
```

### .intersect(items)
Produces new sequence of shared unique items from current sequence and given items by using default comparer. This call
does not evaluate current sequence. This functionality is also available as a
*linque.intersect(sequence, items)* utility function.

```python
data1 = ((0, 1), (0, 1), (0, 2), (1, 2))
data2 = ((0, 1), (1, 2), (1, 2), (0, 3))
result = Linque(data1).intersect(data2).to_list()
print(result)

# [(0, 1), (1, 2)]
```

### .intersect_by(items, key)
Produces new sequence of shared unique items from current sequence and given items by using selected item's key. This
call does not evaluate current sequence. This functionality is also available as a
*linque.intersect_by(sequence, items, key)* utility function.

```python
data1 = ((0, 1), (0, 1), (0, 2), (1, 2))
data2 = ((0, 1), (1, 2), (1, 2), (0, 3))
result = Linque(data1).intersect_by(data2, lambda d: d[1]).to_list()
print(result)

# [(0, 1), (0, 2)]
```

### .last(condition)
Returns the last item in current sequence that satisfies specified condition or raises error if no item found. This call
partially evaluates current sequence. This functionality is also available as a
*linque.last(sequence, condition)* utility function.

```python
data = (0, 1, 2, 3, 4, 5, 4, 5, 6, 0)
result = Linque(data).last(lambda d: d > 4)
print(result)

# 6
```

### .last_or_default(condition, default)
Returns the last item in current sequence that satisfies specified condition or specified default value if no item
found. This call partially evaluates current sequence. This functionality is also available as a
*linque.last_or_default(sequence, condition, default)* utility function.

```python
data = (0, 1, 2, 3, 4, 5, 4, 5, 6, 0)
result = Linque(data).last_or_default(lambda d: d > 10, -1)
print(result)

# -1
```

### .max(selector)
Returns maximum value in current sequence by specified items data selector. This call fully evaluates current sequence.

```python
data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
result = Linque(data).max(lambda d: d[1])
print(result)

# 40
```

### .max_by(key)
Returns item having maximum value in current sequence by using default comparer or specified item's key. This call fully
evaluates current sequence.

```python
data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
result = Linque(data).max_by(lambda d: d[1])
print(result)

# (4, 40)
```

### .mean(selector)
Returns average value of current sequence by specified items data selector. This call fully evaluates current sequence.

```python
data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
result = Linque(data).mean(lambda d: d[1])
print(result)

# 20
```

### .median(selector)
Returns median value of current sequence by specified items data selector. This call fully evaluates current sequence.

```python
data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
result = Linque(data).median(lambda d: d[1])
print(result)

# 20
```

### .min(selector)
Returns minimum value in current sequence by specified items data selector. This call fully evaluates current sequence.

```python
data = ((0, 0), (1, -10), (2, -20), (3, -30), (4, -40))
result = Linque(data).min(lambda d: d[1])
print(result)

# -40
```

### .min_by(key)
Returns item having minimum value in current sequence by using default comparer or specified item's key. This call fully
evaluates current sequence.

```python
data = ((0, 0), (1, -10), (2, -20), (3, -30), (4, -40))
result = Linque(data).min_by(lambda d: d[1])
print(result)

# (4, -40)
```

### .select(selector)
Produces new sequence by selecting items data by specified selector. This call does not evaluate current sequence.

```python
data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
result = Linque(data).select(lambda d: d[1]).to_list()
print(result)

# [0, 10, 20, 30, 40]
```

### .select_many(selector)
Produces new sequence by selecting and flattening items data using specified selector. This call does not evaluate
current sequence.

```python
data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
result = Linque(data).flatten(lambda d: d).to_list()
print(result)

# [0, 0, 1, 10, 2, 20, 3, 30, 4, 40]
```

### .single(condition)
Returns the single item in current sequence that satisfies specified condition or raises error if none or more items
found. This call fully evaluates current sequence. This functionality is also available as a
*linque.single(sequence, condition)* utility function.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result = Linque(data).single(lambda d: 3<d<5)
print(result)

# 4
```

### .skip(count)
Produces new sequence by bypassing specified number of items in current sequence and returns the remaining items. This
call partially evaluates current sequence. This functionality is also available as a *linque.skip(sequence, n)* utility
function.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result = Linque(data).skip(4).to_list()
print(result)

# [4, 5, 6, 7, 8, 9]
```

### .skip_while(condition)
Produces new sequence by bypassing contiguous items from the start of current sequence until specified condition fails
the first time. This functionality is also available as a *linque.skip_while(sequence, condition)* utility function.

```python
data = (0, 1, 2, 3, 4, 5, 4, 3, 2, 2, 0)
result = Linque(data).skip_while(lambda d: d < 4).to_list()
print(result)

# [4, 5, 4, 3, 2, 2, 0]
```

### .sort()
Sorts elements of current sequence in ascending order by using default comparer. This call fully evaluates current
sequence.

```python
data = (8, 0, 2, 3, 5, 1, 6, 7, 4, 9)
result = Linque(data).sort().to_list()
print(result)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### .sort_by(key)
Sorts elements of current sequence in ascending order by using selected item's key. This call fully
evaluates current sequence.

```python
data = ((1, 8), (2, 0), (3, 2), (4, 3), (5, 5), (6, 1), (7, 6), (8, 7), (9, 4), (0, 9))
result = Linque(data).sort_by(lambda d: d[1]).to_list()
print(result)

# [(2, 0), (6, 1), (3, 2), (4, 3), (9, 4), (5, 5), (7, 6), (8, 7), (1, 8), (0, 9)]
```

### .sort_desc()
Produces new sequence by sorting elements of current sequence in ascending order by using default comparer. This call
fully evaluates current sequence.

```python
data = (8, 0, 2, 3, 5, 1, 6, 7, 4, 9)
result = Linque(data).sort_desc().to_list()
print(result)

# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### .sort_by_desc(key)
Produces new sequence by sorting elements of current sequence in ascending order by using selected item's key. This call
fully evaluates current sequence.

```python
data = ((1, 8), (2, 0), (3, 2), (4, 3), (5, 5), (6, 1), (7, 6), (8, 7), (9, 4), (0, 9))
result = Linque(data).sort_by_desc(lambda d: d[1]).to_list()
print(result)

# [(0, 9), (1, 8), (8, 7), (7, 6), (5, 5), (9, 4), (4, 3), (3, 2), (6, 1), (2, 0)]
```

### .sum(selector)
Returns summed value in current sequence by specified items data selector. This call fully evaluates current sequence.

```python
data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
result = Linque(data).sum(lambda d: d[1])
print(result)

# 100
```

### .take(count)
Produces new sequence by selecting specified number of contiguous items from the start of current sequence. This call
partially evaluates current sequence. This functionality is also available as a *linque.take(sequence, n)* utility
function.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result = Linque(data).take(4).to_list()
print(result)

# [0, 1, 2, 3]
```

### .take_while(condition)
Produces new sequence by selecting items from current sequence as long as specified condition is true. This call
partially evaluates current sequence. This functionality is also available as a *linque.take_while(sequence, condition)*
utility function.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result = Linque(data).take_while(lambda d: d < 4).to_list()
print(result)

# [0, 1, 2, 3]
```

### .to_dict(key, value)
Evaluates items into dictionary. This call fully evaluates current sequence.

```python
data = ((0, 1, 'a'), (0, 2, 'b'), (0, 3, 'c'))
result = Linque(data).to_dict(lambda d: d[1], lambda d: d[2])
print(result)

# {1: 'a', 2: 'b', 3: 'c'}
```

### .to_list()
Evaluate items into list. This call fully evaluates current sequence.

```python
data = (0, 1, 2, 3, 4, 0, 1)
result = Linque(data).to_list()
print(result)

# [0, 1, 2, 3, 4, 0, 1]
```

### .to_set()
Evaluate items into set. This call fully evaluates current sequence.

```python
data = (0, 1, 2, 3, 4, 0, 1)
result = Linque(data).to_set()
print(result)

# {0, 1, 2, 3, 4}
```

### .to_tuple()
Evaluate items into tuple. This call fully evaluates current sequence.

```python
data = [0, 1, 2, 3, 4, 0, 1]
result = Linque(data).to_tuple()
print(result)

# (0, 1, 2, 3, 4, 0, 1)
```

### .union(items)
Produces new sequence of unique items from current sequence and given items by using default comparer. This call does
not evaluate current sequence.  This functionality is also available as a
*linque.union(sequence, items)* utility function.

```python
data1 = ((0, 1), (0, 1), (0, 2))
data2 = ((1, 1), (1, 2), (1, 2), (0, 3))
result = Linque(data1).union(data2).to_list()
print(result)

# [(0, 1), (0, 2), (1, 1), (1, 2), (0, 3)]
```

### .union_by(items, key)
Produces new sequence of unique items from current sequence and given items by using default comparer or selected
item's key. This call does not evaluate current sequence.  This functionality is also available as a
*linque.union_by(sequence, items, key)* utility function.

```python
data1 = ((0, 1), (0, 1), (0, 2))
data2 = ((1, 1), (1, 2), (1, 2), (0, 3))
result = Linque(data1).union_by(data2, lambda d: d[1]).to_list()
print(result)

# [(0, 1), (0, 2), (0, 3)]
```

### .where(condition)
Produces new sequence by selecting items by specified predicate. This call does not evaluate current sequence.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result = Linque(data).where(lambda d: d % 2).to_list()
print(result)

# [1, 3, 5, 7, 9]
```

### .zip(\*sequences)
Produces new sequence by merging given sequences with current sequence as long as there are items available in all
sequences. This call does not evaluate current sequence.

```python
data1 = (0, 1, 2, 3, 4)
data2 = ('a', 'b', 'c')
result = Linque(data1).zip(data2).to_list()
print(result)

# [(0, 'a'), (1, 'b'), (2, 'c')]
```


## Disclaimer

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
