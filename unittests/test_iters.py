#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import unittest
import linque


class TestCase(unittest.TestCase):
    """Test case for iterators functions."""
    
    
    def test_aggregate(self):
        """Tests whether count works correctly."""
        
        data = (97, 103, 103, 114, 101, 103, 97, 116, 101)
        
        items = data
        self.assertEqual(linque.aggregate(items, lambda r, n: r+chr(n), ''), 'aggregate')
        
        items = (d for d in data)
        self.assertEqual(linque.aggregate(items, lambda r, n: r+chr(n), ''), 'aggregate')
    
    
    def test_argmax(self):
        """Tests whether argmax works correctly."""
        
        data = (3, 1, 2, 0, 9, 7, 8)
        
        items = data
        self.assertEqual(linque.argmax(items), 4)
        
        items = (d for d in data)
        self.assertEqual(linque.argmax(items), 4)
        
        data = ((0, 3), (1, 1), (2, 2), (3, 0), (4, 9), (5, 7), (6, 8))
        
        items = data
        self.assertEqual(linque.argmax(items, lambda d: d[1]), 4)
        
        items = (d for d in data)
        self.assertEqual(linque.argmax(items, lambda d: d[1]), 4)
    
    
    def test_argmin(self):
        """Tests whether argmin works correctly."""
        
        data = (3, 1, 2, 0, 9, 7, 8)
        
        items = data
        self.assertEqual(linque.argmin(items), 3)
        
        items = (d for d in data)
        self.assertEqual(linque.argmin(items), 3)
        
        data = ((0, 3), (1, 1), (2, 2), (3, 0), (4, 9), (5, 7), (6, 8))
        
        items = data
        self.assertEqual(linque.argmin(items, lambda d: d[1]), 3)
        
        items = (d for d in data)
        self.assertEqual(linque.argmin(items, lambda d: d[1]), 3)
    
    
    def test_argsort(self):
        """Tests whether argsort works correctly."""
        
        data = (3, 1, 2)
        
        items = data
        self.assertEqual(linque.argsort(items), [1, 2, 0])
        self.assertEqual(linque.argsort(items, reverse=True), [0, 2, 1])
        
        items = (d for d in data)
        self.assertEqual(linque.argsort(items), [1, 2, 0])
        
        items = (d for d in data)
        self.assertEqual(linque.argsort(items, reverse=True), [0, 2, 1])
        
        data = ((2, 3), (1, 1), (3, 2))
        
        items = data
        self.assertEqual(linque.argsort(items, lambda d: d[1]), [1, 2, 0])
        self.assertEqual(linque.argsort(items, lambda d: d[1], reverse=True), [0, 2, 1])
        
        items = (d for d in data)
        self.assertEqual(linque.argsort(items, lambda d: d[1]), [1, 2, 0])
        
        items = (d for d in data)
        self.assertEqual(linque.argsort(items, lambda d: d[1], reverse=True), [0, 2, 1])
    
    
    def test_bisect(self):
        """Tests whether binary search works correctly."""
        
        # test values in-between
        values = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertEqual(linque.bisect(values, 2.5), 3)
        self.assertEqual(linque.bisect(values, 2.5, side='right'), 3)
        
        # test exact value
        values = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertEqual(linque.bisect(values, 2), 2)
        self.assertEqual(linque.bisect(values, 2, side='right'), 3)
        
        # test value below range
        values = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertEqual(linque.bisect(values, -1), 0)
        self.assertEqual(linque.bisect(values, -1, side='right'), 0)
        
        # test value above range
        values = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertEqual(linque.bisect(values, 10), len(values))
        self.assertEqual(linque.bisect(values, 10, side='right'), len(values))
        
        # test repeating values
        values = (0, 1, 2, 2, 2, 2, 2, 2, 8, 9)
        self.assertEqual(linque.bisect(values, 1.5), 2)
        self.assertEqual(linque.bisect(values, 2), 2)
        self.assertEqual(linque.bisect(values, 2.5), 8)
        self.assertEqual(linque.bisect(values, 1.5, side='right'), 2)
        self.assertEqual(linque.bisect(values, 2, side='right'), 8)
        self.assertEqual(linque.bisect(values, 2.5, side='right'), 8)
    
    
    def test_chunk(self):
        """Tests whether chunk works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        items = data
        self.assertEqual(tuple(linque.chunk(items, 3)), ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9,)))
        
        items = (d for d in data)
        self.assertEqual(tuple(linque.chunk(items, 3)), ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9,)))
    
    
    def test_concat(self):
        """Tests whether concat works correctly."""
        
        data1 = (0, 1, 2, 3, 4)
        data2 = (5, 6, 7, 8, 9)
        
        items1 = data1
        items2 = data2
        self.assertEqual(tuple(linque.concat(items1, items2)), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
        
        items1 = (d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(tuple(linque.concat(items1, items2)), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    
    
    def test_count(self):
        """Tests whether count works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        items = data
        self.assertEqual(linque.count(items), 10)
        self.assertEqual(linque.count(items, lambda d: d > 4), 5)
        
        items = (d for d in data)
        self.assertEqual(linque.count(items), 10)
        
        items = (d for d in data)
        self.assertEqual(linque.count(items, lambda d: d > 4), 5)
    
    
    def test_distinct(self):
        """Tests whether distinct works correctly."""
        
        data = ((0, 1), (0, 1), (0, 2), (1, 1), (1, 2))
        
        items = data
        self.assertEqual(tuple(linque.distinct(items)), ((0, 1), (0, 2), (1, 1), (1, 2)))
        
        items = (d for d in data)
        self.assertEqual(tuple(linque.distinct(items)), ((0, 1), (0, 2), (1, 1), (1, 2)))
        
        data = ((0, 1), (0, 1), (0, 2), (1, 1), (1, 2))
        
        items = data
        self.assertEqual(tuple(linque.distinct(items, lambda d: d[1])), ((0, 1), (0, 2)))
        
        items = (d for d in data)
        self.assertEqual(tuple(linque.distinct(items, lambda d: d[1])), ((0, 1), (0, 2)))
    
    
    def test_exclude(self):
        """Tests whether exclude works correctly."""
        
        data1 = ((0, 1), (0, 1), (0, 2), (1, 2), (0, 3), (0, 4))
        data2 = ((0, 1), (1, 2), (1, 2), (1, 3))
        
        items1 = data1
        items2 = data2
        self.assertEqual(tuple(linque.exclude(items1, items2)), ((0, 2), (0, 3), (0, 4)))
        
        items1 = (d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(tuple(linque.exclude(items1, items2)), ((0, 2), (0, 3), (0, 4)))
        
        items1 = data1
        items2 = data2
        self.assertEqual(tuple(linque.exclude(items1, items2, lambda d: d[1])), ((0, 4),))
        
        items1 = (d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(tuple(linque.exclude(items1, items2, lambda d: d[1])), ((0, 4),))
    
    
    def test_first(self):
        """Tests whether first works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        items = data
        self.assertEqual(linque.first(items), 0)
        
        items = (d for d in data)
        self.assertEqual(linque.first(items), 0)
        
        items = data
        self.assertEqual(linque.first(items, lambda d: d > 4), 5)
        
        items = (d for d in data)
        self.assertEqual(linque.first(items, lambda d: d > 4), 5)
        
        items = data
        self.assertEqual(linque.first(items, lambda d: d > 10, -1), -1)
        
        items = (d for d in data)
        self.assertEqual(linque.first(items, lambda d: d > 10, -1), -1)
        
        items = data
        with self.assertRaises(StopIteration):
            linque.first(items, lambda d: d > 10)
        
        items = (d for d in data)
        with self.assertRaises(StopIteration):
            linque.first(items, lambda d: d > 10)
    
    
    def test_group(self):
        """Tests whether group works correctly."""
        
        data = ((0, 1), (0, 1), (0, 2), (1, 1))
        
        items = data
        self.assertEqual(tuple(linque.group(items)), (
            ((0, 1), ((0, 1), (0, 1))),
            ((0, 2), ((0, 2),)),
            ((1, 1), ((1, 1),))))
        
        items = (d for d in data)
        self.assertEqual(tuple(linque.group(items)), (
            ((0, 1), ((0, 1), (0, 1))),
            ((0, 2), ((0, 2),)),
            ((1, 1), ((1, 1),))))
        
        items = data
        self.assertEqual(tuple(linque.group(items, lambda d: d[1])), (
            (1, ((0, 1), (0, 1), (1, 1))),
            (2, ((0, 2),))))
        
        items = (d for d in data)
        self.assertEqual(tuple(linque.group(items, lambda d: d[1])), (
            (1, ((0, 1), (0, 1), (1, 1))),
            (2, ((0, 2),))))
    
    
    def test_index(self):
        """Tests whether index works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        items = data
        self.assertEqual(linque.index(items, lambda d: d > 4), 5)
        
        items = (d for d in data)
        self.assertEqual(linque.index(items, lambda d: d > 4), 5)
    
    
    def test_intersect(self):
        """Tests whether intersect works correctly."""
        
        data1 = ((0, 1), (0, 1), (0, 2), (1, 2))
        data2 = ((0, 1), (1, 2), (1, 2), (0, 3))
        
        items1 = data1
        items2 = data2
        self.assertEqual(tuple(linque.intersect(items1, items2)), ((0, 1), (1, 2)))
        
        items1 = (d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(tuple(linque.intersect(items1, items2)), ((0, 1), (1, 2)))
        
        items1 = data1
        items2 = data2
        self.assertEqual(tuple(linque.intersect(items1, items2, lambda d: d[1])), ((0, 1), (0, 2)))
        
        items1 = (d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(tuple(linque.intersect(items1, items2, lambda d: d[1])), ((0, 1), (0, 2)))
    
    
    def test_last(self):
        """Tests whether last works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 4, 5, 6, 1)
        
        items = data
        self.assertEqual(linque.last(items), 1)
        
        items = (d for d in data)
        self.assertEqual(linque.last(items), 1)
        
        items = data
        self.assertEqual(linque.last(items, lambda d: d > 4), 6)
        
        items = (d for d in data)
        self.assertEqual(linque.last(items, lambda d: d > 4), 6)
        
        items = data
        self.assertEqual(linque.last(items, lambda d: d > 10, -1), -1)
        
        items = (d for d in data)
        self.assertEqual(linque.last(items, lambda d: d > 10, -1), -1)
        
        items = data
        with self.assertRaises(StopIteration):
            linque.last(items, lambda d: d > 10)
        
        items = (d for d in data)
        with self.assertRaises(StopIteration):
            linque.last(items, lambda d: d > 10)
    
    
    def test_multisort(self):
        """Tests whether multisort works correctly."""
        
        data = ((1, "d", 11), (0, "a", 10), (0, "c", 100), (0, "b", 1000), (0, "b", 100), (1, "e", 10), (2, "f", 20))
        
        items = data
        
        model = [(0, "a", 10), (0, "b", 100), (0, "b", 1000), (0, "c", 100), (1, "d", 11), (1, "e", 10), (2, "f", 20)]
        self.assertEqual(linque.multisort(items), model)
        
        model = [(2, "f", 20), (1, "e", 10), (1, "d", 11), (0, "c", 100), (0, "b", 1000), (0, "b", 100), (0, "a", 10)]
        self.assertEqual(linque.multisort(items, reverse=True), model)
        
        model = [(0, "a", 10), (0, "b", 100), (0, "b", 1000), (0, "c", 100), (1, "d", 11), (1, "e", 10), (2, "f", 20)]
        self.assertEqual(linque.multisort(items, reverse=[False, False, False]), model)
        
        model = [(2, "f", 20), (1, "e", 10), (1, "d", 11), (0, "c", 100), (0, "b", 1000), (0, "b", 100), (0, "a", 10)]
        self.assertEqual(linque.multisort(items, reverse=[True, True, True]), model)
        
        model = [(2, "f", 20), (1, "d", 11), (1, "e", 10), (0, "a", 10), (0, "b", 100), (0, "b", 1000), (0, "c", 100)]
        self.assertEqual(linque.multisort(items, reverse=[True, False, False]), model)
        
        model = [(2, "f", 20), (1, "d", 11), (1, "e", 10), (0, "a", 10), (0, "b", 1000), (0, "b", 100), (0, "c", 100)]
        self.assertEqual(linque.multisort(items, reverse=[True, False, True]), model)
        
        model = [(2, "f", 20), (1, "e", 10), (1, "d", 11), (0, "c", 100), (0, "b", 100), (0, "b", 1000), (0, "a", 10)]
        self.assertEqual(linque.multisort(items, reverse=[True, True, False]), model)
        
        model = [(0, "c", 100), (0, "b", 1000), (0, "b", 100), (0, "a", 10), (1, "e", 10), (1, "d", 11), (2, "f", 20)]
        self.assertEqual(linque.multisort(items, reverse=[False, True, True]), model)
        
        model = [(0, "a", 10), (0, "b", 1000), (0, "b", 100), (0, "c", 100), (1, "d", 11), (1, "e", 10), (2, "f", 20)]
        self.assertEqual(linque.multisort(items, reverse=[False, False, True]), model)
        
        model = [(0, "a", 10), (0, "b", 1000), (0, "b", 100), (0, "c", 100), (1, "d", 11), (1, "e", 10), (2, "f", 20)]
        self.assertEqual(linque.multisort(items, key=lambda d: (d[0], d[1])), model)
        
        model = [(2, "f", 20), (1, "e", 10), (1, "d", 11), (0, "c", 100), (0, "b", 1000), (0, "b", 100), (0, "a", 10)]
        self.assertEqual(linque.multisort(items, key=lambda d: (d[0], d[1]), reverse=True), model)
        
        model = [(0, "a", 10), (0, "b", 1000), (0, "b", 100), (0, "c", 100), (1, "d", 11), (1, "e", 10), (2, "f", 20)]
        self.assertEqual(linque.multisort(items, key=lambda d: (d[0], d[1]), reverse=[False, False]), model)
        
        model = [(2, "f", 20), (1, "e", 10), (1, "d", 11), (0, "c", 100), (0, "b", 1000), (0, "b", 100), (0, "a", 10)]
        self.assertEqual(linque.multisort(items, key=lambda d: (d[0], d[1]), reverse=[True, True]), model)
        
        model = [(2, "f", 20), (1, "d", 11), (1, "e", 10), (0, "a", 10), (0, "b", 1000), (0, "b", 100), (0, "c", 100)]
        self.assertEqual(linque.multisort(items, key=lambda d: (d[0], d[1]), reverse=[True, False]), model)
        
        model = [(0, "c", 100), (0, "b", 1000), (0, "b", 100), (0, "a", 10), (1, "e", 10), (1, "d", 11), (2, "f", 20)]
        self.assertEqual(linque.multisort(items, key=lambda d: (d[0], d[1]), reverse=[False, True]), model)
        
        model = [(0, "a", 10), (1, "e", 10), (1, "d", 11), (2, "f", 20), (0, "c", 100), (0, "b", 100), (0, "b", 1000)]
        self.assertEqual(linque.multisort(items, key=lambda d: (d[2], d[0])), model)
        
        model = [(0, "b", 1000), (0, "c", 100), (0, "b", 100), (2, "f", 20), (1, "d", 11), (1, "e", 10), (0, "a", 10)]
        self.assertEqual(linque.multisort(items, key=lambda d: (d[2], d[0]), reverse=True), model)
        
        model = [(0, "a", 10), (1, "e", 10), (1, "d", 11), (2, "f", 20), (0, "c", 100), (0, "b", 100), (0, "b", 1000)]
        self.assertEqual(linque.multisort(items, key=lambda d: (d[2], d[0]), reverse=[False, False]), model)
        
        model = [(0, "b", 1000), (0, "c", 100), (0, "b", 100), (2, "f", 20), (1, "d", 11), (1, "e", 10), (0, "a", 10)]
        self.assertEqual(linque.multisort(items, key=lambda d: (d[2], d[0]), reverse=[True, True]), model)
        
        model = [(0, "b", 1000), (0, "c", 100), (0, "b", 100), (2, "f", 20), (1, "d", 11), (0, "a", 10), (1, "e", 10)]
        self.assertEqual(linque.multisort(items, key=lambda d: (d[2], d[0]), reverse=[True, False]), model)
        
        model = [(1, "e", 10), (0, "a", 10), (1, "d", 11), (2, "f", 20), (0, "c", 100), (0, "b", 100), (0, "b", 1000)]
        self.assertEqual(linque.multisort(items, key=lambda d: (d[2], d[0]), reverse=[False, True]), model)
        
        items = (d for d in data)
        
        model = [(0, "c", 100), (0, "b", 1000), (0, "b", 100), (0, "a", 10), (1, "e", 10), (1, "d", 11), (2, "f", 20)]
        self.assertEqual(linque.multisort(items, reverse=[False, True, True]), model)
        
        items = (d for d in data)
        
        model = [(0, "c", 100), (0, "b", 1000), (0, "b", 100), (0, "a", 10), (1, "e", 10), (1, "d", 11), (2, "f", 20)]
        self.assertEqual(linque.multisort(items, key=lambda d: (d[0], d[1]), reverse=[False, True]), model)
    
    
    def test_rank(self):
        """Tests whether rank works correctly."""
        
        data = (0, 2, 3, 2)
        
        self.assertEqual(linque.rank(data, method='average'), [1, 2.5, 4, 2.5])
        self.assertEqual(linque.rank(data, method='min'), [1, 2, 4, 2])
        self.assertEqual(linque.rank(data, method='max'), [1, 3, 4, 3])
        self.assertEqual(linque.rank(data, method='dense'), [1, 2, 3, 2])
        self.assertEqual(linque.rank(data, method='ordinal'), [1, 2, 4, 3])
        
        self.assertEqual(linque.rank(data, method='average', reverse=True), [4, 2.5, 1, 2.5])
        self.assertEqual(linque.rank(data, method='min', reverse=True), [4, 2, 1, 2])
        self.assertEqual(linque.rank(data, method='max', reverse=True), [4, 3, 1, 3])
        self.assertEqual(linque.rank(data, method='dense', reverse=True), [3, 2, 1, 2])
        self.assertEqual(linque.rank(data, method='ordinal', reverse=True), [4, 2, 1, 3])
        
        items = (d for d in data)
        self.assertEqual(linque.rank(items, method='average'), [1, 2.5, 4, 2.5])
        
        items = (d for d in data)
        self.assertEqual(linque.rank(items, method='min'), [1, 2, 4, 2])
        
        items = (d for d in data)
        self.assertEqual(linque.rank(items, method='max'), [1, 3, 4, 3])
        
        items = (d for d in data)
        self.assertEqual(linque.rank(items, method='dense'), [1, 2, 3, 2])
        
        items = (d for d in data)
        self.assertEqual(linque.rank(items, method='ordinal'), [1, 2, 4, 3])
        
        data = ((2, 0), (3, 2), (2, 3), (0, 2))
        
        self.assertEqual(linque.rank(data, lambda d: d[1], method='average'), [1, 2.5, 4, 2.5])
        self.assertEqual(linque.rank(data, lambda d: d[1], method='min'), [1, 2, 4, 2])
        self.assertEqual(linque.rank(data, lambda d: d[1], method='max'), [1, 3, 4, 3])
        self.assertEqual(linque.rank(data, lambda d: d[1], method='dense'), [1, 2, 3, 2])
        self.assertEqual(linque.rank(data, lambda d: d[1], method='ordinal'), [1, 2, 4, 3])
        
        self.assertEqual(linque.rank(data, lambda d: d[1], method='average', reverse=True), [4, 2.5, 1, 2.5])
        self.assertEqual(linque.rank(data, lambda d: d[1], method='min', reverse=True), [4, 2, 1, 2])
        self.assertEqual(linque.rank(data, lambda d: d[1], method='max', reverse=True), [4, 3, 1, 3])
        self.assertEqual(linque.rank(data, lambda d: d[1], method='dense', reverse=True), [3, 2, 1, 2])
        self.assertEqual(linque.rank(data, lambda d: d[1], method='ordinal', reverse=True), [4, 2, 1, 3])
        
        items = (d for d in data)
        self.assertEqual(linque.rank(items, lambda d: d[1], method='average'), [1, 2.5, 4, 2.5])
        
        items = (d for d in data)
        self.assertEqual(linque.rank(items, lambda d: d[1], method='min'), [1, 2, 4, 2])
        
        items = (d for d in data)
        self.assertEqual(linque.rank(items, lambda d: d[1], method='max'), [1, 3, 4, 3])
        
        items = (d for d in data)
        self.assertEqual(linque.rank(items, lambda d: d[1], method='dense'), [1, 2, 3, 2])
        
        items = (d for d in data)
        self.assertEqual(linque.rank(items, lambda d: d[1], method='ordinal'), [1, 2, 4, 3])
    
    
    def test_single(self):
        """Tests whether single works correctly."""
        
        data = (42, )
        
        items = data
        self.assertEqual(linque.single(items), 42)
        
        items = (d for d in data)
        self.assertEqual(linque.single(items), 42)
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        items = data
        self.assertEqual(linque.single(items, lambda d: 3 < d < 5), 4)
        
        items = (d for d in data)
        self.assertEqual(linque.single(items, lambda d: 3 < d < 5), 4)
        
        items = data
        self.assertEqual(linque.single(items, lambda d: d > 10, -1), -1)
        
        items = (d for d in data)
        self.assertEqual(linque.single(items, lambda d: d > 10, -1), -1)
        
        items = data
        with self.assertRaises(ValueError):
            linque.single(items)
        
        items = (d for d in data)
        with self.assertRaises(ValueError):
            linque.single(items)
        
        items = data
        with self.assertRaises(ValueError):
            linque.single(items, lambda d: d > 5)
        
        items = (d for d in data)
        with self.assertRaises(ValueError):
            linque.single(items, lambda d: d > 5)
        
        items = data
        with self.assertRaises(ValueError):
            linque.single(items, lambda d: d > 5, -1)
        
        items = (d for d in data)
        with self.assertRaises(ValueError):
            linque.single(items, lambda d: d > 5, -1)
    
    
    def test_skip(self):
        """Tests whether skip works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        items = data
        self.assertEqual(tuple(linque.skip(items, 4)), (4, 5, 6, 7, 8, 9))
        
        items = (d for d in data)
        self.assertEqual(tuple(linque.skip(items, 4)), (4, 5, 6, 7, 8, 9))
    
    
    def test_skip_while(self):
        """Tests whether skip_while works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 4, 3, 2, 2, 0)
        
        items = data
        self.assertEqual(tuple(linque.skip_while(items, lambda d: d < 4)), (4, 5, 4, 3, 2, 2, 0))
        
        items = (d for d in data)
        self.assertEqual(tuple(linque.skip_while(items, lambda d: d < 4)), (4, 5, 4, 3, 2, 2, 0))
    
    
    def test_take(self):
        """Tests whether take works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        items = data
        self.assertEqual(tuple(linque.take(items, 4)), (0, 1, 2, 3))
        
        items = (d for d in data)
        self.assertEqual(tuple(linque.take(items, 4)), (0, 1, 2, 3))
    
    
    def test_take_while(self):
        """Tests whether take_while works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        items = data
        self.assertEqual(tuple(linque.take_while(items, lambda d: d < 4)), (0, 1, 2, 3))
        
        items = (d for d in data)
        self.assertEqual(tuple(linque.take_while(items, lambda d: d < 4)), (0, 1, 2, 3))
        
        items = (d for d in data)
        self.assertEqual(tuple(linque.take_while(items, lambda d: d < 20)), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    
    
    def test_union(self):
        """Tests whether union works correctly."""
        
        data1 = ((0, 1), (0, 1), (0, 2))
        data2 = ((1, 1), (1, 2), (1, 2), (0, 3))
        
        items1 = data1
        items2 = data2
        self.assertEqual(tuple(linque.union(items1, items2)), ((0, 1), (0, 2), (1, 1), (1, 2), (0, 3)))
        
        items1 = (d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(tuple(linque.union(items1, items2)), ((0, 1), (0, 2), (1, 1), (1, 2), (0, 3)))
        
        items1 = data1
        items2 = data2
        self.assertEqual(tuple(linque.union(items1, items2, lambda d: d[1])), ((0, 1), (0, 2), (0, 3)))
        
        items1 = (d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(tuple(linque.union(items1, items2, lambda d: d[1])), ((0, 1), (0, 2), (0, 3)))


# run test case
if __name__ == "__main__":
    unittest.main(verbosity=2)
