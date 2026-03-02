import numpy as np

from linear_structures.stack import Stack
from non_linear_structures.graph import Graph


class GraphSearch:
    """This class provides the semantic structure that houses key helper 
    functions that are useful in Graph Traversal."""

    @staticmethod
    def depth_first_search(
        graph: Graph, 
        vertex_name: str,
        explored_vertices: list[str],
        frontier: Stack
    ) -> None:
        """Performs Depth First Search from a given start vertex in the Graph
        and provides the traversal path that encompasses the Graph."""

        # If Current Vertex not explored then updating the explored states
        if vertex_name not in explored_vertices:
            explored_vertices.append(vertex_name)
        # If Current Vertex already explored than continue with Frontier
        else:
            if not frontier.is_empty():
                next_vertex = frontier.pop().value
                GraphSearch.depth_first_search(
                    graph=graph,
                    vertex_name=next_vertex,
                    explored_vertices=explored_vertices,
                    frontier=frontier
                )
            
            # Quick return without addition loops of readding neighbours
            return

        # Getting the neighbours for the node
        neighbour_names = graph.get_neighbours(vertex_name=vertex_name)

        # Adding the Neighbours into the Stack based on Explored Vertices state
        for neighbour in neighbour_names:
            if neighbour not in explored_vertices:
                frontier.push(value=neighbour)

        # Base Case: When all nodes are explored and no new neighbours are left
        if frontier.is_empty():
            return
        # Recursive Case: Continue Exploration until the Frontier is exhausted
        else:
            # Top most vertex as the next node to explore
            next_vertex = frontier.pop().value
            GraphSearch.depth_first_search(
                graph=graph,
                vertex_name=next_vertex,
                explored_vertices=explored_vertices,
                frontier=frontier
            )
