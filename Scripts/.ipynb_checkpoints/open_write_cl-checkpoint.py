import sys

gene_file = sys.argv[1]
out_file = sys.argv[2]

print(gene_file)
print(out_file)

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
        
def writeGenelist(clean_gene_list):
    with open('out_file','w')as gene_names:
        for gene in clean_gene_list:
            gene_names.writelines(gene+'\n')
    print('Genes have been written successfully')
    
if len(sys.argv)<3:
    print(_doc_)
else:
    
    gene_file = sys.argv
    out_file = sys.argv
    clean_gene_list = getGenelist(gene_file)
    writeGenelist(clean_gene_list,out_file)
