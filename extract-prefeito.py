import os

os.chdir(os.getcwd() + r"\Dados brutos\\")
files = [f for f in os.listdir('.') if os.path.isfile(f)]

for f_name in files:
    if "locais" in f_name:
        continue
    with open(f_name, "r", encoding='utf-8', errors="ignore") as file:
        start = False
        next_voto = False
        candidates_found = False
        candidato = ""

        for line in file: 
            if "KINCA" in line or "BENONI" in line or "ANDERSON" in line:
                candidato = line
                start = True
                candidates_found = True
            if start == False: 
                continue

            if next_voto == True:
                voto = int(line)
                next_voto = False
                start = False
                print(f"{f_name[:-4]};{candidato[:-1]};{voto}")

            if "Votação" in line:
                next_voto = True
                continue

        if candidates_found == False:
            print("Error", f_name)
            break


