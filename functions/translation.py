import sys
# from enum import Enum
from alive_progress import alive_bar
from read import readStrand, readStrandInput

mRNA = ["a", "g", "u", "a", "g", "c", "c", "a", "g", "u", "c", "a"]
amino = []


# class Acids(Enum):
Phe = "uuu", "uuc", "Phe"
Leu = "uua", "uug", "cuu", "cuc", "cua", "cug", "Leu"
Ile = "auu", "auc", "aua", "Ile"
Met = "aug", "Met"
Val = "guu", "guc", "gua", "gug", "Val"
Ser = "ucu", "ucc", "uca", "ucg", "agu", "agc", "Ser"
Pro = "ccu", "ccc", "cca", "ccg", "Pro"
Thr = "acu", "acc", "acu", "acg", "Thr"
Ala = "gcu", "gcc", "gca", "gcg", "Ala"
Tyr = "uau", "uac", "Tyr"
Stop = "uaa", "uag", "uga", "Stop"
His = "cau", "cac", "His"
Gin = "caa", "cag", "Gin"
Asn = "aau", "aac", "Asn"
Lys = "aaa", "aag", "Lys"
Asp = "gau", "gac", "Asp"
Glu = "gaa", "gag", "Gsp"
Cys = "ugu", "ugc", "Cys"
Trp = "ugg", "Trp"
Arg = "cgu", "cgc", "cga", "cgg", "aga", "agg", "Arg"
Gly = "ggu", "ggc", "gga", "ggg", "Gly"

Acids = [Phe, Leu, Ile, Met, Val, Ser, Pro, Thr, Ala, Tyr, Stop,
         His, Gin, Asn, Lys, Asp, Glu, Cys, Trp, Arg, Gly]


def tinit():
    val = input("Would to use our demo data: (y/n) ")
    if val == "y":
        translate(mRNA)
    elif val == "n":
        val2 = input("Should we point to a file: (y/n) ")
        if val2 == "y":
            path = input("Point us to a file: ")
            dna = readStrand(path)
            translate(dna)
        elif val == "n":
            data = input("DNA input: ")
            dna = readStrandInput(data)
            translate(dna)
        else:
            print("unknown input, quitting...")
            sys.exit()
    else:
        print("unknown input, quitting...")
        sys.exit()


def translate(rna):
    length = len(rna)/3
    codons = []
    with alive_bar(int(length)) as bar:
        i = 0
        while i < len(rna):
            bar()
            codons.append(f"{rna[i]}{rna[i + 1]}{rna[i + 2]}")
            i += 3
    with alive_bar(len(codons)) as bar:
        for codon in range(len(codons)):
            bar()
            for acid in Acids:
                for i in range(len(acid)):
                    if codons[codon] == acid[i]:
                        amino.append(acid[len(acid)-1])
    val = input("Write to text file (keep null to say no): ")
    if val == "":
        print("quitting...")
    else:
        file = open(val, "a+")
        with alive_bar(len(amino)) as bar:
            for i in range(len(amino)):
                bar()
                file.write(f"{amino[i]}, ")
        file.close()
        print("Operation completed!")
