from alive_progress import alive_bar

def readStrand(path):
    src = open(path)
    raw = src.readlines()
    raws = raw[0][raw[0].find("[")+1:raw[0].find("]")]
    arr = raws.split("-")
    return arr
    src.close()


def readStrandInput(data):
    arr = data.split("-")
    return arr


def splitHelix(path):
    src = open(path)
    raw = src.readlines()
    raws = raw[0][raw[0].find("{")+1:raw[0].find("}")]
    arr = raws.split("-")
    strand1 = []
    strand2 = []
    for i in range(len(arr)-1):
        s = arr[i].split("+")
        strand1.append(s[0])
        strand2.append(s[1])
    return strand1, strand2


def Helicase():
    val = input("Point us to a file: ")
    strand1, strand2 = splitHelix(val)
    val2 = input("Write to file (keep null to say no): ")
    if val2 == "":
        print(f"{strand1}\n{strand2}")
    else:
        file = open(f"{val}.dna", "a+")
        file.write("[")
        with alive_bar(len(strand1)) as bar:
            for i in range(len(strand1)):
                bar()
                file.write(f"{strand1[i]}-")
        file.write("]\n")
        file.write("[")
        with alive_bar(len(strand2)) as bar:
            for i in range(len(strand2)):
                bar()
                file.write(f"{strand2[i]}-")
        file.write("]\n")
        file.close()
        print("Operation completed!")
