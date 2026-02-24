from non_linear_structures.hash_structure import Hash

import random


def main() -> None:

    # Dream Cars for fun as values 🙃
    values = [
        "Porsche 911 GT3RS", "Nissan R35 GTR", "La Ferrari Aperta",
        "Mazda RX7", "Toyota GR GT3", "Lexus LFA", "Koenigsegg Gemera",
        "Ford GT40", "McLaren Senna", "Toyota GR Yaris", "Ford Focus", "BMW M4"
    ]

    # Hash Structure: Direct Chaining
    first_hash = Hash(collision_resolution_technique="Direct Chaining")

    print("Inserting 15 elements into the Hash Structure")
    for i in range(15):
        char = chr(65 + i)
        value = values[random.randint(0, len(values) - 1)]
        print(f"Inserting: {char, value}")
        first_hash.insert(key=char, value=value)

    print("\n\nHash Structure after Insertion")
    print(first_hash)

    # Accessing Keys
    keys = [chr(65 + i) for i in range(10)]
    print("\n\nAccessing Keys from the Hash Structure")
    for key in keys:
        print(f"{key}: {first_hash[key]}")


if __name__ == "__main__":
    main()