"""
Module for processing DNA/RNA sequence data.

This module provides functions for analyzing and manipulating DNA/RNA sequences.
"""

def count_nucleotides(sequence: str) -> dict:
    """
    Count the occurrences of each nucleotide in a DNA/RNA sequence.

    Args:
        sequence (str): The DNA/RNA sequence to analyze.

    Returns:
        dict: A dictionary with keys 'A', 'C', 'G', and 'T' containing their respective counts.
    """
    return {
        nucleotide: sequence.count(nucleotide)
        for nucleotide in 'ACGT'
    }

def calculate_gc_content(sequence: str) -> float:
    """
    Calculate the GC content of a DNA/RNA sequence.

    Args:
        sequence (str): The DNA/RNA sequence to analyze.

    Returns:
        float: The GC content as a percentage.
    """
    gc_count = sum(count_nucleotides(sequence).values())
    return (gc_count / len(sequence)) * 100

def calculate_gc_skew(sequence: str) -> tuple:
    """
    Calculate the GC skew of a DNA/RNA sequence.

    Args:
        sequence (str): The DNA/RNA sequence to analyze.

    Returns:
        tuple: A tuple containing the G and C counts.
    """
    g_count = sum(1 for nucleotide in sequence if nucleotide in 'G')
    c_count = sum(1 for nucleotide in sequence if nucleotide in 'C')
    return (g_count - c_count) / len(sequence), g_count, c_count
