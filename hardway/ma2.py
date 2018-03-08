# 1.5.5
import math 
d = 0.25
H = 2.0
V = math. pi * pow(d/2, 2) * H

# 2.2.2
#insulin [Homo sapiens]GI : 386828
# extracted 51 amino acids of A + B chain 
insulin = "GIVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKT"
for amino_acid in "ACDEFGHIKLMNPQRSTVWY":
    number = insulin.count(amino_acid)
    print(amino_acid, number)

print (insulin)

for i in range(10):
    print (i,)

import random
alphabet = "ATCG"
sequence = ""
for i in range(10):
    index = random.randint(0, 3)
    sequence = sequence + alphabet[index]
print(sequence)


seq = "PRQTEINSEQWENCE"
for i in range(len(seq) - 4):
    print (seq[i:i+5])    
	
insulin = "GIVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKT"
for i in range(len(insulin)):
    print(insulin[1:i+1])