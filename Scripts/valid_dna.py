mydna = "CAGTGATGATGACGAT"
yourdna = "ACGATCGAGACGTAGTA"
testdna = "ATFRACGATTGHAHYAK"

def percentageGC(x):
    return (x.count('G')+x.count('C'))/len(x)*100

def isvalidDNA(s):
    valid_bases=list('ACTG')
    valid = True
    for base in s:
        if base in valid_bases:
            continue
        else:
            valid = False
            print("There is an invalid base %s at position %d" % (base,s.find(base)))     
    return(valid)

    if isvalidDNA(testdna)==True:
        print(percentageGC(testdna))
    else:
        print("Enter valid DNA sequence")