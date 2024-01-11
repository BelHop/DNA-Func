# DNA-Func
A python app that carries out essentials DNA functions
----
This was made as a study aid for Biology it:
- Replicates DNA
- Transcribes DNA to RNA
- Translates RNA to Amino acids
- And can unzip a DNA helix

----
## Special stuff!

This cli reads DNA and RNA in in special syntax:
- DNA is read in .dna files
- RNA is read in .rna files
- Amino acids can be read in normal text files and have no special syntax

Dna looks like this: `[a-g-t-c-g-a-t-t-c]`
- The `[ ]` denote the beginning and end of a DNA strand
- The `-` denotes the movement to the right of the current base and can be thought of as a vertical connection
- Because DNA can have two helix there's special syntax for that:
    -  `{ }` denote the beginning and end of a **Double helix**
    -  `+` denote the connection of two bases at the same level and can be though of as a parallel/horizontal connection

RNA looks like this: `(u-a-g-c-g-a-c-u-u)`
- The `( )` denote the beginning and end of an RNA strand (not DNA)
- The `-` mean the same thing as DNA
