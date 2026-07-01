# servidor Flask com endpoints
from flask import Flask, request, jsonify
import db
import prioritizer

app = Flask(__name__)

@app.route('/rfqs', methods=['GET'])
def listar_rfqs():
    df = db.carregar_rfqs()
    # Filtra só pendentes e aplica prioridade
    pendentes = df[df['status'] == 'pendente']
    priorizados = prioritizer.calcular_prioridade(pendentes)
    return jsonify(priorizados.to_dict(orient='records'))

@app.route('/assign', methods=['POST'])
def atribuir():
    dados = request.get_json()
    rfq_id = dados['rfq_id']
    analista_id = dados['analista_id']

    # Atualiza status do RFQ
    rfqs = db.carregar_rfqs()
    rfqs.loc[rfqs['id'] == rfq_id, 'status'] = 'atribuido'
    db.salvar_rfqs(rfqs)

    # Incrementa carga do analista
    analistas = db.carregar_analistas()
    analistas.loc[analistas['id'] == analista_id, 'carga_atual'] += 1
    db.salvar_analistas(analistas)

    return jsonify({"mensagem": "Atribuído com sucesso"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)