import os

with open("Dados brutos/locais.txt", "r", encoding='utf-8', errors="ignore") as file:
    start = False
    next_voto = False
    candidates_found = False
    candidato = ""

    for line in file: 
        values = line.split(';')
        local = values[0]
        for sec in values[1:]:
            sec = sec.strip()
            if len(sec) == 3:
                print(f"{local};{sec}")
            else:
                print(f"{local};0{sec}")


