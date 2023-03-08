__author__ = "Keenan Manpearl"
__date__ = "2023/03/06"

def parse_query(fp):
    '''
    Parameters
    ----------
    fp : STR
        file path to query FASTA file
        query sequence must only contain the leters ATGC

    Returns
    -------
    line : STR
        query sequence parsed from FASTA file

    '''
    nucleotides = set("ATCG")
    with open(fp,"r") as file:
        lines = file.readlines()
        if len(lines) < 2:
            raise Exception("Query sequence must be a FASTA file") 
        elif len(lines) > 2:
            raise Exception("Query sequence must be a FASTA file with only one entry")
        if lines[0].startswith(">"):
            sequence = lines[1].upper().strip()
            if set(sequence) > nucleotides:
                raise Exception("Query must be a DNA sequence")
            return sequence
        else:
            raise Exception("Query sequence must be a FASTA file")
                 

def parse_reads(fp):
    '''
    Parameters
    ----------
    fp : STR
        file path to sequence reads FASTA file
        reads must only contain the leters ATGC

    Returns
    -------
    read_dict : DICT
        read_id (keys) and sequence (values)
    '''
    nucleotides = set("ATCG")
    read_dict = {}
    with open(fp, "r") as file:
        lines = file.readlines()
        if len(lines) % 2 != 0:
            raise Exception("Sequence reads must be a FASTA file")
        i = 0
        while i < len(lines):
            read_id = lines[i]
            if not read_id.startswith(">"):
                raise Exception("Sequence reads must be a FASTA file") 
            # remove > from line and any trailing whitespace 
            read_id = read_id[1:].strip()
            sequence = lines[i+1].upper().strip()
            if set(sequence) > nucleotides:
                raise Exception("Reads must be DNA sequences")
            read_dict[read_id] = sequence
            i += 2
    return(read_dict)