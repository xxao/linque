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
        self.assertEqual(tuple(linque.distinct(items, lambda d: d[1])), ((0, 1), (0, 2)))
        
        items = (d for d in data)
        self.assertEqual(tuple(linque.distinct(items)), ((0, 1), (0, 2), (1, 1), (1, 2)))
        
        items = (d for d in data)
        self.assertEqual(tuple(linque.distinct(items, lambda d: d[1])), ((0, 1), (0, 2)))
    
    
    def test_exclude(self):
        """Tests whether exclude works correctly."""
        
        data1 = ((0, 1), (0, 1), (0, 2), (1, 2), (0, 3), (0, 4))
        data2 = ((0, 1), (1, 2), (1, 2), (1, 3))
        
        items1 = data1
        items2 = data2
        self.assertEqual(tuple(linque.exclude(items1, items2)), ((0, 2), (0, 3), (0, 4)))
        self.assertEqual(tuple(linque.exclude(items1, items2, lambda d: d[1])), ((0, 4),))
        
        items1 = (d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(tuple(linque.exclude(items1, items2)), ((0, 2), (0, 3), (0, 4)))
        
        items1 = (d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(tuple(linque.exclude(items1, items2, lambda d: d[1])), ((0, 4),))
    
    
    def test_first(self):
        """Tests whether first works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        items = data
        self.assertEqual(linque.first(items, lambda d: d > 4), 5)
        
        items = (d for d in data)
        self.assertEqual(linque.first(items, lambda d: d > 4), 5)
        
        items = (d for d in data)
        self.assertEqual(linque.first(items, lambda d: d > 10, -1), -1)
    
    
    def test_group(self):
        """Tests whether group works correctly."""
        
        data = ((0, 1), (0, 1), (0, 2), (1, 1))
        
        items = data
        self.assertEqual(tuple(linque.group(items)), (
            ((0, 1), ((0, 1), (0, 1))),
            ((0, 2), ((0, 2),)),
            ((1, 1), ((1, 1),))))
        
        self.assertEqual(tuple(linque.group(items, lambda d: d[1])), (
            (1, ((0, 1), (0, 1), (1, 1))),
            (2, ((0, 2),))))
        
        items = (d for d in data)
        self.assertEqual(tuple(linque.group(items)), (
            ((0, 1), ((0, 1), (0, 1))),
            ((0, 2), ((0, 2),)),
            ((1, 1), ((1, 1),))))
        
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
        self.assertEqual(tuple(linque.intersect(items1, items2, lambda d: d[1])), ((0, 1), (0, 2)))
        
        items1 = (d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(tuple(linque.intersect(items1, items2)), ((0, 1), (1, 2)))
        
        items1 = (d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(tuple(linque.intersect(items1, items2, lambda d: d[1])), ((0, 1), (0, 2)))
    
    
    def test_last(self):
        """Tests whether last works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 4, 5, 6, 0)
        
        items = data
        self.assertEqual(linque.last(items, lambda d: d > 4), 6)
        
        items = (d for d in data)
        self.assertEqual(linque.last(items, lambda d: d > 4), 6)
        
        items = (d for d in data)
        self.assertEqual(linque.last(items, lambda d: d > 10, -1), -1)
    
    
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
        self.assertEqual(tuple(linque.union(items1, items2, lambda d: d[1])), ((0, 1), (0, 2), (0, 3)))
        
        items1 = (d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(tuple(linque.union(items1, items2)), ((0, 1), (0, 2), (1, 1), (1, 2), (0, 3)))
        
        items1 = (d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(tuple(linque.union(items1, items2, lambda d: d[1])), ((0, 1), (0, 2), (0, 3)))


# run test case
if __name__ == "__main__":
    unittest.main(verbosity=2)
