trna='AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA'

def percentageGC(x):
    print ((x.count('G')+x.count('C'))/len(x)*100)
percentageGC(trna)

def percentageAT(x):
    print ((x.count('A')+x.count('T'))/len(x)*100)
percentageAT(trna)

aa='MNKMDLVADVAEKTDLSKAKATEVIDAVFA'
def aminoacidposition(x): 
    print("the first amino acid is %s" %x[0])
    print("the last amino acid is %s" %x[-1])
    print("the fifth amino acid is %s" %x[4])
    
aminoacidposition(aa)

dna='AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA'
def restrictionsite(x):
    print("the first restriction site 'TCCGGA' is at index %s" %x.find('TCCGGA'))
    
restrictionsite(dna)

dna = 'AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA'
def reverse_complement(seq):
    reverse= seq[::-1]
    complement = ({'A':"T",'T':"A",'C':"G",'G':"C"})
    print(''.join(complement[x]for x in seq))
reverse_complement(dna)

def AtmTransactions():
    acountbal = 50000
    choice = input("Please enter 'b' to check balance, 'd' to deposit, 'w' to withdraw or 'q' to quit: ")
    while choice != 'q':
        if choice.lower() in ('w','d','b'):
            if choice.lower() == 'b':
                print("Your balance is: %d" % acountbal)
                print("Anything else?")
                choice = input("Enter b for balance, w to withdraw, d to deposit or q to quit: ")
                print(choice.lower())
            elif choice.lower() == 'd':
                deposit = float(input("Enter amount to deposit:"))
                acountbal = acountbal + deposit
                print("Anything else?")
                choice = input("Enter b for balance, w to withdraw, d to deposit or q to quit: ")
                print(choice.lower())
            else:
                withdraw = float(input("Enter amount to withdraw: "))
                if withdraw <= acountbal:
                    print("here is your: %.2f" % withdraw)
                    acountbal = acountbal - withdraw
                    print("Anything else?")
                    choice = input("Enter b for balance, w to withdraw, d to deposit or q to quit: ")
                else:
                    print("You have insufficient funds: %.2f" % acountbal)
        else:
            print("Wrong choice!")
            choice = input("Please enter 'b' to check balance, 'd' to deposit or 'w' to withdraw: ")
            
AtmTransactions()

def y():  
    x=0
    while x<=5:
        print(x)
        x+=1       
y()

def y():
    x=0
    while x<=10:
        if x!=5:
            print(x)
        x+=1        
y()

def z():   
    for x in range (11):
        if x>3:
            print(x)
z()

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

isvalidDNA(testdna)

if isvalidDNA(testdna)==True:
    print(percentageGC(testdna))
else:
    print("Enter valid DNA sequence")
    
isvalidDNA(mydna)
        
if isvalidDNA(mydna)==True:
    print(percentageGC(mydna))
else:
    print("Enter valid DNA sequence")
    
isvalidDNA(yourdna)
        
if isvalidDNA(yourdna)==True:
    print(percentageGC(yourdna))
else:
    print("Enter valid DNA sequence")
    
def getGenelist():
    with open('../Data/humchr.txt','r')as humchr:
        tag = False
        gene_list = []
        for line in humchr:
            if line.startswith('Gene'):
                tag = True
            if tag:
                line_split = line.split()
                if len(line_split)!=0:
                    if '-'in line_split[0]:
                        continue
                    else:
                        gene_list.append(line_split[0])
        return gene_list[3:][:-2]
    
clean_gene_list = getGenelist() 

print(clean_gene_list)
    
def writeGenelist(clean_gene_list):
    with open('../Data/gene_names.txt','w')as gene_names:
        for gene in clean_gene_list:
            gene_names.writelines(gene+'\n')
            
print("Genes have been written successfully")
    
def DNA_4letters():
    dna = list('GACGATATAAAAAAAAAACGACGAAAAATA')
    print(len(set('GACGATATAAAAAAAAAACGACGAAAAATA')))
    
DNA_4letters()
           
dna ='GACGATATGAAAAAAAAAACGACGAAAAATGA'
def ATGcount(x):
    step = 0
    dna_list = []
    while step <= len(dna)-3:
        dna_list.append(dna[step:step+3])
        step = step +1 
    print(dna_list.count('ATG'))

ATGcount(dna)
          
def longestrepeatingregion():   
    dna_dict = {'A':0,'C':0, 'G':0, 'T':0}
    for dna in 'GACGATATAAAAAAAAAACGACGAAAAATA':
        dna_dict [dna] = dna_dict[dna]+1

    A_list = []
    tag = False
    As = []
    for dna in 'GACGATATAAAAAAAAAACGACGAAAAATA':
        if dna =='A':
            tag = True
            As.append(dna)
        else:
            if len(As)>1:
                A_list.append(As)
            As = []
            tag = False

    len_list = [len(x) for x in A_list]

    long_index = len_list.index(max(len_list))

    return(print("%s is the longest repeating letter, repeats %d times" % (A_list[long_index][0],len(A_list[long_index]))))
 
longestrepeatingregion()

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
            
    return(print(dna_list))
    
getkmers(dna,3)




