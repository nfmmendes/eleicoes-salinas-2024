import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.getcwd() + r"\Dados brutos\\")
files = [f for f in os.listdir(".") if os.path.isfile(f)]

f_out = open("../vereador.csv", "w")

for f_name in files:
    if "locais" in f_name:
        continue
    with open(f_name, "r", encoding='utf-8', errors="ignore") as file:
        start = False
        next_voto = False
        candidato = ""

        for line in file: 
            if "KINCA" in line or "BENONI" in line or "ANDERSON" in line:
                break
            values = line.split(' ')
            if len(values) > 1 and values[0].isnumeric():
                candidato = ' '.join(values[1:])

            if next_voto == True:
                voto = int(line)
                next_voto = False
                f_out.write(f"{f_name[:-4]};{candidato[:-1]};{voto}\n")

            if "Votação" in line:
                next_voto = True
                continue

