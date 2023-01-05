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
    .group(lambda d: len(d)) \
    .sort(lambda d: d[0]) \
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
linq = Linque((d for d in range(10)), evaluate=True)
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


## Available Operations

### Quantifier Operations

- [all](#allcondition): Determines whether all items satisfy given condition.
- [any](#anycondition): Determines whether a sequence contains any item or whether any item satisfies given condition.
- [contains](#containsvalue-key): Determines whether a sequence contains item with given value by using default comparer or specified item's key.

### Search Operations

- [argmax](#argmaxkey): Returns index of the maximum item in a sequence by using default comparer or specified item's key.
- [argmin](#argminkey): Returns index of the minimum item in a sequence by using default comparer or specified item's key.
- [first](#firstcondition-default): Returns the first item that satisfies specified condition or specified default value if provided.
- [last](#lastcondition-default): Returns the last item that satisfies specified condition or specified default value if provided.
- [max](#maxkey): Returns item having maximum value in a sequence by using default comparer or specified item's key.
- [min](#minkey): Returns item having minimum value in a sequence by using default comparer or specified item's key.
- [single](#singlecondition-default): Returns the single item that satisfies specified condition, specified default value or raises error.
- [where](#wherecondition): Produces new sequence by selecting items by specified predicate.

### Sorting Operations

- [argsort](#argsortkey-reverse): Returns items indices that would sort current sequence by using default comparer or selected item's key.
- [reverse](#reverse): Produces new sequence by inverting order of items.
- [rank](#rankkey-method-reverse): Provides 1-based rank for each item of current sequence by using default comparer or selected item's key.
- [sort](#sortkey-reverse): Produces new sequence by sorting elements by using default comparer or selected item's key.

### Projection Operations

- [flatten](#flattenselector): Produces new sequence by selecting and flattening items data using specified selector.
- [select](#selectselector): Produces new sequence by selecting items data by specified selector.
- [select_many](#select_manyselector): Produces new sequence by selecting and flattening items data using specified selector.
- [zip](#zipsequences): Produces new sequence by merging given sequences as long as there are items in all sequences.

### Random Operations
- [choice](#choiceweights-seed): Returns random item from current sequence.
- [choices](#choicescount-weights-seed): Produces new sequence by randomly choosing number of items from current sequence.
- [sample](#samplecount-seed): Produces new sequence by randomly sample number of items from current sequence.
- [shuffle](#shuffleseed): Produces new sequence by randomly shuffling items from current sequence.

### Grouping Operations

- [group](#groupkey): Produces new sequence by grouping items according to default comparer or specified key selector.

### Partitioning Operations

- [chunk](#chunksize): Produces new sequence by splitting into chunks of specified size.
- [skip](#skipcount): Produces new sequence by bypassing specified number of items and returns the remaining items.
- [skip_while](#skip_whilecondition): Produces new sequence by bypassing contiguous items from the start until specified condition fails.
- [take](#takecount): Produces new sequence by selecting specified number of contiguous items.
- [take_while](#take_whilecondition): Produces new sequence by selecting items as long as specified condition is true.

### Concatenation Operations

- [concat](#concatitems): Produces new sequence by appending given items at the end of a sequence. 

### Set Operations

- [distinct](#distinctkey): Produces new sequence by selecting distinct items by using default comparer or specified item's key.
- [exclude](#excludeitems-key): Produces new sequence by excluding specified items by using default comparer or selected item's key.
- [intersect](#intersectitems-key): Produces new sequence of shared unique items by using default comparer or selected item's key.
- [union](#unionitems-key): Produces new sequence of unique items by using default comparer or selected item's key.

### Converting Operations

- [each](#eachaction): Applies specified function to every item in a sequence.
- [enumerate](#enumerate): Produces new sequence by enumerating items into (index, item) pairs.
- [evaluate](#evaluate): Evaluates all the iterators in a sequence and stores items as internal list.
- [to_dict](#to_dictkey-value): Evaluates items into dictionary.
- [to_list](#to_list): Evaluates items into list.
- [to_set](#to_set): Evaluates items into set.
- [to_tuple](#to_tuple): Evaluates items into tuple.

### Aggregation Operations

- [aggregate](#aggregateaccumulator-seed): Applies accumulator function over a sequence.
- [count](#countcondition): Returns number of items in a sequence satisfying given condition.
- [maximum](#maximumselector): Returns maximum value in a sequence by specified items data selector.
- [mean](#meanselector): Returns average value of a sequence by specified items data selector.
- [median](#medianselector): Returns median value of a sequence by specified items data selector.
- [minimum](#minimumselector): Returns minimum value in a sequence by specified items data selector.
- [sum](#sumselector): Returns summed value in a sequence by specified items data selector.


## Examples

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

### .argmax(key)
Returns index of the maximum item in a sequence by using default comparer or specified item's key. This call fully
evaluates current sequence. This functionality is also available as a *linque.argmax(sequence, key)*
utility function.

```python
data = (3, 1, 2, 0, 9, 7, 8)
result = Linque(data).argmax()
print(result)

# 4

data = ((0, 3), (1, 1), (2, 2), (3, 0), (4, 9), (5, 7), (6, 8))
result = Linque(data).argmax(lambda d: d[1])
print(result)

# 4
```

### .argmin(key)
Returns index of the minimum item in a sequence by using default comparer or specified item's key. This call fully
evaluates current sequence. This functionality is also available as a *linque.argmin(sequence, key)*
utility function.

```python
data = (3, 1, 2, 0, 9, 7, 8)
result = Linque(data).argmin()
print(result)

# 3

data = ((0, 3), (1, 1), (2, 2), (3, 0), (4, 9), (5, 7), (6, 8))
result = Linque(data).argmin(lambda d: d[1])
print(result)

# 3
```

### .argsort(key, reverse)
Returns items indices that would sort current sequence by using default comparer or specified item's key. This call
fully evaluates current sequence. This functionality is also available as a *linque.argsort(sequence, key, reverse)*
utility function.

```python
data = (3, 1, 2)
result = Linque(data).argsort().to_list()
print(result)

# [1, 2, 0]

data = ((2, 3), (1, 1), (3, 2))
result = Linque(data).argsort(lambda d: d[1]).to_list()
print(result)

# [1, 2, 0]
```

### .choice(weights, seed)
Returns random item from current sequence. This call fully evaluates current sequence.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result = Linque(data).choice()
print(result)

# 7
```

### .choices(count, weights, seed)
Produces new sequence by randomly choosing items from current sequence. Each item can be selected multiple times.
This call fully evaluates current sequence.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result = Linque(data).choices(20).to_list()
print(result)

# [7, 0, 0, 0, 4, 7, 3, 1, 5, 0, 1, 6, 7, 1, 2, 6, 8, 0, 5, 8]
```

### .chunk(size)
Produces new sequence by splitting current sequence into chunks of specified size. This call does not evaluate current
sequence. This functionality is also available as a *linque.chunk(sequence, size)* utility function.

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

### .contains(value, key)
Determines whether current sequence contains item with given value by using default comparer or specified item's key.
This call partially evaluates current sequence.

```python
data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
result = Linque(data).contains((1, 10))
print(result)

# True

data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
result = Linque(data).contains(10, lambda d: d[1])
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

### .distinct(key)
Produces new sequence by selecting distinct items from current sequence using default comparer or specified item's key.
First occurrence of each item is used. This call does not evaluate current sequence. This functionality is also
available as a *linque.distinct(sequence, items, key)* utility function.

```python
data = ((0, 1), (0, 1), (0, 2), (1, 1), (1, 2))
result = Linque(data).distinct().to_list()
print(result)

# [(0, 1), (0, 2), (1, 1), (1, 2)]

data = ((0, 1), (0, 1), (0, 2), (1, 1), (1, 2))
result = Linque(data).distinct(lambda d: d[1]).to_list()
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

### .exclude(items, key)
Produces new sequence by excluding specified items from current sequence using default comparer or selected item's key.
This call does not evaluate current sequence. This functionality is also available as a
*linque.exclude(sequence, items, key)* utility function.

```python
data1 = ((0, 1), (0, 1), (0, 2), (1, 2), (0, 3), (0, 4))
data2 = ((0, 1), (1, 2), (1, 2), (1, 3))

result = Linque(data1).exclude(data2).to_list()
print(result)

# [(0, 2), (0, 3), (0, 4)]

result = Linque(data1).exclude(data2, lambda d: d[1]).to_list()
print(result)

# [(0, 4)]
```

### .first(condition, default)
Returns the first item in current sequence that satisfies specified condition or specified default value if provided and
no item found. This call partially evaluates current sequence. This functionality is also available as a
*linque.first(sequence, condition, default)* utility function.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

result = Linque(data).first(lambda d: d > 4)
print(result)

# 5

result = Linque(data).first(lambda d: d > 10, -1)
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

### .group(key)
Produces new sequence by grouping items of current sequence according to specified key selector and creates result
values as (key, group) pairs. This call fully evaluates current sequence. This functionality is also available as a
*linque.group(sequence, key)* utility function.

```python
data = ((0, 1), (0, 1), (0, 2), (1, 1))

result = Linque(data).group().to_dict(lambda d: d[0], lambda d: d[1].to_list())
print(result)

# {
#     (0, 1): [(0, 1), (0, 1)], 
#     (0, 2): [(0, 2)],
#     (1, 1): [(1, 1)]
# }

result = Linque(data).group(lambda d: d[1]).to_dict(lambda d: d[0], lambda d: d[1].to_list())
print(result)

# {
#     1: [(0, 1), (0, 1), (1, 1)], 
#     2: [(0, 2)],
# }
```

### .intersect(items, key)
Produces new sequence of shared unique items from current sequence and given items by using default comparer or selected
item's key. This call does not evaluate current sequence. This functionality is also available as a
*linque.intersect(sequence, items, key)* utility function.

```python
data1 = ((0, 1), (0, 1), (0, 2), (1, 2))
data2 = ((0, 1), (1, 2), (1, 2), (0, 3))

result = Linque(data1).intersect(data2).to_list()
print(result)

# [(0, 1), (1, 2)]

result = Linque(data1).intersect(data2, lambda d: d[1]).to_list()
print(result)

# [(0, 1), (0, 2)]
```

### .last(condition, default)
Returns the last item in current sequence that satisfies specified condition or specified default value if provided and
no item  found. This call partially evaluates current sequence. This functionality is also available as a
*linque.last(sequence, condition, default)* utility function.

```python
data = (0, 1, 2, 3, 4, 5, 4, 5, 6, 0)

result = Linque(data).last(lambda d: d > 4)
print(result)

# 6

result = Linque(data).last(lambda d: d > 10, -1)
print(result)

# -1
```

### .maximum(selector)
Returns maximum value in current sequence by specified items data selector. This call fully evaluates current sequence.

```python
data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
result = Linque(data).maximum(lambda d: d[1])
print(result)

# 40
```

### .max(key)
Returns item having maximum value in current sequence by using specified item's key. This call fully evaluates current
sequence.

```python
data = ((0, 0), (1, 100), (20, 20), (3, 30), (4, 40))

result = Linque(data).max()
print(result)

# (20, 20)

result = Linque(data).max(lambda d: d[1])
print(result)

# (1, 100)
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

### .minimum(selector)
Returns minimum value in current sequence by specified items data selector. This call fully evaluates current sequence.

```python
data = ((0, 0), (1, -10), (2, -20), (3, -30), (4, -40))
result = Linque(data).minimum(lambda d: d[1])
print(result)

# -40
```

### .min(key)
Returns item having minimum value in current sequence by using specified item's key. This call fully evaluates current
sequence.

```python
data = ((0, 0), (1, -100), (-2, -20), (3, -30), (4, -40))

result = Linque(data).min()
print(result)

# (-2, -20)

result = Linque(data).min(lambda d: d[1])
print(result)

# (1, -100)
```

### .rank(key, method, reverse)
Provides 1-based rank for each item of current sequence by using default comparer or selected item's key. The ties are
resolved according to selected method. This call fully evaluates current sequence. This functionality is also available
as a *linque.rank(sequence, key, method, reverse)* utility function.

```python
data = (0, 2, 3, 2)

result = Linque(data).rank(method='average').to_list()
print(result)

# [1, 2.5, 4, 2.5]

result = Linque(data).rank(method='min').to_list()
print(result)

# [1, 2, 4, 2]

result = Linque(data).rank(method='max').to_list()
print(result)

# [1, 3, 4, 3]

result = Linque(data).rank(method='dense').to_list()
print(result)

# [1, 2, 3, 2]

result = Linque(data).rank(method='ordinal').to_list()
print(result)

# [1, 2, 4, 3]

data = ((2, 0), (3, 2), (2, 3), (0, 2))

result = Linque(data).rank(lambda d: d[1], method='average').to_list()
print(result)

# [1, 2.5, 4, 2.5]

result = Linque(data).rank(lambda d: d[1], method='min').to_list()
print(result)

# [1, 2, 4, 2]

result = Linque(data).rank(lambda d: d[1], method='max').to_list()
print(result)

# [1, 3, 4, 3]

result = Linque(data).rank(lambda d: d[1], method='dense').to_list()
print(result)

# [1, 2, 3, 2]

result = Linque(data).rank(lambda d: d[1], method='ordinal').to_list()
print(result)

# [1, 2, 4, 3]
```

### .reverse()
Produces new sequence by inverting order of items in current sequence. This call fully evaluates current sequence.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result = Linque(data).reverse().to_list()
print(result)

# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### .sample(count, seed)
Produces new sequence by randomly sampling items from current sequence. Each item can be selected only once.
This call fully evaluates current sequence.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result = Linque(data).sample(5).to_list()
print(result)

# [6, 3, 5, 0, 7]
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
result = Linque(data).select_many(lambda d: d).to_list()
print(result)

# [0, 0, 1, 10, 2, 20, 3, 30, 4, 40]
```

### .shuffle(seed)
Produces new sequence by randomly shuffling items from current sequence. This call fully evaluates current sequence.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
result = Linque(data).shuffle().to_list()
print(result)

# [6, 5, 3, 2, 4, 0, 1, 9, 8, 7]
```

### .single(condition, default)
Returns the single item in current sequence that satisfies specified condition or specified default value if provided
and no item found. Raises error if more items found. This call fully evaluates current sequence. This functionality is
also available as a *linque.single(sequence, condition, default)* utility function.

```python
data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

result = Linque(data).single(lambda d: 3<d<5)
print(result)

# 4

result = Linque(data).single(lambda d: d>10, -1)
print(result)

# -1
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

### .sort(key, reverse)
Sorts elements of current sequence by using default comparer or selected item's key. If the key provides multiple
columns, the sorting direction can be specified for each individual column. This call fully evaluates current sequence.
This functionality is also available as a *linque.multisort(sequence, key, reverse)* utility function.

```python
data = (8, 0, 2, 3, 5, 1, 6, 7, 4, 9)
result = Linque(data).sort().to_list()
print(result)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

data = ((1, 8), (2, 0), (3, 2), (4, 3), (5, 5), (6, 1), (7, 6), (8, 7), (9, 4), (0, 9))
result = Linque(data).sort(lambda d: d[1], reverse=True).to_list()
print(result)

# [(0, 9), (1, 8), (8, 7), (7, 6), (5, 5), (9, 4), (4, 3), (3, 2), (6, 1), (2, 0)]

data = ((1, "d", 11), (0, "a", 10), (0, "b", 1000), (0, "c", 100), (0, "b", 100), (1, "e", 10), (2, "f", 20))
result = Linque(data).sort(lambda d: (d[0], d[1]), reverse=[False, True]).to_list()
print(result)

# [(0, 'c', 100), (0, 'b', 1000), (0, 'b', 100), (0, 'a', 10), (1, 'e', 10), (1, 'd', 11), (2, 'f', 20)]
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

### .union(items, key)
Produces new sequence of unique items from current sequence and given items by using default comparer and selected
item's key. This call does not evaluate current sequence. This functionality is also available as a
*linque.union(sequence, items, key)* utility function.

```python
data1 = ((0, 1), (0, 1), (0, 2))
data2 = ((1, 1), (1, 2), (1, 2), (0, 3))

result = Linque(data1).union(data2).to_list()
print(result)

# [(0, 1), (0, 2), (1, 1), (1, 2), (0, 3)]

result = Linque(data1).union(data2, lambda d: d[1]).to_list()
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
