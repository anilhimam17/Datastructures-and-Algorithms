from non_linear_structures.hash_structure import Hash


def main() -> None:
    first_hash = Hash(collision_resolution_technique="Quadratic Probing")

    print("Inserting 25 elements into the Hash Structure")
    for i in range(25):
        char = chr(65 + i)
        print("Inserting: ", char)
        first_hash.insert(key=char, value="")

    print("\n\nHash Structure after Insertion")
    print(first_hash)


if __name__ == "__main__":
    main()