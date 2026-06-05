def apply_mask(collection: list, mask: list):
    """Applica la maschera mask a collection, restituendone i valori selezionati."""
    # versione 1 (stampa e basta)
    # for i in range(len(collection)):
    #     if mask[i]:
    #         print(collection[i])

    # versione 2 (li ritorna)
    return [element for element, mask_filter in zip(collection, mask) if mask_filter]

    # versione 3 (li ritorna)
    return [collection[i] for i in range(len(collection)) if mask[i]]

def apply_negated_mask(collection: list, mask: list):
    """Applica la maschera mask a collection, restituendone i valori *non* selezionati."""
    return [element for element, mask_filter in zip(collection, mask) if mask_filter]

def sum_mask(collection: list, mask: list) -> float:
    """Somma tutti i valori selezionati dalla maschera."""
    return sum(apply_mask(collection, mask))

print(apply_mask(
    ["A", "B", "C", "D"],
    [True, False, True, False]
))
