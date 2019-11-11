#! /home/nanje/miniconda3/bin/python
# #! /usr/bin/env python


trna='AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA'
def percentageGC(x):
    return (x.count('G')+x.count('C'))/len(x)*100
def percentageAT(x):
    return (x.count('A')+x.count('T'))/len(x)*100

percentageGC(trna)

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
    return ''.join(complement[x]for x in seq)

reverse_complement(dna)


def AtmTransactions():
    acountbal = 50000
    choice = input("Please enter 'b' to check balance, 'd' to deposit or 'w' to withdraw: ")
    while choice != 'q':
        if choice.lower() in ('w','d','b'):
            if choice.lower() == 'b':
                print("Your balance is: %d" % acountbal)
                print("Anything else?")
                choice = input("Enter b for balance, w to withdraw, d to deposit or q to quit: ")
                print(choice.lower())
            elif choice.lower() == 'd':
                deposit = float(input("Enter amount to deposit:"))
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

def x():
    x=0
    while x<10:
        if x!=5:
            print(x)
        x+=1
        
x()

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

percentageGC(testdna)

percentageGC(mydna)

percentageGC(yourdna)


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

clean_gene_list

def writeGenelist(clean_gene_list):
    with open('../Data/gene_names.txt','w')as gene_names:
        for gene in clean_gene_list:
            gene_names.writelines(gene+'\n')
    print('Genes have been written successfully')
    
writeGenelist('../Data/gene_names.txt')


import sys

gene_file = sys.argv[1]
out_file = sys.argv[2]

def getGenelist():
    with open(gene_file,'r')as humchr:
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
    
def writeGenelist(clean_gene_list):
    with open(out_file,'w')as gene_names:
        for gene in clean_gene_list:
            gene_names.writelines(gene+'\n')
    print('Genes have been written successfully')
    
writeGenelist('../Data/gene_names.txt')
