"""
LeetCode 133 - Clone Graph (Medium)
https://leetcode.com/problems/clone-graph/

Problem:
    Given a reference of a node in a connected undirected graph, return a
    deep copy (clone) of the graph. Each node contains a value and a list
    of its neighbors.

Approach:
    DFS with a hash map mapping original node -> cloned node. When we visit
    a node, create its clone, store the mapping, then recursively clone all
    its neighbors. The map also acts as our visited set, preventing infinite
    loops in cyclic graphs.

Complexity:
    Time:  O(V + E) - each node and edge examined once
    Space: O(V) - hash map and recursion stack

Example:
    Input:  adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
"""

from typing import Optional, Dict


class Node:
    def __init__(self, val: int = 0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    if node is None:
        return None

    cloned: Dict[Node, Node] = {}

    def dfs(original: Node) -> Node:
        if original in cloned:
            return cloned[original]
        copy = Node(original.val)
        cloned[original] = copy
        for nb in original.neighbors:
            copy.neighbors.append(dfs(nb))
        return copy

    return dfs(node)


if __name__ == "__main__":
    # Build: 1 - 2 - 3 - 4 - 1 (square)
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    cloned = clone_graph(n1)
    print(cloned.val, [nb.val for nb in cloned.neighbors])  # 1 [2, 4]
    print(cloned is not n1)                                 # True (deep copy)
