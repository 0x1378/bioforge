from exceptions import InvalidSequenceError , DataFileError
from pathlib import Path

class DNA_Sequence:
    valid_dna_sequence = ["A","T","C","G"]

    def __init__(self, sequence_id, description, sequence):
        self.sequence_id = sequence_id
        self.description = description
        self.sequence = sequence.upper().strip()
        self.validate()

    def validate(self):
        if self.sequence == None:
            raise InvalidSequenceError(f"empty dna in {self.sequence_id}")
        if not(set(self.sequence) <= set(self.valid_dna_sequence)):
            invalid_dna = ", ".join(set(self.sequence) - set(self.valid_dna_sequence))
            raise InvalidSequenceError(f"invalid dna in {self.sequence_id}: {invalid_dna}")
        
    def complement(self):
        dict_complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        dna_complement = ""
        for nb in self.sequence:
            dna_complement += dict_complement[nb]
        return dna_complement
    
    def reverse_complement(self):
        dna_reverse_complement = (self.complement())[::-1]
        return dna_reverse_complement
    
    def dna_to_rna(self):
        return self.sequence.replace("T","U")
    
    def gc_content(self):
        g_count = 0
        c_count = 0
        dna_len = len(self.sequence)
        for nb in self.sequence:
            if nb == "G":
                g_count+=1
            elif nb == "C":
                c_count+=1
        return ((g_count+c_count)/dna_len)*100


class DataDirLoad:
    @staticmethod
    def load_codon_table(ct_path):
        ct_full_path = Path.cwd() / ct_path 
        if not ct_full_path.is_file():
            raise DataFileError(f"wrong codon_table directory: {ct_full_path} ")
        codon_table = {}
        with open(ct_full_path, "r", encoding="utf-8") as ct:
            for line_num, line in enumerate(ct, 1):
                line = line.strip()
                if line=="" or line.startswith("#"):
                    continue
                parts = line.split()
                if len(parts) != 2:
                    raise DataFileError(f"error linr {line_num}: {line}")
                codon_table[parts[0].upper()] = parts[1].upper()
        return codon_table

    @staticmethod
    def load_amino_weights(aw_path):
        aw_full_path = Path.cwd() / aw_path 
        if not aw_full_path.is_file():
            raise DataFileError(f"wrong amino_weights directory: {aw_full_path} ")
        amino_weights = {}
        with open(aw_full_path, "r", encoding="utf-8") as aw:
            for line_num, line in enumerate(aw, 1):
                line = line.strip()
                if line=="" or line.startswith("#"):
                    continue
                parts = line.split()
                if len(parts) != 2:
                    raise DataFileError(f"error line {line_num}: {line}")
                amino_weights[parts[0].upper()] = parts[1].upper()
        return amino_weights

# a = DNA_Sequence("poo011"," ATGGGGCGGAC  ")
# print(a.sequence)
# try:
#     a.validate()
#     print(a.complement())
#     print(a.reverse_complement())
#     print(a.dna_to_rna())
#     print(a.gc_content())
# except Exception as e:
#     print(e)

# b = DataDirLoad()
# print(b.load_codon_table("data/codon_table.txt"))
# print(b.load_amino_weights("data/amino_weights.txt"))