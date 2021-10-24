"""
You are given two integer arrays, source and target, both of length n.
You are also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi] indicates
that you are allowed to swap the elements at index ai and index bi (0-indexed) of array source.
Note that you can swap elements at a specific pair of indices multiple times and in any order.

The Hamming distance of two arrays of the same length, source and target,
is the number of positions where the elements are different.
Formally, it is the number of indices i for 0 <= i <= n-1 where source[i] != target[i] (0-indexed).

Return the minimum Hamming distance of source and target after performing any amount
of swap operations on array source.
"""
import collections
from typing import List


class UnionFind:
    def __init__(self, n):
        self.roots = [i for i in range(n)]

    def find(self, v):
        if self.roots[v] != v:
            self.roots[v] = self.find(self.roots[v])

        return self.roots[v]

    def union(self, u, v):
        self.roots[self.find(u)] = self.find(v)


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        uf = UnionFind(len(source))
        for idx1, idx2 in allowedSwaps:
            uf.union(idx1, idx2)

        m = collections.defaultdict(set)
        for i in range(len(source)):
            m[uf.find(i)].add(i)

        res = 0
        for indices in m.values():
            freq = {}
            for i in indices:
                freq[source[i]] = freq.get(source[i], 0) + 1
                freq[target[i]] = freq.get(target[i], 0) - 1
            res += sum(val for val in freq.values() if val > 0)

        return res


print(Solution().minimumHammingDistance(source=[1, 2, 3, 4], target=[2, 1, 4, 5], allowedSwaps=[[0, 1], [2, 3]]))
