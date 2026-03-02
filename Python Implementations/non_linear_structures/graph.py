import numpy as np


class Graph:
    """This class implements the semantic structure and properties 
    of a Generalised Graph."""

    # ==== Standard Methods ====
    def __init__(self) -> None:
        self.no_of_vertices = 0
        self.adj_matrix: np.ndarray = np.zeros(shape=(0, 0))
        self.vertex_map: dict[str, int] = {}

    def __str__(self) -> str:
        """Provides a String Representation for the Graph Structure."""

        repr_str = (
            f"\nVertex Map:\n{self.vertex_map}"
            f"\nAdjacency Matrix:\n{self.adj_matrix}"
        )
        return repr_str
        

    # ==== Member Methods ====
    def add_vertex(self, vertex_name: str) -> None:
        """Adds a new vertex to the graph by updating the Adjacency Matrix."""

        # Check if the vertex already exists in vertex map
        if vertex_name not in self.vertex_map:
            
            # Storing the Index location for the new vertex
            self.vertex_map[vertex_name] = self.no_of_vertices
            
            # Updating the Matrix for the new vertex
            self.adj_matrix = np.pad(
                array=self.adj_matrix,
                pad_width=(
                    (0, 1),  # Padding for a new row (vector) for new vertex
                    (0, 1)   # Padding for a new col for entire adj_matrix for new vertex  
                ),
                mode="constant"  # Defaults the edge values in vector to 0
            )

            # Updating the No of Vertices
            self.no_of_vertices += 1
        else:
            raise ValueError("The vertex was already in the graph")
        
    def add_edge(self, vertex_1: str, vertex_2: str) -> None:
        """Adds an edge between two existing vertices by updating the Adjacency Matrix."""
        
        # Checking for the existence of both the vertices in the graph
        for vertex in [vertex_1, vertex_2]:
            if vertex not in self.vertex_map:
                raise ValueError(
                    f"Vertex: {vertex} was not in the graph add the vertex before "
                    "adding the edge."
                )
            
        # Checking for looped edges which arent compatible yet
        if vertex_1 == vertex_2:
            raise ValueError("Adding looped edges isn't compatible in the Graph yet.")
        
        # Accessing the Indices to each vertex vector
        v1_idx = self.vertex_map[vertex_1]
        v2_idx = self.vertex_map[vertex_2]

        # Updating the edges
        self.adj_matrix[v1_idx, v2_idx] = 1
        self.adj_matrix[v2_idx, v1_idx] = 1

    def remove_edge(self, vertex_1: str, vertex_2: str) -> None:
        """Removes an edge between two existing vertices by updating the Adjacency Matrix."""
        
        # Checking for the existence of both the vertices
        for vertex in [vertex_1, vertex_2]:
            if vertex not in self.vertex_map:
                raise ValueError(
                    f"Vertex: {vertex} was not in the graph add the vertex "
                    "and an edge between the vertices before removing the edge."
                )
        
        # Checking for the removal of looped edges
        if vertex_1 == vertex_2:
            raise ValueError("Removing looped edges isn't compatible in the Graph yet.")
        
        # Accessing the keys to the vertices for updating the edge
        v1_idx = self.vertex_map[vertex_1]
        v2_idx = self.vertex_map[vertex_2]
        
        # Updating the edges
        self.adj_matrix[v1_idx, v2_idx] = 0
        self.adj_matrix[v2_idx, v1_idx] = 0

    def remove_vertex(self, vertex_name: str) -> None:
        """Removes an existing Vertex from the Graph by updating the Adjacency Matrix 
        for all its neighbours."""

        # Checking for the existence of both the vertices
        if vertex_name not in self.vertex_map:
            raise ValueError(
                f"Vertex: {vertex_name} was not in the graph add the vertex "
                "before trying to remove it."
            )
        
        # Accessing the Index for Remove Vertex
        rm_vertex_idx = self.vertex_map[vertex_name]

        # Deleting the entries in other Vertices
        self.adj_matrix = np.delete(
            arr=self.adj_matrix,
            obj=rm_vertex_idx,  # Removing all the edges
            axis=1  # Along Column Axis
        )

        # Deleting the Remove Vertex
        self.adj_matrix = np.delete(
            arr=self.adj_matrix,
            obj=rm_vertex_idx,
            axis=0  # Along Row Axis
        )

        # Updating the Vertex Map
        del self.vertex_map[vertex_name]
        self.vertex_map = {
            vertex_name: (idx if idx < rm_vertex_idx else idx - 1)
            for vertex_name, idx in self.vertex_map.items()
        }

        # Updating the no of vertices
        self.no_of_vertices -= 1
