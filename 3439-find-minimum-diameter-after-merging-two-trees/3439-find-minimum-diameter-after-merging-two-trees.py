from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def calculate_diameter_and_depth(edges, n):
            # Build adjacency list
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            # BFS to find the farthest node from a starting node
            def bfs(node):
                visited = [-1] * n
                visited[node] = 0
                queue = deque([node])
                farthest_node, max_distance = node, 0
                while queue:
                    curr = queue.popleft()
                    for neighbor in graph[curr]:
                        if visited[neighbor] == -1:
                            visited[neighbor] = visited[curr] + 1
                            queue.append(neighbor)
                            if visited[neighbor] > max_distance:
                                max_distance = visited[neighbor]
                                farthest_node = neighbor
                return farthest_node, max_distance, visited

            # Find the farthest node from an arbitrary start node
            farthest_node, _, _ = bfs(0)
            # Find the diameter and depths
            opposite_node, diameter, depths = bfs(farthest_node)

            # Calculate the center(s) of the diameter
            path = []
            curr = opposite_node
            while curr != -1:
                path.append(curr)
                curr = next((neighbor for neighbor in graph[curr] if depths[neighbor] == depths[curr] - 1), -1)
            
            center = path[len(path) // 2] if len(path) % 2 == 1 else path[len(path) // 2 - 1]
            return diameter, depths, center

        n1 = len(edges1) + 1
        n2 = len(edges2) + 1

        # Get diameters, depths, and centers for both trees
        diameter1, depths1, center1 = calculate_diameter_and_depth(edges1, n1)
        diameter2, depths2, center2 = calculate_diameter_and_depth(edges2, n2)

        max_depth1 = max(depths1)
        max_depth2 = max(depths2)

        # Merging trees by connecting their centers
        # New diameter is max(diameter1, diameter2, max_depth1 + max_depth2 + 1)
        return max(diameter1, diameter2, depths1[center1] + depths2[center2] + 1)

# Example usage
edges1 = [[0, 1], [0, 2], [0, 3]]
edges2 = [[0, 1]]
sol = Solution()
print(sol.minimumDiameterAfterMerge(edges1, edges2))  # Expected: 3

edges1 = [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]
edges2 = [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]
print(sol.minimumDiameterAfterMerge(edges1, edges2))  # Expected: 5
