def find_motifs(string: str, motif_length: int) -> list:
    """Trova i motif di lunghezza motif_length nella stringa data."""
    counts = dict()
    # come punti di partenza dei motif considero le posizioni 0, 1, ..., n - motif_length
    # perche' un motif puo' iniziare al massimo motif_length posizioni prima della fine della stringa
    for i in range(len(string) - motif_length + 1):
        motif = string[i : i + motif_length]
        if motif in counts:
            counts[motif] += 1
        else:
            counts[motif] = 1

    return sorted(counts.items(), key=lambda x: x[1], reverse=True)
