def find_maximum(collection: list):
    """Trova il massimo nella data lista."""
    if len(collection) == 0:
        raise ValueError("Collezione vuota!")

    maximum = collection[0]
    for element in collection[1:]:
        if element > maximum:
            maximum = element

    return maximum

def find_maximum_with_indexes(collection: list):
    """Trova il massimo nella data lista."""
    if len(collection) == 0:
        raise ValueError("Collezione vuota!")

    length = len(collection)
    maximum = collection[0]
    for i in range(length):
        if collection[i] > maximum:
            maximum = collection[i]

    return maximum

def both_in_collection(collection, element_a, element_b) -> bool:
    return element_a in collection and element_b in collection

def only_one_in_collection(collection, element_a, element_b) -> bool:
    return (element_a in collection and element_b not in collection) or ((element_a not in collection and element_b in collection))

def collection_in_collection(collection, subcollection) -> bool:
    """Verifica che tutti gli elementi della collezione subcollection siano in collection."""
    for element in subcollection:
        if element not in collection:
            return False

    return True

def hamming_similarity(collection_a: list, collection_b: list) -> int:
    """Conta il numero di elementi uguali tra le due liste date, assunte della stessa lunghezza."""
    count = 0
    for element_a, element_b in zip(collection_a, collection_b):
        if element_a == element_b:
            count += 1

    return count