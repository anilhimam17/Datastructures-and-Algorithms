from collections import OrderedDict


class Graph:
    """This class implements the semantic structure and properties 
    of a Generalised Graph."""

    # ==== Standard Methods ====
    def __init__(self) -> None:
        self.no_of_vertices = 0
        self.adj_matrix: OrderedDict[str, list[int]] = OrderedDict()

    # ==== Member Methods ====
    def add_vertex(self, vertex_name: str) -> None:
        """Adds a new vertex to the graph by updating the Adjacency Matrix."""

        # Check if the vertex already exists
        if vertex_name not in self.adj_matrix:
            self.no_of_vertices += 1
            self.adj_matrix[vertex_name] = []
            self.adj_matrix[vertex_name].extend([0 for _ in range(self.no_of_vertices)])
        else:
            raise ValueError("The vertex was already in the graph")
        
        # Extending the list for subsequent vertices
        for other_vertex in self.adj_matrix.keys():
            if other_vertex != vertex_name:
                vertex_edges = self.adj_matrix[other_vertex]
                vertex_edges.extend([0 for _ in range(self.no_of_vertices - len(vertex_edges))])
        
    def add_edge(self, vertex_1: str, vertex_2: str) -> None:
        """Adds an edge between two existing vertices by updating the Adjacency Matrix."""
        
        # Checking for the existence of both the vertices
        for vertex in [vertex_1, vertex_2]:
            if vertex not in self.adj_matrix:
                raise ValueError(
                    f"Vertex: {vertex} was not in the graph add the vertex before "
                    "adding the edge."
                )
        
        v1_key = list(self.adj_matrix.keys()).index(vertex_1)
        v2_key = list(self.adj_matrix.keys()).index(vertex_2)

        # Updating the edges
        self.adj_matrix[vertex_1][v2_key] = 1
        self.adj_matrix[vertex_2][v1_key] = 1

    def remove_edge(self, vertex_1: str, vertex_2: str) -> None:
        """Removes an edge between two existing vertices by updating the Adjacency Matrix."""
        
        # Checking for the existence of both the vertices
        for vertex in [vertex_1, vertex_2]:
            if vertex not in self.adj_matrix:
                raise ValueError(
                    f"Vertex: {vertex} was not in the graph add the vertex "
                    "and an edge between the vertices before removing the edge."
                )

        # Accessing the keys to the vertices for updating the edge
        v1_key = list(self.adj_matrix.keys()).index(vertex_1)
        v2_key = list(self.adj_matrix.keys()).index(vertex_2)
        
        # Updating the edges
        self.adj_matrix[vertex_1][v2_key] = 0
        self.adj_matrix[vertex_2][v1_key] = 0

    def remove_vertex(self, vertex_name: str) -> None:
        """Removes an existing Vertex from the Graph by updating the Adjacency Matrix 
        for all its neighbours."""

        # Checking for the existence of both the vertices
        if vertex_name not in self.adj_matrix:
            raise ValueError(
                f"Vertex: {vertex_name} was not in the graph add the vertex "
                "and an edge between the vertices before removing the edge."
            )
        
        vertex_keys = list(self.adj_matrix.keys())

        # Accessing the existing edges for the Delete Vertex
        vertex_edges = self.adj_matrix[vertex_name]
        vertex_idx = vertex_keys.index(vertex_name)

        # Traversing through all the live edges between delete node and neighbours to set to 0
        for neighbour_idx, _ in enumerate(vertex_edges):
            
            # Removing the edge from the delete vertex
            self.adj_matrix[vertex_name][neighbour_idx] = 0
            
            # Removing the edge from the neighbouring vertex
            neighbour_name = vertex_keys[neighbour_idx]
            self.adj_matrix[neighbour_name].pop(vertex_idx)

        # Removing the Vertex from the Adjacency Matrix
        self.adj_matrix.pop(vertex_name)

        # Updating the no of vertices
        self.no_of_vertices -= 1
