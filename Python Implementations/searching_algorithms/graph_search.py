from numpy import inf

from linear_structures.stack import Stack
from linear_structures.queue import Queue
from non_linear_structures.graph import Graph
from non_linear_structures.heap import Heap


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
        for neighbour, _ in neighbour_names:
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

    @staticmethod
    def breadth_first_search(
        graph: Graph, 
        vertex_name: str,
        explored_vertices: list[str],
        frontier: Queue
    ) -> None:
        """Performs Breadth First Search from a given start vertex in the Graph
        and provides the traversal path that encompasses the Graph."""

        # If Current Vertex not explored then updating the explored states
        if vertex_name not in explored_vertices:
            explored_vertices.append(vertex_name)
        # If Current Vertex already explored than continue with Frontier
        else:
            if not frontier.is_empty():
                next_vertex = frontier.dequeue().value
                GraphSearch.breadth_first_search(
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
        for neighbour, _ in neighbour_names:
            if neighbour not in explored_vertices:
                frontier.enqueue(value=neighbour)

        # Base Case: When all nodes are explored and no new neighbours are left
        if frontier.is_empty():
            return
        # Recursive Case: Continue Exploration until the Frontier is exhausted
        else:
            # Top most vertex as the next node to explore
            next_vertex = frontier.dequeue().value
            GraphSearch.breadth_first_search(
                graph=graph,
                vertex_name=next_vertex,
                explored_vertices=explored_vertices,
                frontier=frontier
            )

    @staticmethod
    def dijkstra_search(
        graph: Graph, 
        source_vertex: str, 
        explored_vertices: list[str], 
        frontier: Heap[tuple[str, int, str]],
    ) -> list[tuple[str, tuple[float, str]]]:
        """Performs Dijkstra's Algorithm on the given graph to indentify the
        shortest path to all the nodes from a input source_vertex."""

        # Checking the existence of the vertex
        if source_vertex not in graph.vertex_map:
            raise ValueError(f"The {source_vertex} does not exist in the provide graph.")
        
        # Shortest Paths Dictionary
        shortest_path_digest: dict[str, tuple[float, str]] = {
            v_name:(inf, "")
            for v_name, _ in graph.vertex_map.items()
        }

        # Inserting the first vertex into the Heap
        frontier.insert(new_value=(source_vertex, 0, "source"), key=1)
        
        # Performing the Iterative Search
        GraphSearch._dijkstra_search_helper(
            graph=graph,
            explored_vertices=explored_vertices,
            frontier=frontier,
            shortest_paths_digest=shortest_path_digest
        )

        # Final Shortest Paths
        shortest_paths = list(shortest_path_digest.items())
        return shortest_paths

    @staticmethod    
    def _dijkstra_search_helper(
            graph: Graph,
            explored_vertices: list[str],
            frontier: Heap[tuple[str, int, str]],
            shortest_paths_digest:dict[str, tuple[float, str]]
        ) -> dict[str, tuple[float, str]]:
        """Helper function the performs the iterative search for the shortest path to 
        all vertices from the source vertex provided in the dijkstra_search method."""

        # Loop until all the cheapest paths have been explored
        while frontier.peek() is not None: 

            # Extracting the current root
            vertex = frontier.extract(key=1)

            # If the current vertex was not explored append and get neighbours for exploration
            if vertex[0] not in explored_vertices:
                explored_vertices.append(vertex[0])
            else:
                continue

            # Accessing the components of the current vertex
            v_name, v_cost, v_pred = vertex
            
            # Finding all the neighbours from the corresponding node
            neighbour_cost_map = graph.get_neighbours(vertex_name=v_name)
            for n_name, n_cost in neighbour_cost_map:
                actual_cost = v_cost + n_cost
                # If the actual cost for a neighbour is lesser than existing cost queue for exploration
                if actual_cost <= shortest_paths_digest[n_name][0]:
                    frontier.insert(new_value=(n_name, actual_cost, v_name), key=1)

            # Extracting the next cheapest path
            if v_cost < shortest_paths_digest[v_name][0]:
                shortest_paths_digest[v_name] = (v_cost, v_pred)

        return shortest_paths_digest

    @staticmethod
    def bellman_ford_search(
            graph: Graph,
            source_vertex: str
        ) -> list[tuple[str, tuple[float, str]]]:
        """Performs the Bellman-Ford Algorithm on the given graph to indentify the
        shortest path to all the nodes from a input source_vertex and recognises 
        the presence of any negative cycles in the graph."""

        # Intial Shortest Paths Dictionary
        shortest_path_digest: dict[str, tuple[float, str]] = {
            v_name:(inf, "")
            for v_name, _ in graph.vertex_map.items()
        }

        # Setting the distance to intial vertex to 0
        shortest_path_digest[source_vertex] = (0, "source")

        # Accessing all the weighted edges in the graph
        weighted_edges = graph.get_graph_edges()

        # Iterating for a total of V-1 time for relaxation + 1 time for -ve cycle detection
        n_iterations = graph.no_of_vertices
        updated_cost = False
        for i in range(n_iterations):
            # Flag to track relaxations in an iteration of the edges
            updated_cost = False

            # Relaxing the shortest path to each vertex by iterating through all the edges
            for weighted_edge in weighted_edges:

                # Source, Destination and Cost for a respective edge
                s_vertex, d_vertex, d_cost = weighted_edge
                
                # Cost to get to Source
                s_cost = shortest_path_digest[s_vertex][0]

                # Actual Cost from Source
                actual_cost = s_cost + d_cost

                # If the source vertex was not explored yet and has cost infinity no point in updating
                if actual_cost == inf:
                    continue
                # Relaxing the Cost to Destination if a cheaper path was found
                elif actual_cost < shortest_path_digest[d_vertex][0]:
                    shortest_path_digest[d_vertex] = (actual_cost, s_vertex)
                    updated_cost = True
            
            # Early Exit from the Loop if all the shortest path have already been found in less than V-1 iterations
            if not updated_cost:
                break

        # Checking of negative cycles in the Vth Iteration
        if updated_cost:
            print("There is a Negative Cycle present in the given Graph")
        # Status if no negative cycles were found
        else:
            print("There was no Negative Cycle present in the given Graph")

        # Final Shortest Paths
        shortest_paths = list(shortest_path_digest.items())
        return shortest_paths
