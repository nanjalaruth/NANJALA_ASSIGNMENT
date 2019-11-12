dna = 'GACGATATGAAAAAAAAAACGACGAAAAATGAATA'
def getkmers(dna,k):
    step = 0
    dna_list = []
    while step <= len(dna)-k:
        dna_list.append(dna[step:step+k])
        step = step +1
        
    for i, dna in enumerate(dna_list):
        if dna =='ATA':
            print(dna,i)
            
    return dna_list
    
getkmers(dna,3)