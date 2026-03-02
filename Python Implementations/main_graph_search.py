from linear_structures.stack import Stack
from non_linear_structures.graph import Graph
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

    print("\nPeforming Depth First Search on the Graph from all the existing nodes:")
    graph_search = GraphSearch()
    for node in simple_graph.vertex_map.keys():
        explored_vertices = []
        frontier = Stack()
        
        # DFS
        graph_search.depth_first_search(
            graph=simple_graph,
            vertex_name=node,
            explored_vertices=explored_vertices,
            frontier=frontier
        )

        print(f"DFS from {node} as start:\n{explored_vertices}")


if __name__ == "__main__":
    main()