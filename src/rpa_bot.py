# script robô que faz a distribuição
import requests
import pandas as pd
import db

API_BASE = "http://localhost:5000"

def executar():
    # 1. Busca fila priorizada na API
    resposta = requests.get(f"{API_BASE}/rfqs")
    fila = resposta.json()

    # 2. Carrega analistas do CSV
    analistas = db.carregar_analistas()

    for rfq in fila:
        tipo = rfq['tipo']
        # Filtra analistas da especialidade que ainda têm vaga
        candidatos = analistas[(analistas['especialidade'] == tipo) & 
                               (analistas['carga_atual'] < analistas['carga_maxima'])]
        if candidatos.empty:
            print(f"Nenhum analista disponível para RFQ {rfq['id']} ({tipo})")
            continue

        # Escolhe o analista com menor carga atual
        escolhido = candidatos.sort_values('carga_atual').iloc[0]

        # Atribui via API
        payload = {"rfq_id": rfq['id'], "analista_id": int(escolhido['id'])}
        resp = requests.post(f"{API_BASE}/assign", json=payload)
        if resp.status_code == 200:
            print(f"RFQ {rfq['id']} atribuído a {escolhido['nome']}")
            # Atualiza a carga localmente para o próximo loop
            analistas.loc[analistas['id'] == escolhido['id'], 'carga_atual'] += 1
        else:
            print(f"Erro ao atribuir RFQ {rfq['id']}")

if __name__ == "__main__":
    executar()