from numpy import copy, inf, ndarray

from non_linear_structures.graph import Graph


class UnionFind:
    """This class implements a Disjoint Set Datastructure aka UnionFind
    that helps with detecting cycles or loops in graphs."""

    # Standard Methods
    def __init__(self, graph: Graph, adj_matrix: ndarray, mst_digest: dict[str, float]) -> None:
        
        # Current Vertex Map and Inverse Map providing the state of the graph
        self.vertex_map = graph.vertex_map
        self.inv_map = graph.vertex_inverse_map

        # Used for backtracking parents based on the updates made after each edge
        self.parents = list(self.vertex_map.values())

        # Used to distinguish between x, y in edge for parent
        self.ranks = [1 for _ in range(graph.no_of_vertices)]

        # Adjacency Matrix to update the weights of MST
        self.adj_matrix = adj_matrix

        # MST digest
        self.mst_digest = mst_digest

    def __str__(self) -> str:
        """Provides a string representation for an instance of the structure."""
        
        repr_str = (
            f"\nAdjacency Matrix post Kruskal's Algorithm:\n{self.adj_matrix}"
            f"\nFinal Minimum Spanning Tree:\n{
                "\n".join([str(item) for item in self.mst_digest.items()])
            }"
        )
        return repr_str
    
    def make_union(self, v1: str, v2: str, cost: float) -> None:
        """Performs a union operation for a pair of vertices by providing priority 
        to the vertex with higher rank, which is the vertex that has greater contribution
        in the MST."""

        # Finding the parents of the given vertices forming the edge
        p_a = self.find(vertex=v1)
        p_b = self.find(vertex=v2)

        # Indexing the Vertices
        v1_idx = self.vertex_map[v1]
        v2_idx = self.vertex_map[v2]

        # If True: No cycle is being formed and Viz.
        if p_a != p_b:
            if p_a > p_b:
                self.parents[p_b] = p_a
                self.adj_matrix[v2_idx, v1_idx] = cost
                
            elif p_a < p_b:
                self.parents[p_a] = p_b
                self.adj_matrix[v1_idx, v2_idx] = cost
            # If both parents have equal contribution preferance to Left Operand
            else:
                self.parents[p_b] = p_a
                self.ranks[p_a] += 1
                self.adj_matrix[v2_idx, v1_idx] = cost
            
            self.mst_digest[v1] = cost
            self.mst_digest[v2] = cost

    def find(self, vertex: str) -> int:
        """Peforms the find set operation to find the parent of a given vertex."""
        
        # Checking the existence of the nodes
        if vertex not in self.vertex_map:
            raise ValueError(f"The identifier {vertex} was not found")

        """
        By Default: 
        Every Vertex is its own parent (self.parents) however, find alters this list to 
        provide priority to a vertex between x, y for any edge as parent. This helps detecting
        loops making the Kruskal Edge-based approach of an MST work.

        Thus Provisional Index: Is the original index parent -> parent map as in default.
        However Actual Index: Is the current parent for any given vertex provided by the path tracing
        taking place when inducting each edge into the MST to check for cycles.
        """
        provisional_idx = self.vertex_map[vertex]
        actual_idx = self.parents[provisional_idx]
        
        # If True: The vertex is no longer the parent of itself and is playing in role in the MST
        # If False: Base Case reached where Parent Idx (provisional) and Actual Idx are same
        if provisional_idx != actual_idx:
            # Recursive Case: Backtracking to the Original Parent Vertex
            self.parents[actual_idx] = self.find(vertex=self.inv_map[actual_idx])
        
        return self.parents[actual_idx]
