import pandas as pd
from pathlib import Path

DATA = Path("data")

# RFQs iniciais
rfqs = pd.DataFrame({
    "id": [1,2,3,4,5],
    "cliente": ["Cliente A","Cliente B","Cliente C","Cliente A","Cliente D"],
    "valor_estimado": [15000,8000,25000,5000,12000],
    "prazo_dias": [5,2,10,1,7],
    "tipo": ["Eletrônico","Mecânico","Eletrônico","Mecânico","Eletrônico"],
    "status": ["pendente"]*5
})

analistas = pd.DataFrame({
    "id": [1,2,3],
    "nome": ["Ana","Carlos","Mariana"],
    "especialidade": ["Eletrônico","Mecânico","Eletrônico"],
    "carga_maxima": [3,3,3],
    "carga_atual": [0,0,0]
})

rfqs.to_csv(DATA / "rfqs.csv", index=False)
analistas.to_csv(DATA / "analysts.csv", index=False)
print("Dados restaurados!")