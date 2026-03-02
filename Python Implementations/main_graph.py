from non_linear_structures.graph import Graph


# The Main Function
def main() -> None:
    
    # Intiailising the first instance of the Graph
    first_graph = Graph()

    # Adding 5 vertices
    print("\nAdding 5 Independent Vertices into the Graph")
    for i in range(5):
        first_graph.add_vertex(vertex_name=chr(i + 65))

    print("\nThe Initial Adjacency Matrix without any of the edges added:")
    print(first_graph)

    # Adding Edges between the given Vertex Pairs
    edge_pairs = [
        ("A", "B"), ("B", "E"), ("E", "D"), 
        ("D", "C"), ("C", "A"), ("D", "A"), ("A", "A")
    ]
    print("\nAdding edges between the Vertices in the Graph")
    for v1, v2 in edge_pairs:
        try:
            first_graph.add_edge(vertex_1=v1, vertex_2=v2)
        except ValueError:
            print("Encountered a looped edge insertion and ignored")
            continue
    print(first_graph)

    # Removing Edge between the given Vertex Pairs
    remove_pairs = [("A", "D"), ("A", "A")]
    print("\nRemoving edges between the Vertices in the Graph")
    for v1, v2 in remove_pairs:
        try:
            first_graph.remove_edge(vertex_1=v1, vertex_2=v2)
        except ValueError:
            print("Encounted a looped edge removal and ignored")
            continue
    print(first_graph)

    # Removing a Vertex from the Graph
    print("\nRemoving Vertex C from the Graph")
    first_graph.remove_vertex(vertex_name="C")
    print(first_graph)


if __name__ == "__main__":
    main()