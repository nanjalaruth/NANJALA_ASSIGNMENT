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