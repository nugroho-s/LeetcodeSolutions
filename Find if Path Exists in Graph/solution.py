# Union Find algorithm
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def find_root(node: int) -> int:
            if group[node] != node:
                group[node] = find_root(group[node])
            return group[node]

        group = list(range(n))
        for start_node, end_node in edges:
            group[find_root(start_node)] = find_root(end_node)
        print(group)
        return find_root(source) == find_root(destination)
