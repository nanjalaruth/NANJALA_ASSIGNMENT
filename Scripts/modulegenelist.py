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

def writeGenelist(clean_gene_list):
    with open('../Data/gene_file.txt','w')as gene_file:
        for gene in clean_gene_list:
            gene_file.writelines(gene+'\n')
            
print("Genes have been written successfully")

writeGenelist(clean_gene_list)

#!/home/nanje/miniconda3/bin/python
import modulegenelist
('../Data/humchr.txt','r')
('../Data/gene_file.txt','w')