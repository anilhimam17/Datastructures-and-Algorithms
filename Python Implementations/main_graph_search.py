from linear_structures.stack import Stack
from linear_structures.queue import Queue
from non_linear_structures.graph import Graph
from non_linear_structures.heap import Heap
from searching_algorithms.graph_search import GraphSearch


def main() -> None:

    print("\nCreating a simple graph with 5 nodes:")
    simple_graph = Graph()
    for i in range(5):
        simple_graph.add_vertex(vertex_name=chr(i + 65))
    print(simple_graph)

    print("\nAdding Edges between the Graphs Nodes:")
    edge_pairs = [
        ("A", "B"), ("C", "A"), ("D", "A"),
        ("B", "E"), ("E", "D"), ("D", "C")
    ]
    for v1, v2 in edge_pairs:
        simple_graph.add_edge(vertex_1=v1, vertex_2=v2)
    print(simple_graph)

    print("\nViewing the Nearest Neighbours of all the vertices:")
    for vertex in simple_graph.vertex_map.keys():
        print(simple_graph.get_neighbours(vertex_name=vertex))

    # Initialising the Graph Search Object
    graph_search = GraphSearch()
    
    # Depth First Search
    print("\nPeforming Depth First Search on the Graph from all the existing nodes:")
    for node in simple_graph.vertex_map.keys():
        explored_vertices = []
        frontier = Stack()
        
        graph_search.depth_first_search(
            graph=simple_graph,
            vertex_name=node,
            explored_vertices=explored_vertices,
            frontier=frontier
        )
        print(f"DFS from {node} as start:\n{explored_vertices}")

    print("\nViewing the Nearest Neighbours of all the vertices:")
    for vertex in simple_graph.vertex_map.keys():
        print(simple_graph.get_neighbours(vertex_name=vertex))

    # Breadth First Search
    print("\nPeforming Breadth First Search on the Graph from all the existing nodes:")
    for node in simple_graph.vertex_map.keys():
        explored_vertices = []
        frontier = Queue()
        
        graph_search.breadth_first_search(
            graph=simple_graph,
            vertex_name=node,
            explored_vertices=explored_vertices,
            frontier=frontier
        )
        print(f"BFS from {node} as start:\n{explored_vertices}")

    # Creating a Directed Graph for the Single Source Shortest Path Problem
    directed_graph = Graph(graph_type="directed")
    print("\nInserting 8 Vertices into the Directed Graph")
    for i in range(8):
        directed_graph.add_vertex(vertex_name=chr(i + 65))
    print(directed_graph)

    # Inserting the Weighted Edges
    edge_cost_pairs = [
        ("A", "B", 6), ("A", "C", 10), ("A", "D", 9),
        ("B", "D", 5), ("B", "E", 16), ("B", "F", 13),
        ("C", "D", 6), ("C", "H", 5), ("C", "G", 21),
        ("D", "F", 8),
        ("E", "G", 10),
        ("F", "E", 4), ("F", "G", 12),
        ("H", "F", 2), ("H", "G", 14)
    ]
    print("\nInserting all the weighted edges into the Directed Graph")
    for v1, v2, w in edge_cost_pairs:
        directed_graph.add_edge(vertex_1=v1, vertex_2=v2, edge_weight=w)
    print(directed_graph)

    # Setting the Parameters for the SSSP
    source_node = "A"
    explored_vertices = []
    frontier = Heap(heap_size=directed_graph.no_of_vertices ** 2)
    
    # Dijkstra's Search
    print(f"\nApplying Dijkstra's Algorithm to find the shortest path to all nodes from Source: {source_node}")
    shortest_paths = graph_search.dijkstra_search(
        graph=directed_graph,
        source_vertex=source_node,
        explored_vertices=explored_vertices,
        frontier=frontier
    )

    # Resulting Shortest Paths
    print("Shortest Paths:")
    for n_name, (n_cost, n_pred) in shortest_paths:
        print(f"\nNode: {n_name}\nPredecessor: {n_pred} | Cost: {n_cost}")

    # Viewing all the weighted edges in the Graph
    print("\nWeighted Edges in the Graph")
    weighted_edges = directed_graph.get_graph_edges()
    for edge in weighted_edges:
        print(edge)

    # Bellman-Ford Search with +ve weights
    print(f"\nApplying the Bellman-Ford Algorithm to find the shortest path to all nodes from Source: {source_node}")
    shortest_paths = graph_search.bellman_ford_search(
        graph=directed_graph,
        source_vertex=source_node
    )

    # Resulting Shortest Paths
    print("\nShortest Paths:")
    for n_name, (n_cost, n_pred) in shortest_paths:
        print(f"\nNode: {n_name}\nPredecessor: {n_pred} | Cost: {n_cost}")

    # Creating a Directed Negative Graph for the Single Source Shortest Path Problem
    directed_neg_graph = Graph(graph_type="directed")
    print("\nInserting 5 Vertices into the Directed Negative Graph")
    for i in range(5):
        directed_neg_graph.add_vertex(vertex_name=chr(i + 65))
    print(directed_neg_graph)

    # Inserting the Weighted Edges
    edge_cost_pairs = [
        ("A", "C", 6), ("A", "D", -6),
        ("B", "A", 3),
        ("C", "D", 1),
        ("D", "B", 1),
        ("E", "D", 2), ("E", "B", 4)
    ]
    print("\nInserting all the weighted edges into the Directed Negative Graph")
    for v1, v2, w in edge_cost_pairs:
        directed_neg_graph.add_edge(vertex_1=v1, vertex_2=v2, edge_weight=w)
    print(directed_neg_graph)

    # Setting the Parameters for the SSSP
    source_node = "E"

    # Viewing all the weighted edges in the Graph
    print("\nWeighted Edges in the Negative Graph")
    weighted_edges = directed_neg_graph.get_graph_edges()
    for edge in weighted_edges:
        print(edge)

    # Bellman-Ford Search with -ve weights
    print(f"\nApplying the Bellman-Ford Algorithm to find the shortest path to all nodes from Source (Negative Graph): {source_node}")
    shortest_paths = graph_search.bellman_ford_search(
        graph=directed_neg_graph,
        source_vertex=source_node
    )

    # Resulting Shortest Paths
    print("\nShortest Paths (Negative Graph):")
    for n_name, (n_cost, n_pred) in shortest_paths:
        print(f"\nNode: {n_name}\nPredecessor: {n_pred} | Cost: {n_cost}")


if __name__ == "__main__":
    main()