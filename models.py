from exceptions import InvalidSequenceError

class DNA_Sequence:
    valid_dna_sequence = ["A","T","C","G"]

    def __init__(self, sequence_id, sequence):
        self.sequence_id = sequence_id
        self.sequence = sequence.upper().strip()
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

