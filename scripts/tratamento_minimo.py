import pandas as pd
import numpy as np
import os

os.makedirs("dados_tratados", exist_ok=True)

# Leitura forçando tudo como string primeiro (CRUCIAL)
df = pd.read_csv(
    "dados_brutos/enem_2019.csv",
    sep=",",
    encoding="utf-8",
    dtype=str
)

# Seleção mínima
df = df[
    [
        "nota_ch",
        "nota_ct",
        "nota_lc",
        "nota_mt",
        "nota_redacao",
        "sexo",
        "tipo_ens_med",
        "estado"
    ]
]

# Função segura para conversão numérica
def converter_nota(col):
    col = col.str.replace(",", ".", regex=False)
    col = pd.to_numeric(col, errors="coerce")
    return col

# Converter notas corretamente
colunas_notas = [
    "nota_ch",
    "nota_ct",
    "nota_lc",
    "nota_mt",
    "nota_redacao"
]

for col in colunas_notas:
    df[col] = converter_nota(df[col])

# Remover valores absurdos (nota ENEM válida: 0 a 1000)
for col in colunas_notas:
    df.loc[(df[col] < 0) | (df[col] > 1000), col] = np.nan

# Remover linhas inválidas
df = df.dropna(subset=colunas_notas)

# Exportação limpa
df.to_csv(
    "dados_tratados/enem_fato.csv",
    index=False,
    encoding="utf-8"
)

print("✅ Tabela fato limpa e confiável gerada.")
