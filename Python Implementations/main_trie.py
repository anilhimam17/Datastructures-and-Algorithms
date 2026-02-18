from non_linear_structures.trie import Trie


def main() -> None:

    first_trie = Trie()

    words = ["API", "Barca", "APIs", "Barcelona"]
    for word in words:
        print(f"Inserting {word} into the Trie")
        first_trie.insert(word)
        print(first_trie, end="\n\n")
    

# Driver
if __name__ == "__main__":
    main()