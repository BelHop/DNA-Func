from alive_progress import alive_bar
import sys
from read import readStrand, readStrandInput

strand = ["a", "g", "t", "a", "g", "c", "c", "a", "g", "t", "c", "a"]
strandC = []


def init():
    val = input("Would to use our demo data: (y/n) ")
    if val == "y":
        replication(strand)
    elif val == "n":
        val2 = input("Read .dna file (keep null to say no): ")
        if val2 == "":
            data = input("DNA input: ")
            dna = readStrandInput(data)
            replication(dna)
        else:
            dna = readStrand(val2)
            replication(dna)
    else:
        print("unknown input, quitting...")
        sys.exit()


def replication(DNA):
    with alive_bar(len(DNA)) as bar:
        for base in DNA:
            bar()
            match base:
                case "a":
                    strandC.append("t")
                case "t":
                    strandC.append("a")
                case "g":
                    strandC.append("c")
                case "c":
                    strandC.append("g")
    print(f"Original strand:   {DNA}")
    print(f"Replicated strand: {strandC}")
    val = input("Write to .dna file (keep null to say no): ")
    if val == "":
        print("quitting...")
    else:
        val1 = input("Write as strands independently?: (y/n) ")
        if val1 == "y":
            file = open(f"{val}.dna", "a+")
            file.write("[")
            with alive_bar(len(DNA)) as bar:
                for i in range(len(DNA)):
                    bar()
                    file.write(f"{DNA[i]}-")
            file.write("]\n")
            file.write("[")
            with alive_bar(len(DNA)) as bar:
                for i in range(len(strandC)):
                    bar()
                    file.write(f"{strandC[i]}-")
            file.write("]\n")
            file.close()
            print("Operation completed!")
        elif val1 == "n":
            helix = []
            file = open(f"{val}.dna", "a+")
            with alive_bar(len(DNA)) as bar:
                for i in range(len(DNA)):
                    bar()
                    helix.append(f"{DNA[i]}+{strandC[i]}")
            file.write("{")
            with alive_bar(len(DNA)) as bar:
                for i in range(len(helix)):
                    bar()
                    file.write(f"{helix[i]}-")
            file.write("}")
            file.close()
            print("Operation completed!")
