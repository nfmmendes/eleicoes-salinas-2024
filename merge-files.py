import pandas as pd

df_section = pd.read_csv("locais.csv", sep=";", encoding="utf-8")
df_prefeito = pd.read_csv("prefeito.csv", sep=";", encoding="utf-16")
df_vereador = pd.read_csv("vereador.csv", sep=";", encoding="ANSI")


df_prefeito = df_section.merge(df_prefeito, on="SECAO")
df_vereador = df_section[["LOCAL", "SECAO"]].merge(df_vereador, on="SECAO")


df_prefeito.to_csv("prefeito-final.csv", sep=";", encoding="ANSI")
df_vereador.to_csv("vereador-final.csv", sep=";", encoding="ANSI")
