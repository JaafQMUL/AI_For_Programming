# reverse_complement.py
# Reads a single-line DNA sequence from a FASTA file and prints its
# reverse complement.

COMPLEMENT = {"A": "T", "T": "A", "C": "G", "G": "C"}

def read_fasta_sequence(path):
    """Return the sequence (str) from a single-record FASTA file."""
    with open(path) as f:
        lines = f.readlines()
    return "".join(lines[1:]).replace("\n", "")

def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    try:
        return "".join(COMPLEMENT[base] for base in reversed(seq))
    except KeyError as error:
        raise ValueError(
            f"Invalid DNA base {error.args[0]!r}; sequence must contain only A, T, C, and G."
        ) from error

if __name__ == "__main__":
    import sys
    seq = read_fasta_sequence(sys.argv[1])
    print(reverse_complement(seq))
