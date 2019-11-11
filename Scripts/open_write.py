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