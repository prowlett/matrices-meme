"""
Generates matrices worksheet with questions such that
a b  *  e f  =  10a+e   10b+f
c d     g h     10c+g   10d+h
based on results.txt
"""

from random import randint

f = open("results.txt", "r")
results = []
for line in f:
    results.append(line.rstrip('\r\n'))
f.close()

N = 20

if len(results) > N:
    start = """\\documentclass{article}
\\usepackage{amsmath}
\\usepackage{a4wide}
\\usepackage{multicol}
\\title{Matrix multiplication practice worksheet}
\\author{Peter Rowlett}
\\date{5 August 2024}
\\begin{document}
    \\maketitle
    
    \\begin{multicols}{2}
        \\begin{enumerate}
"""
    end = """
        \\end{enumerate}
    \\end{multicols}
\\end{document}
"""
    matrix_bits = """                    {} & {}\\\\
                    {} & {}
"""

    f = open("worksheet.tex","w")
    f.write(start)

    used = []


    for i in range(0,N):
        n = randint(0,len(results)-1)
        while n in used:
            n = randint(0,len(results)-1)
        used.append(n)
        f.write("            \\item \\[\\begin{bmatrix}\n")
        elements = results[n].split(",")
        f.write(matrix_bits.format(elements[0],elements[1],elements[2],elements[3]))
        f.write("                \\end{bmatrix}\\begin{bmatrix}\n")
        f.write(matrix_bits.format(elements[4],elements[5],elements[6],elements[7]))
        f.write("                \\end{bmatrix}\\]\n")

    f.write(end)
    f.close()
