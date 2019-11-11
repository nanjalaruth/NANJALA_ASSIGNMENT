dna = 'AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA'
def reverse_complement(seq):
    reverse= seq[::-1]
    complement = ({'A':"T",'T':"A",'C':"G",'G':"C"})
    return ''.join(complement[x]for x in seq)

reverse_complement(dna)