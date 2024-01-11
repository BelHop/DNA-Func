from alive_progress import alive_bar
import sys
from read import readStrand, readStrandInput

strand = ["a", "g", "t", "a", "g", "c", "c", "a", "g", "t", "c", "a"]
mRNA = []


def Tinit():
    val = input("Would to use our demo data: (y/n) ")
    if val == "y":
        transcription(strand)
    elif val == "n":
        val2 = input("Should we point to a file: (y/n) ")
        if val2 == "y":
            path = input("Point us to a file: ")
            dna = readStrand(path)
            transcription(dna)
        elif val == "n":
            data = input("DNA input: ")
            dna = readStrandInput(data)
            transcription(dna)
        else:
            print("unknown input, quitting...")
            sys.exit()
    else:
        print("unknown input, quitting...")
        sys.exit()


def transcription(DNA):
    with alive_bar(len(DNA)) as bar:
        for base in DNA:
            bar()
            match base:
                case "a":
                    mRNA.append("u")
                case "t":
                    mRNA.append("a")
                case "g":
                    mRNA.append("c")
                case "c":
                    mRNA.append("g")
    print(f"DNA strand:   {DNA}")
    print(f"mRNA strand:  {mRNA}")
    val = input("Write to .rna file (keep null to say no): ")
    if val == "":
        print("quitting...")
    else:
        file = open(f"{val}.rna", "a+")
        file.write("(")
        for i in range(len(mRNA)):
            bar()
            file.write(f"{mRNA[i]}-")
        file.write(")")
        file.close()
        print("Operation completed!")
