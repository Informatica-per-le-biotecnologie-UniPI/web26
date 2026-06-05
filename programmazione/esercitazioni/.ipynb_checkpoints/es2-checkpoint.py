def create_f_string(starting_codon: str, body: str , end_codon: str) -> str:
    return f"{starting_codon}{body}{end_codon}"

def create_f_string_concat(starting_codon: str, body: str , end_codon: str) -> str:
    return starting_codon + body + end_codon

def verify(starting_codon: str, body: str , end_codon: str) -> bool:
    return create_f_string(starting_codon, body, end_codon) == create_f_string_concat(starting_codon, body, end_codon)
