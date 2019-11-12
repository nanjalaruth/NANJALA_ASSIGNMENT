trna='AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA'

def percentageGC(x):
    return (x.count('G')+x.count('C'))/len(x)*100
percentageGC(trna)

def percentageAT(x):
    return (x.count('A')+x.count('T'))/len(x)*100
percentageAT(trna)