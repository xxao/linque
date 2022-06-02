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
    
    
    def test_argsort(self):
        """Tests whether argsort works correctly."""
        
        data = (3, 1, 2)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.argsort().to_tuple(), (1, 2, 0))
        self.assertEqual(linq.argsort(True).to_tuple(), (0, 2, 1))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.argsort().to_tuple(), (1, 2, 0))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.argsort(True).to_tuple(), (0, 2, 1))
    
    
    def test_argsort_by(self):
        """Tests whether argsort_by works correctly."""
        
        data = ((2, 3), (1, 1), (3, 2))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.argsort_by(lambda d: d[1]).to_tuple(), (1, 2, 0))
        self.assertEqual(linq.argsort_by(lambda d: d[1], True).to_tuple(), (0, 2, 1))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.argsort_by(lambda d: d[1]).to_tuple(), (1, 2, 0))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.argsort_by(lambda d: d[1], True).to_tuple(), (0, 2, 1))
    
    
    def test_concat(self):
        """Tests whether concat works correctly."""
        
        data1 = (0, 1, 2, 3, 4)
        data2 = (5, 6, 7, 8, 9)
        
        linq = linque.Linque(data1)
        items2 = data2
        self.assertEqual(linq.concat(items2).to_tuple(), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
        
        linq = linque.Linque(d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(linq.concat(items2).to_tuple(), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    
    
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
    
    
    def test_contains_by(self):
        """Tests whether contains_by works correctly."""
        
        data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
        
        linq = linque.Linque(data)
        self.assertTrue(linq.contains_by(10, lambda d: d[1]))
        self.assertFalse(linq.contains_by(-10, lambda d: d[1]))
        
        linq = linque.Linque(d for d in data)
        self.assertTrue(linq.contains_by(10, lambda d: d[1]))
        
        linq = linque.Linque(d for d in data)
        self.assertFalse(linq.contains_by(-10, lambda d: d[1]))
    
    
    def test_chunk(self):
        """Tests whether chunk works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(
            linq.chunk(3).select(lambda d: d.to_tuple()).to_tuple(), ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9,)))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(
            linq.chunk(3).select(lambda d: d.to_tuple()).to_tuple(), ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9,)))
    
    
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
    
    
    def test_distinct(self):
        """Tests whether distinct works correctly."""
        
        data = ((0, 1), (0, 1), (0, 2), (1, 1), (1, 2))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.distinct().to_tuple(), ((0, 1), (0, 2), (1, 1), (1, 2)))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.distinct().to_tuple(), ((0, 1), (0, 2), (1, 1), (1, 2)))
    
    
    def test_distinct_by(self):
        """Tests whether distinct_by works correctly."""
        
        data = ((0, 1), (0, 1), (0, 2), (1, 1), (1, 2))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.distinct_by(lambda d: d[1]).to_tuple(), ((0, 1), (0, 2)))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.distinct_by(lambda d: d[1]).to_tuple(), ((0, 1), (0, 2)))
    
    
    def test_each(self):
        """Tests whether each works correctly."""
        
        def action(d):
            d[1] = str(d[0])
        
        data = ([0, None], [1, None], [2, None], [3, None], [4, None])
        
        linq = linque.Linque(data)
        self.assertEqual(linq.each(action).to_tuple(), ([0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4']))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.each(action).to_tuple(), ([0, '0'], [1, '1'], [2, '2'], [3, '3'], [4, '4']))
    
    
    def test_enumerate(self):
        """Tests whether enumerate works correctly."""
        
        data = (5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.enumerate().to_tuple(), ((0, 5), (1, 6), (2, 7), (3, 8), (4, 9)))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.enumerate().to_tuple(), ((0, 5), (1, 6), (2, 7), (3, 8), (4, 9)))
    
    
    def test_evaluate(self):
        """Tests whether evaluate works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.take(4).to_tuple(), (0, 1, 2, 3))
        self.assertEqual(linq.take(4).to_tuple(), (4, 5, 6, 7))
        
        linq = linque.Linque(d for d in data).evaluate()
        self.assertEqual(linq.take(4).to_tuple(), (0, 1, 2, 3))
        self.assertEqual(linq.take(4).to_tuple(), (0, 1, 2, 3))
    
    
    def test_exclude(self):
        """Tests whether exclude works correctly."""
        
        data1 = ((0, 1), (0, 1), (0, 2), (1, 2), (0, 3), (0, 4))
        data2 = ((0, 1), (1, 2), (1, 2), (1, 3))
        
        linq = linque.Linque(data1)
        items2 = data2
        self.assertEqual(linq.exclude(items2).to_tuple(), ((0, 2), (0, 3), (0, 4)))
        
        linq = linque.Linque(d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(linq.exclude(items2).to_tuple(), ((0, 2), (0, 3), (0, 4)))
    
    
    def test_exclude_by(self):
        """Tests whether exclude_by works correctly."""
        
        data1 = ((0, 1), (0, 1), (0, 2), (1, 2), (0, 3), (0, 4))
        data2 = ((0, 1), (1, 2), (1, 2), (1, 3))
        
        linq = linque.Linque(data1)
        items2 = data2
        self.assertEqual(linq.exclude_by(items2, lambda d: d[1]).to_tuple(), ((0, 4),))
        
        linq = linque.Linque(d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(linq.exclude_by(items2, lambda d: d[1]).to_tuple(), ((0, 4),))
    
    
    def test_first(self):
        """Tests whether first works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.first(), 0)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.first(), 0)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.first(lambda d: d > 4), 5)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.first(lambda d: d > 4), 5)
        
        linq = linque.Linque(data)
        with self.assertRaises(StopIteration):
            linq.first(lambda d: d > 10)
        
        linq = linque.Linque(d for d in data)
        with self.assertRaises(StopIteration):
            linq.first(lambda d: d > 10)
    
    
    def test_first_or_default(self):
        """Tests whether first_or_default works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.first_or_default(), 0)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.first_or_default(), 0)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.first_or_default(lambda d: d > 4), 5)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.first_or_default(lambda d: d > 4), 5)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.first_or_default(lambda d: d > 10, -1), -1)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.first_or_default(lambda d: d > 10, -1), -1)
    
    
    def test_flatten(self):
        """Tests whether flatten works correctly."""
        
        data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.flatten(lambda d: d).to_tuple(), (0, 0, 1, 10, 2, 20, 3, 30, 4, 40))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.flatten(lambda d: d).to_tuple(), (0, 0, 1, 10, 2, 20, 3, 30, 4, 40))
    
    
    def test_group(self):
        """Tests whether group works correctly."""
        
        data = ((0, 1), (0, 1), (0, 2), (1, 1))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.group().to_dict(lambda d: d[0], lambda d: d[1].to_tuple()), {
            (0, 1): ((0, 1), (0, 1)),
            (0, 2): ((0, 2),),
            (1, 1): ((1, 1),)})
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.group().to_dict(lambda d: d[0], lambda d: d[1].to_tuple()), {
            (0, 1): ((0, 1), (0, 1)),
            (0, 2): ((0, 2),),
            (1, 1): ((1, 1),)})
    
    
    def test_group_by(self):
        """Tests whether group_by works correctly."""
        
        data = ((0, 1), (0, 1), (0, 2), (1, 1))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.group_by(lambda d: d[1]).to_dict(lambda d: d[0], lambda d: d[1].to_tuple()), {
            1: ((0, 1), (0, 1), (1, 1)),
            2: ((0, 2),)})
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.group_by(lambda d: d[1]).to_dict(lambda d: d[0], lambda d: d[1].to_tuple()), {
            1: ((0, 1), (0, 1), (1, 1)),
            2: ((0, 2),)})
    
    
    def test_intersect(self):
        """Tests whether intersect works correctly."""
        
        data1 = ((0, 1), (0, 1), (0, 2), (1, 2))
        data2 = ((0, 1), (1, 2), (1, 2), (0, 3))
        
        linq = linque.Linque(data1)
        items2 = data2
        self.assertEqual(linq.intersect(items2).to_tuple(), ((0, 1), (1, 2)))
        
        linq = linque.Linque(d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(linq.intersect(items2).to_tuple(), ((0, 1), (1, 2)))
    
    
    def test_intersect_by(self):
        """Tests whether intersect_by works correctly."""
        
        data1 = ((0, 1), (0, 1), (0, 2), (1, 2))
        data2 = ((0, 1), (1, 2), (1, 2), (0, 3))
        
        linq = linque.Linque(data1)
        items2 = data2
        self.assertEqual(linq.intersect_by(items2, lambda d: d[1]).to_tuple(), ((0, 1), (0, 2)))
        
        linq = linque.Linque(d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(linq.intersect_by(items2, lambda d: d[1]).to_tuple(), ((0, 1), (0, 2)))
    
    
    def test_last(self):
        """Tests whether last works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 4, 5, 6, 0)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.last(), 0)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.last(), 0)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.last(lambda d: d > 4), 6)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.last(lambda d: d > 4), 6)
        
        linq = linque.Linque(data)
        with self.assertRaises(StopIteration):
            linq.last(lambda d: d > 10)
        
        linq = linque.Linque(d for d in data)
        with self.assertRaises(StopIteration):
            linq.last(lambda d: d > 10)
    
    
    def test_last_or_default(self):
        """Tests whether last_or_default works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 4, 5, 6, 1)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.last_or_default(), 1)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.last_or_default(), 1)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.last_or_default(lambda d: d > 4), 6)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.last_or_default(lambda d: d > 4), 6)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.last_or_default(lambda d: d > 10, -1), -1)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.last_or_default(lambda d: d > 10, -1), -1)
    
    
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
    
    
    def test_max_by(self):
        """Tests whether max_by works correctly."""
        
        data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.max_by(lambda d: d[1]), (4, 40))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.max_by(lambda d: d[1]), (4, 40))
    
    
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
    
    
    def test_min_by(self):
        """Tests whether min_by works correctly."""
        
        data = ((0, 0), (1, -10), (2, -20), (3, -30), (4, -40))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.min_by(lambda d: d[1]), (4, -40))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.min_by(lambda d: d[1]), (4, -40))
    
    
    def test_rank(self):
        """Tests whether rank works correctly."""
        
        data = (0, 2, 3, 2)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.rank('average').to_tuple(), (1, 2.5, 4, 2.5))
        self.assertEqual(linq.rank('min').to_tuple(), (1, 2, 4, 2))
        self.assertEqual(linq.rank('max').to_tuple(), (1, 3, 4, 3))
        self.assertEqual(linq.rank('dense').to_tuple(), (1, 2, 3, 2))
        self.assertEqual(linq.rank('ordinal').to_tuple(), (1, 2, 4, 3))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.rank('average').to_tuple(), (1, 2.5, 4, 2.5))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.rank('min').to_tuple(), (1, 2, 4, 2))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.rank('max').to_tuple(), (1, 3, 4, 3))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.rank('dense').to_tuple(), (1, 2, 3, 2))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.rank('ordinal').to_tuple(), (1, 2, 4, 3))
    
    
    def test_rank_by(self):
        """Tests whether rank_by works correctly."""
        
        data = ((2, 0), (3, 2), (2, 3), (0, 2))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.rank_by(lambda d: d[1], 'average').to_tuple(), (1, 2.5, 4, 2.5))
        self.assertEqual(linq.rank_by(lambda d: d[1], 'min').to_tuple(), (1, 2, 4, 2))
        self.assertEqual(linq.rank_by(lambda d: d[1], 'max').to_tuple(), (1, 3, 4, 3))
        self.assertEqual(linq.rank_by(lambda d: d[1], 'dense').to_tuple(), (1, 2, 3, 2))
        self.assertEqual(linq.rank_by(lambda d: d[1], 'ordinal').to_tuple(), (1, 2, 4, 3))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.rank_by(lambda d: d[1], 'average').to_tuple(), (1, 2.5, 4, 2.5))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.rank_by(lambda d: d[1], 'min').to_tuple(), (1, 2, 4, 2))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.rank_by(lambda d: d[1], 'max').to_tuple(), (1, 3, 4, 3))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.rank_by(lambda d: d[1], 'dense').to_tuple(), (1, 2, 3, 2))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.rank_by(lambda d: d[1], 'ordinal').to_tuple(), (1, 2, 4, 3))
    
    
    def test_reverse(self):
        """Tests whether reverse works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.reverse().to_tuple(), (9, 8, 7, 6, 5, 4, 3, 2, 1, 0))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.reverse().to_tuple(), (9, 8, 7, 6, 5, 4, 3, 2, 1, 0))
    
    
    def test_select(self):
        """Tests whether select works correctly."""
        
        data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.select(lambda d: d[1]).to_tuple(), (0, 10, 20, 30, 40))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.select(lambda d: d[1]).to_tuple(), (0, 10, 20, 30, 40))
    
    
    def test_select_many(self):
        """Tests whether select_many works correctly."""
        
        data = ((0, 0), (1, 10), (2, 20), (3, 30), (4, 40))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.select_many(lambda d: d).to_tuple(), (0, 0, 1, 10, 2, 20, 3, 30, 4, 40))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.select_many(lambda d: d).to_tuple(), (0, 0, 1, 10, 2, 20, 3, 30, 4, 40))
    
    
    def test_single(self):
        """Tests whether single works correctly."""
        
        data = (42, )
        
        linq = linque.Linque(data)
        self.assertEqual(linq.single(), 42)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.single(), 42)
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.single(lambda d: 3<d<5), 4)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.single(lambda d: 3<d<5), 4)
        
        linq = linque.Linque(data)
        with self.assertRaises(ValueError):
            linq.single()
        
        linq = linque.Linque(d for d in data)
        with self.assertRaises(ValueError):
            linq.single()
        
        linq = linque.Linque(data)
        with self.assertRaises(ValueError):
            linq.single(lambda d: d>5)
        
        linq = linque.Linque(d for d in data)
        with self.assertRaises(ValueError):
            linq.single(lambda d: d>5)
    
    
    def test_single_or_default(self):
        """Tests whether single_or_default works correctly."""
        
        data = (42, )
        
        linq = linque.Linque(data)
        self.assertEqual(linq.single_or_default(), 42)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.single_or_default(), 42)
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.single_or_default(lambda d: 3 < d < 5), 4)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.single_or_default(lambda d: d > 10, -1), -1)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.single_or_default(lambda d: 3 < d < 5), 4)
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.single_or_default(lambda d: d > 10, -1), -1)
        
        linq = linque.Linque(data)
        with self.assertRaises(ValueError):
            linq.single()
        
        linq = linque.Linque(d for d in data)
        with self.assertRaises(ValueError):
            linq.single()
        
        linq = linque.Linque(data)
        with self.assertRaises(ValueError):
            linq.single(lambda d: d > 5)
        
        linq = linque.Linque(d for d in data)
        with self.assertRaises(ValueError):
            linq.single(lambda d: d > 5)
    
    
    def test_skip(self):
        """Tests whether skip works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.skip(4).to_tuple(), (4, 5, 6, 7, 8, 9))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.skip(4).to_tuple(), (4, 5, 6, 7, 8, 9))
    
    
    def test_skip_while(self):
        """Tests whether skip_while works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 4, 3, 2, 2, 0)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.skip_while(lambda d: d < 4).to_tuple(), (4, 5, 4, 3, 2, 2, 0))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.skip_while(lambda d: d < 4).to_tuple(), (4, 5, 4, 3, 2, 2, 0))
    
    
    def test_sort(self):
        """Tests whether sort works correctly."""
        
        data = (8, 0, 2, 3, 5, 1, 6, 7, 4, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.sort().to_tuple(), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.sort().to_tuple(), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.sort(True).to_tuple(), (9, 8, 7, 6, 5, 4, 3, 2, 1, 0))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.sort(True).to_tuple(), (9, 8, 7, 6, 5, 4, 3, 2, 1, 0))
    
    
    def test_sort_by(self):
        """Tests whether sort_by works correctly."""
        
        data = ((1, 8), (2, 0), (3, 2), (4, 3), (5, 5), (6, 1), (7, 6), (8, 7), (9, 4), (0, 9))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.sort_by(lambda d: d[1]).to_tuple(), ((2, 0), (6, 1), (3, 2), (4, 3), (9, 4), (5, 5), (7, 6), (8, 7), (1, 8), (0, 9)))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.sort_by(lambda d: d[1]).to_tuple(), ((2, 0), (6, 1), (3, 2), (4, 3), (9, 4), (5, 5), (7, 6), (8, 7), (1, 8), (0, 9)))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.sort_by(lambda d: d[1], True).to_tuple(), ((0, 9), (1, 8), (8, 7), (7, 6), (5, 5), (9, 4), (4, 3), (3, 2), (6, 1), (2, 0)))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.sort_by(lambda d: d[1], True).to_tuple(), ((0, 9), (1, 8), (8, 7), (7, 6), (5, 5), (9, 4), (4, 3), (3, 2), (6, 1), (2, 0)))
    
    
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
        self.assertEqual(linq.take(4).to_tuple(), (0, 1, 2, 3))
        self.assertEqual(linq.take(4).to_tuple(), (0, 1, 2, 3))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.take(4).to_tuple(), (0, 1, 2, 3))
        self.assertEqual(linq.take(4).to_tuple(), (4, 5, 6, 7))
    
    
    def test_take_while(self):
        """Tests whether take_while works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.take_while(lambda d: d < 4).to_tuple(), (0, 1, 2, 3))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.take_while(lambda d: d < 4).to_tuple(), (0, 1, 2, 3))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.take_while(lambda d: d < 20).to_tuple(), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    
    
    def test_to_dict(self):
        """Tests whether to_dict works correctly."""
        
        data = ((0, 1, 'a'), (0, 2, 'b'), (0, 3, 'c'))
        
        linq = linque.Linque(data)
        self.assertEqual(linq.to_dict(lambda d: d[1]), {
            1: (0, 1, 'a'),
            2: (0, 2, 'b'),
            3: (0, 3, 'c')})
        
        self.assertEqual(linq.to_dict(lambda d: d[1], lambda d: d[2]), {
            1: 'a',
            2: 'b',
            3: 'c'})
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.to_dict(lambda d: d[1]), {
            1: (0, 1, 'a'),
            2: (0, 2, 'b'),
            3: (0, 3, 'c')})
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.to_dict(lambda d: d[1], lambda d: d[2]), {
            1: 'a',
            2: 'b',
            3: 'c'})
    
    
    def test_to_list(self):
        """Tests whether to_list works correctly."""
        
        data = (0, 1, 2, 3, 4, 0, 1)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.to_list(), list(data))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.to_list(), list(data))
    
    
    def test_to_set(self):
        """Tests whether to_set works correctly."""
        
        data = (0, 1, 2, 3, 4, 0, 1)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.to_set(), set(data))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.to_set(), set(data))
    
    
    def test_to_tuple(self):
        """Tests whether to_tuple works correctly."""
        
        data = [0, 1, 2, 3, 4, 0, 1]
        
        linq = linque.Linque(data)
        self.assertEqual(linq.to_tuple(), tuple(data))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.to_tuple(), tuple(data))
    
    
    def test_union(self):
        """Tests whether union works correctly."""
        
        data1 = ((0, 1), (0, 1), (0, 2))
        data2 = ((1, 1), (1, 2), (1, 2), (0, 3))
        
        linq = linque.Linque(data1)
        items2 = data2
        self.assertEqual(linq.union(items2).to_tuple(), ((0, 1), (0, 2), (1, 1), (1, 2), (0, 3)))
        
        linq = linque.Linque(d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(linq.union(items2).to_tuple(), ((0, 1), (0, 2), (1, 1), (1, 2), (0, 3)))
    
    
    def test_union_by(self):
        """Tests whether union_by works correctly."""
        
        data1 = ((0, 1), (0, 1), (0, 2))
        data2 = ((1, 1), (1, 2), (1, 2), (0, 3))
        
        linq = linque.Linque(data1)
        items2 = data2
        self.assertEqual(linq.union_by(items2, lambda d: d[1]).to_tuple(), ((0, 1), (0, 2), (0, 3)))
        
        linq = linque.Linque(d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(linq.union_by(items2, lambda d: d[1]).to_tuple(), ((0, 1), (0, 2), (0, 3)))
    
    
    def test_where(self):
        """Tests whether where works correctly."""
        
        data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        
        linq = linque.Linque(data)
        self.assertEqual(linq.where(lambda d: d % 2).to_tuple(), (1, 3, 5, 7, 9))
        
        linq = linque.Linque(d for d in data)
        self.assertEqual(linq.where(lambda d: d % 2).to_tuple(), (1, 3, 5, 7, 9))
    
    
    def test_zip(self):
        """Tests whether zip works correctly."""
        
        data1 = (0, 1, 2, 3, 4)
        data2 = ('a', 'b', 'c')
        
        linq = linque.Linque(data1)
        items2 = data2
        self.assertEqual(linq.zip(items2).to_tuple(), ((0, 'a'), (1, 'b'), (2, 'c')))
        
        linq = linque.Linque(d for d in data1)
        items2 = (d for d in data2)
        self.assertEqual(linq.zip(items2).to_tuple(), ((0, 'a'), (1, 'b'), (2, 'c')))


# run test case
if __name__ == "__main__":
    unittest.main(verbosity=2)
