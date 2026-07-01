# funções para ler/salvar dados (simula banco)
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

def carregar_rfqs():
    return pd.read_csv(DATA_DIR / "rfqs.csv")

def salvar_rfqs(df):
    df.to_csv(DATA_DIR / "rfqs.csv", index=False)

def carregar_analistas():
    return pd.read_csv(DATA_DIR / "analysts.csv")

def salvar_analistas(df):
    df.to_csv(DATA_DIR / "analysts.csv", index=False)