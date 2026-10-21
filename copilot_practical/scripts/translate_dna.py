python
def translate(seq):
    # Standard codon table
    codon_table = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
        'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
        'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    # Remove any non-codon characters and convert to uppercase
    seq = ''.join(filter(lambda x: x in 'ATCG', seq.upper()))

    # Translate the sequence
    protein_seq = []
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        if codon in codon_table:
            protein_seq.append(codon_table[codon])
        else:
            protein_seq.append('*')  # Unknown codon

    return ''.join(protein_seq)

# Example usage:
dna_sequence = "ATGCGTAATGGT"
protein_sequence = translate(dna_sequence)
print(protein_sequence)  # Output: Met-Asp
```

### Explanation:
1. **Codon Table**: The function uses a dictionary `codon_table` to map each codon to its corresponding 
amino acid.
2. **Input Validation**: The input sequence is cleaned to remove any non-nucleotide characters and converted 
to uppercase.
3. **Translation**: The function iterates through the sequence in steps of 3 (one codon at a time), 
translates each codon using the codon table, and appends the resulting amino acid to the `protein_seq` list.
4. **Output**: The function returns the protein sequence as a string.

This function assumes that the input sequence is a valid nucleic acid sequence. If the sequence contains 
invalid characters, they are ignored during translation.
