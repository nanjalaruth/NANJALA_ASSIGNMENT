dna='AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA'
def restrictionsite(x):
    print("the first restriction site 'TCCGGA' is at index %s" %x.find('TCCGGA'))
    
restrictionsite(dna)