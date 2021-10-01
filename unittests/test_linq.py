#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import unittest
import linque


class TestCase(unittest.TestCase):
    """Test case for Linq class."""
    
    
    def test_aggregate(self):
        """Tests whether count works correctly."""
        
        data = (97, 103, 103, 114, 101, 103, 97, 116, 101)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.aggregate(lambda r, d: r+chr(d), ''), 'aggregate')
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.aggregate(lambda r, d: r+chr(d), ''), 'aggregate')
    
    
    def test_all(self):
        """Tests whether all works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertTrue(linq.all(lambda d: d > -5))
        self.assertFalse(linq.all(lambda d: d > 5))
        
        linq = linque.Linque(d for d in data)
        self.assertTrue(linq.all(lambda d: d > -5))
        
        linq = linque.Linque(d for d in data)
        self.assertFalse(linq.all(lambda d: d > 5))
    
    
    def test_any(self):
        """Tests whether any works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertTrue(linq.any())
        self.assertTrue(linq.any(lambda d: d > 5))
        
        linq = linque.Linque(d for d in data)
        self.assertTrue(linq.any())
        
        linq = linque.Linque(d for d in data)
        self.assertTrue(linq.any(lambda d: d > 5))
    
    
    def test_argmax(self):
        """Tests whether argmax works correctly."""
        
        data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.argmax(lambda d: d[1]), (4, 40))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.argmax(lambda d: d[1]), (4, 40))
    
    
    def test_argmin(self):
        """Tests whether argmin works correctly."""
        
        data = ((0, 0), (1, -10), (2, -20), (3, -30), (4, -40))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.argmin(lambda d: d[1]), (4, -40))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.argmin(lambda d: d[1]), (4, -40))
    
    
    def test_concat(self):
        """Tests whether concat works correctly."""
        
        data1 = (0, 1, 2, 3, 4)
        data2 = (5, 6, 7, 8, 9)
        
        linq = linque.Linque(data1)
        items2 = data2
        self.assertEqual(linq.concat(items2).tuple(), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
        
        linq = linque.Linque(d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(linq.concat(items2).tuple(), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    
    
    def test_contains(self):
        """Tests whether contains works correctly."""
        
        data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
        
        linq = linque.Linque(data)
        self.assertTrue(linq.contains((1, 10)))
        self.assertFalse(linq.contains((1, -10)))
        
        linq = linque.Linque(d for d in data)
        self.assertTrue(linq.contains((1, 10)))
        
        linq = linque.Linque(d for d in data)
        self.assertFalse(linq.contains((1, -10)))
    
    
    def test_chunk(self):
        """Tests whether chunk works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.chunk(3).select(lambda d: d.tuple()).tuple(), ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9,)))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.chunk(3).select(lambda d: d.tuple()).tuple(), ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9,)))
    
    
    def test_count(self):
        """Tests whether count works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.count(), 10)
        self.assertEqual(linq.count(lambda d: d > 4), 5)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.count(), 10)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.count(lambda d: d > 4), 5)
    
    
    def test_dict(self):
        """Tests whether dict works correctly."""
        
        data = ((0, 1, 'a'), (0, 2, 'b'), (0, 3, 'c'))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.dict(lambda d: d[1]), {
            1: (0, 1, 'a'),
            2: (0, 2, 'b'),
            3: (0, 3, 'c')})
        
        self.assertEqual(linq.dict(lambda d: d[1], lambda d: d[2]), {
            1: 'a',
            2: 'b',
            3: 'c'})
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.dict(lambda d: d[1]), {
            1: (0, 1, 'a'),
            2: (0, 2, 'b'),
            3: (0, 3, 'c')})
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.dict(lambda d: d[1], lambda d: d[2]), {
            1: 'a',
            2: 'b',
            3: 'c'})
    
    
    def test_distinct(self):
        """Tests whether distinct works correctly."""
        
        data = ((0, 1), (0, 1), (0, 2), (1, 1), (1, 2))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.distinct().tuple(), ((0, 1), (0, 2), (1, 1), (1, 2)))
        self.assertEqual(linq.distinct(lambda d: d[1]).tuple(), ((0, 1), (0, 2)))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.distinct().tuple(), ((0, 1), (0, 2), (1, 1), (1, 2)))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.distinct(lambda d: d[1]).tuple(), ((0, 1), (0, 2)))
    
    
    def test_each(self):
        """Tests whether each works correctly."""
        
        def action(d):
            d[1] = str(d[0])
        
        data = ([0, None], [1, None], [2, None], [3, None], [4, None])
        
        linq = linque.Linque(data)
        self.assertEqual(linq.each(action).tuple(), ([0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4']))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.each(action).tuple(), ([0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4']))
    
    
    def test_enumerate(self):
        """Tests whether enumerate works correctly."""
        
        data = (5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.enumerate().tuple(), ((0, 5), (1, 6), (2, 7), (3, 8), (4, 9)))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.enumerate().tuple(), ((0, 5), (1, 6), (2, 7), (3, 8), (4, 9)))
    
    
    def test_evaluate(self):
        """Tests whether evaluate works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.take(4).tuple(), (0, 1, 2, 3))
        self.assertEqual(linq.take(4).tuple(), (4, 5, 6, 7))
        
        linq = linque.Linque(d for d in data).evaluate()
        self.assertEqual(linq.take(4).tuple(), (0, 1, 2, 3))
        self.assertEqual(linq.take(4).tuple(), (0, 1, 2, 3))
    
    
    def test_exclude(self):
        """Tests whether exclude works correctly."""
        
        data1 = ((0, 1), (0, 1), (0, 2), (1, 2), (0, 3), (0, 4))
        data2 = ((0, 1), (1, 2), (1, 2), (1, 3))
        
        linq = linque.Linque(data1)
        items2 = data2
        self.assertEqual(linq.exclude(items2).tuple(), ((0, 2), (0, 3), (0, 4)))
        self.assertEqual(linq.exclude(items2, lambda d: d[1]).tuple(), ((0, 4), ))
        
        linq = linque.Linque(d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(linq.exclude(items2).tuple(), ((0, 2), (0, 3), (0, 4)))
        
        linq = linque.Linque(d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(linq.exclude(items2, lambda d: d[1]).tuple(), ((0, 4), ))
    
    
    def test_first(self):
        """Tests whether first works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.first(lambda d: d > 4), 5)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.first(lambda d: d > 4), 5)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.first(lambda d: d > 10, -1), -1)
    
    
    def test_flatten(self):
        """Tests whether flatten works correctly."""
        
        data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.flatten(lambda d: d).tuple(), (0, 0, 1, 10, 2, 20, 3, 30, 4, 40))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.flatten(lambda d: d).tuple(), (0, 0, 1, 10, 2, 20, 3, 30, 4, 40))
    
    
    def test_group(self):
        """Tests whether group works correctly."""
        
        data = ((0, 1), (0, 1), (0, 2), (1, 1))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.group().dict(lambda d: d[0], lambda d: d[1].tuple()), {
            (0, 1): ((0, 1), (0, 1)),
            (0, 2): ((0, 2),),
            (1, 1): ((1, 1),)})
        
        self.assertEqual(linq.group(lambda d: d[1]).dict(lambda d: d[0], lambda d: d[1].tuple()), {
            1: ((0, 1), (0, 1), (1, 1)),
            2: ((0, 2),)})
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.group().dict(lambda d: d[0], lambda d: d[1].tuple()), {
            (0, 1): ((0, 1), (0, 1)),
            (0, 2): ((0, 2),),
            (1, 1): ((1, 1),)})
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.group(lambda d: d[1]).dict(lambda d: d[0], lambda d: d[1].tuple()), {
            1: ((0, 1), (0, 1), (1, 1)),
            2: ((0, 2),)})
    
    
    def test_intersect(self):
        """Tests whether intersect works correctly."""
        
        data1 = ((0, 1), (0, 1), (0, 2), (1, 2))
        data2 = ((0, 1), (1, 2), (1, 2), (0, 3))
        
        linq = linque.Linque(data1)
        items2 = data2
        self.assertEqual(linq.intersect(items2).tuple(), ((0, 1), (1, 2)))
        self.assertEqual(linq.intersect(items2, lambda d: d[1]).tuple(), ((0, 1), (0, 2)))
        
        linq = linque.Linque(d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(linq.intersect(items2).tuple(), ((0, 1), (1, 2)))
        
        linq = linque.Linque(d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(linq.intersect(items2, lambda d: d[1]).tuple(), ((0, 1), (0, 2)))
    
    
    def test_last(self):
        """Tests whether last works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 4, 5, 6, 0)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.last(lambda d: d > 4), 6)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.last(lambda d: d > 4), 6)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.last(lambda d: d > 10, -1), -1)
    
    
    def test_list(self):
        """Tests whether list works correctly."""
        
        data = (0, 1, 2, 3, 4, 0, 1)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.list(), list(data))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.list(), list(data))
    
    
    def test_max(self):
        """Tests whether max works correctly."""
        
        data = (0, 1, 2, 3, 4)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.max(), 4)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.max(), 4)
        
        data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.max(lambda d: d[1]), 40)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.max(lambda d: d[1]), 40)
    
    
    def test_mean(self):
        """Tests whether mean works correctly."""
        
        data = (0, 1, 2, 3, 4)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.mean(), 2)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.mean(), 2)
        
        data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.mean(lambda d: d[1]), 20)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.mean(lambda d: d[1]), 20)
    
    
    def test_median(self):
        """Tests whether median works correctly."""
        
        data = (0, 1, 2, 3, 4)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.median(), 2)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.median(), 2)
        
        data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.median(lambda d: d[1]), 20)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.median(lambda d: d[1]), 20)
    
    
    def test_min(self):
        """Tests whether min works correctly."""
        
        data = (0, -1, -2, -3, -4)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.min(), -4)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.min(), -4)
        
        data = ((0, 0), (1, -10), (2, -20), (3, -30), (4, -40))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.min(lambda d: d[1]), -40)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.min(lambda d: d[1]), -40)
    
    
    def test_reverse(self):
        """Tests whether reverse works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.reverse().tuple(), (9, 8, 7, 6, 5, 4, 3, 2, 1, 0))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.reverse().tuple(), (9, 8, 7, 6, 5, 4, 3, 2, 1, 0))
    
    
    def test_select(self):
        """Tests whether select works correctly."""
        
        data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.select(lambda d: d[1]).tuple(), (0, 10, 20, 30, 40))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.select(lambda d: d[1]).tuple(), (0, 10, 20, 30, 40))
    
    
    def test_set(self):
        """Tests whether set works correctly."""
        
        data = (0, 1, 2, 3, 4, 0, 1)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.set(), set(data))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.set(), set(data))
    
    
    def test_skip(self):
        """Tests whether skip works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.skip(4).tuple(), (4, 5, 6, 7, 8, 9))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.skip(4).tuple(), (4, 5, 6, 7, 8, 9))
    
    
    def test_skip_while(self):
        """Tests whether skip_while works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 4, 3, 2, 2, 0)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.skip_while(lambda d: d < 4).tuple(), (4, 5, 4, 3, 2, 2, 0))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.skip_while(lambda d: d < 4).tuple(), (4, 5, 4, 3, 2, 2, 0))
    
    
    def test_sort(self):
        """Tests whether sort works correctly."""
        
        data = (8, 0, 2, 3, 5, 1, 6, 7, 4, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.sort().tuple(), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.sort().tuple(), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    
    
    def test_sort_desc(self):
        """Tests whether sort_desc works correctly."""
        
        data = (8, 0, 2, 3, 5, 1, 6, 7, 4, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.sort_desc().tuple(), (9, 8, 7, 6, 5, 4, 3, 2, 1, 0))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.sort_desc().tuple(), (9, 8, 7, 6, 5, 4, 3, 2, 1, 0))
    
    
    def test_sum(self):
        """Tests whether sum works correctly."""
        
        data = (0, 1, 2, 3, 4)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.sum(), 10)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.sum(), 10)
        
        data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.sum(lambda d: d[1]), 100)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.sum(lambda d: d[1]), 100)
    
    
    def test_take(self):
        """Tests whether take works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.take(4).tuple(), (0, 1, 2, 3))
        self.assertEqual(linq.take(4).tuple(), (0, 1, 2, 3))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.take(4).tuple(), (0, 1, 2, 3))
        self.assertEqual(linq.take(4).tuple(), (4, 5, 6, 7))
    
    
    def test_take_while(self):
        """Tests whether take_while works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.take_while(lambda d: d < 4).tuple(), (0, 1, 2, 3))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.take_while(lambda d: d < 4).tuple(), (0, 1, 2, 3))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.take_while(lambda d: d < 20).tuple(), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    
    
    def test_tuple(self):
        """Tests whether tuple works correctly."""
        
        data = [0, 1, 2, 3, 4, 0, 1]
        
        linq = linque.Linque(data)
        self.assertEqual(linq.tuple(), tuple(data))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.tuple(), tuple(data))
    
    
    def test_union(self):
        """Tests whether union works correctly."""
        
        data1 = ((0, 1), (0, 1), (0, 2))
        data2 = ((1, 1), (1, 2), (1, 2), (0, 3))
        
        linq = linque.Linque(data1)
        items2 = data2
        self.assertEqual(linq.union(items2).tuple(), ((0, 1), (0, 2), (1, 1), (1, 2), (0, 3)))
        self.assertEqual(linq.union(items2, lambda d: d[1]).tuple(), ((0, 1), (0, 2), (0, 3)))
        
        linq = linque.Linque(d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(linq.union(items2).tuple(), ((0, 1), (0, 2), (1, 1), (1, 2), (0, 3)))
        
        linq = linque.Linque(d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(linq.union(items2, lambda d: d[1]).tuple(), ((0, 1), (0, 2), (0, 3)))
    
    
    def test_where(self):
        """Tests whether where works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.where(lambda d: d % 2).tuple(), (1, 3, 5, 7, 9))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.where(lambda d: d % 2).tuple(), (1, 3, 5, 7, 9))
    
    
    def test_zip(self):
        """Tests whether zip works correctly."""
        
        data1 = (0, 1, 2, 3, 4)
        data2 = ('a', 'b', 'c')
        
        linq = linque.Linque(data1)
        items2 = data2
        self.assertEqual(linq.zip(items2).tuple(), ((0, 'a'), (1, 'b'), (2, 'c')))
        
        linq = linque.Linque(d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(linq.zip(items2).tuple(), ((0, 'a'), (1, 'b'), (2, 'c')))


# run test case
if __name__ == "__main__":
    unittest.main(verbosity=2)
