def print_by_index(collection_a, collection_b):
    """Stampa tutti i caratteri che appaiono in posizione i-esima per le due collezioni date. Assunta uguale lunghezza."""
    length = len(collection_a)
    for i in range(length):
        print(f"In posizione {i}:\n\t{collection_a[i]}\n\t{collection_b[i]}")

def print_most_frequent_by_index(collections):
    """Stampa tutti i caratteri che appaiono in posizione i-esima per le collezioni date. Assunta uguale lunghezza."""
    collection_length = len(collections[0])
    for position in range(collection_length):
        counts = dict()
        highest_frequency = 0  # frequenza dell'elemento piu' frequente trovato
        most_frequent_element = None
        # itero su tutte le collezioni, calcolo la frequenza di ogni elemento
        for collection in collections:
            # se ho gia' trovato l'elemento, devo aumentarne la frequenza
            if collection[position] in counts:
                counts[collection[position]] += 1
            # se non l'avevo gia' trovato, devo settare la frequenza a 1
            else:
                counts[collection[position]] = 1

            # se ho trovato un elemento con frequenza maggiore di quella massima,
            # allora aggiorno
            if counts[collection[position]] > highest_frequency:
                most_frequent_element = collection[position]
                highest_frequency = counts[collection[position]]


        print(f"In posizione {position}: {most_frequent_element}")

def are_palindrome(string_a: str, string_b: str) -> bool:
    """Le due stringhe son palindrome?"""
    lengths = (len(string_a), len(string_b))
    if lengths[0] != lengths[1]:
        return False

    for i in range(lengths[0]):
        if string_a[i] != string_b[lengths[0] - i - 1]:
            return False

    return True
