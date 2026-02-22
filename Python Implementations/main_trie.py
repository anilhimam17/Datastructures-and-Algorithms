from non_linear_structures.trie import Trie
from non_linear_structures.trie_node import TrieNode


def main() -> None:

    print("Viewing a TrieNode")
    first_trie_node = TrieNode()
    print(first_trie_node, end="\n\n")

    first_trie = Trie()
    print("Viewing the Empty Trie")
    print(first_trie, end="\n\n")

    words = [
        "API", "Barca", "APIs", "Barcelona", 
        "A", "Ba", "Apart", "Apartment"
    ]
    print("Inseting 4 Words into the Trie")
    for word in words:
        first_trie.insert(word)
        print(f"Inserted {word} into the Trie")
        print(first_trie, end="\n\n")

    search_words = [*words[:3], "", "Anil", *words[-2:]]
    print("Searching for words in the Trie")
    for word in search_words:
        print(f"Searching for {word}: ", first_trie.search(word))

    seeds = ["A", "B", "Bar", "An"]
    print("\n\nChecking autocomplete strings")
    for seed in seeds:
        strings = first_trie.starts_with(seed)
        if strings:
            print(f"Autocomplete Strings for {seed}:\n", strings, end="\n\n")
        else:
            print("The seed was not in the Trie\n\n")

    print(first_trie)
    print("\n\nDeleting words from the Trie")
    delete_words = ["A", "Ba", "Barcelona", "Apartment", "Anil"]
    for word in delete_words:
        print(f"Deleting {word}")
        res = first_trie.delete(word)
        if res:
            print(first_trie)
        else:
            print("The delete word was not found in the Trie")


# Driver
if __name__ == "__main__":
    main()