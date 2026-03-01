from non_linear_structures.graph import Graph


# The Main Function
def main() -> None:
    
    # Intiailising the first instance of the Graph
    first_graph = Graph()

    # Adding 5 vertices
    print("\nAdding 5 Independent Vertices into the Graph")
    for i in range(5):
        first_graph.add_vertex(vertex_name=chr(i + 65))

    # Adding Edges between the given Vertex Pairs
    edge_pairs = [
        ("A", "B"), ("B", "E"), ("E", "D"), 
        ("D", "C"), ("C", "A"), ("D", "A")
    ]
    print("\nAdding edges between the Vertices in the Graph")
    for v1, v2 in edge_pairs:
        first_graph.add_edge(vertex_1=v1, vertex_2=v2)

    print(f"\nThe Adjacency Matrix of the Graph:\n{first_graph.adj_matrix}")

    # Removing Edge between the given Vertex Pairs
    remove_pairs = [("A", "D")]
    print("\nRemoving edges between the Vertices in the Graph")
    for v1, v2 in remove_pairs:
        first_graph.remove_edge(vertex_1=v1, vertex_2=v2)

    print(f"\nThe Adjacency Matrix of the Graph:\n{first_graph.adj_matrix}")

    # Removing a Vertex from the Graph
    print("Removing Vertex C from the Graph")
    first_graph.remove_vertex(vertex_name="C")

    print(f"\nThe Adjacency Matrix of the Graph:\n{first_graph.adj_matrix}")


if __name__ == "__main__":
    main()