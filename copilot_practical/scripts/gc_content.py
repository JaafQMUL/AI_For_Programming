"""Print GC content percentages for records in a FASTA file."""

import argparse
import warnings


def print_gc_content(path, min_gc=None):
    """Read FASTA records and print each non-empty record's GC content."""
    header = None
    sequence = []

    def report_record():
        if header is None:
            return
        bases = "".join(sequence)
        if not bases:
            warnings.warn(f"Skipping empty sequence for {header}", UserWarning)
            return
        gc_percentage = sum(base.upper() in "GC" for base in bases) / len(bases) * 100
        if min_gc is None or gc_percentage > min_gc:
            print(f"{header} {gc_percentage:.2f}%")

    with open(path) as fasta_file:
        for line in fasta_file:
            line = line.strip()
            if line.startswith(">"):
                report_record()
                header = line
                sequence = []
            elif header is not None:
                sequence.append(line)

    report_record()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fasta", help="path to the FASTA file")
    parser.add_argument(
        "--min-gc", type=float, help="print only records above this GC percentage"
    )
    args = parser.parse_args()
    print_gc_content(args.fasta, args.min_gc)
