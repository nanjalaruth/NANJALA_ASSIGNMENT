dna = 'GACGATATGAAAAAAAAAACGACGAAAAATGA'
def ATGcount(x):
    step = 0
    dna_list = []
    while step <= len(dna)-3:
        dna_list.append(dna[step:step+3])
        step = step +1 
    return(dna_list.count('ATG'))

ATGcount(dna)