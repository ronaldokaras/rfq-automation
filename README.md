# 🤖 Automação Inteligente de RFQ – Priorização, API e RPA

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0-black)](https://flask.palletsprojects.com/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3-lightblue)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Projeto de portfólio que simula a automação do processo de Cotação (RFQ) utilizando **priorização inteligente**, uma **API REST** e um **robô (RPA)** para distribuição automática de tarefas.

---

## 📌 Objetivo

Demonstrar como tecnologias de automação e inteligência artificial podem ser integradas para otimizar o fluxo de trabalho de uma equipe de cotações:

- **IA (simulada com regras configuráveis)** → atribui uma pontuação de prioridade a cada RFQ.
- **API REST em Flask** → disponibiliza a fila priorizada e recebe comandos de atribuição.
- **Robô Python (RPA)** → consome a API, escolhe o analista mais adequado e registra a distribuição automaticamente.

---

## 🧱 Arquitetura do Sistema

```text
[ CSV de RFQs ] + [ CSV de Analistas ]
        |
        v
[ API Flask ]  <-- (porta 5000)
   |         ^
   |         |
   v         |
[ Robô RPA ] ---------> [ Atualiza status via POST ]
```

### O fluxo completo

1. Os pedidos de cotação (RFQs) e a lista de analistas são armazenados em arquivos CSV (simulando um banco de dados).
2. A API Flask expõe os RFQs pendentes com suas prioridades calculadas.
3. O robô RPA (script Python) consome a API, aplica regras de distribuição e atualiza os status.
4. Após a execução do robô, a fila de pendentes fica vazia (todos foram atribuídos), mas pode ser restaurada com um comando simples.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.9+**
- **Flask** – API REST
- **Pandas** – manipulação de dados
- **Requests** – consumo da API pelo robô
- **CSV** – banco de dados local (simulado)

---

## 📁 Estrutura do Projeto

```bash
rfq-automation/
├── data/
│   ├── rfqs.csv          # Pedidos de cotação
│   └── analysts.csv      # Analistas e suas cargas
├── src/
│   ├── api.py            # Servidor Flask (endpoints)
│   ├── db.py             # Leitura/escrita dos CSVs
│   ├── prioritizer.py    # Lógica de priorização
│   └── rpa_bot.py        # Robô de distribuição
├── reset_data.py         # Script para restaurar os dados iniciais
├── requirements.txt
└── README.md
```
---

## ⚙️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/ronaldokaras/rfq-automation.git
cd rfq-automation
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. (Recomendado) Restaure os dados originais

Sempre que quiser testar do zero, execute:

```bash
python reset_data.py
```

Isso recria os arquivos CSV com os RFQs no estado `pendente` e analistas com carga zerada.

### 4. Inicie a API

```bash
python src/api.py
```

A API estará rodando em `http://localhost:5000`. Deixe esse terminal aberto.

### 5. Execute o robô

Em outro terminal:

```bash
python src/rpa_bot.py
```

O robô irá consultar a fila, priorizar e atribuir os RFQs aos analistas disponíveis. Os arquivos CSV serão atualizados automaticamente.

---

## 📡 Endpoints da API

### `GET /rfqs`

Retorna a lista de RFQs com status `pendente`, ordenada pela prioridade calculada.

Exemplo de resposta:

```json
[
  {
    "id": 4,
    "cliente": "Cliente A",
    "valor_estimado": 5000,
    "prazo_dias": 1,
    "tipo": "Mecânico",
    "status": "pendente",
    "prioridade": 45
  },
  ...
]
```

### `POST /assign`

Atribui um RFQ a um analista.

**Body (JSON):**

```json
{
  "rfq_id": 1,
  "analista_id": 2
}
```

**Resposta de sucesso:**

```json
{
  "mensagem": "Atribuído com sucesso"
}
```

---

## 🧠 Regras de Priorização (substituíveis por modelo de IA)

- Prazo menor que 3 dias → +30 pontos
- Valor estimado acima de R$ 10.000 → +20 pontos
- Cliente VIP (Cliente A) → +15 pontos

As regras estão no arquivo `src/prioritizer.py`. Para evoluir o projeto, você pode substituir essa função por um modelo preditivo treinado com dados históricos (ex.: RandomForest) sem alterar o restante do sistema.

---

## 🔁 Entendendo o retorno vazio na API

Após a execução do robô, todos os RFQs pendentes são atribuídos. Por isso, ao acessar `GET /rfqs` você verá uma lista vazia `[]`. Esse é o comportamento esperado: a fila foi consumida.

Para testar novamente, basta rodar o script de reset:

```bash
python reset_data.py
```

E acessar novamente `http://localhost:5000/rfqs` – a lista estará completa.

---

## 📈 Possíveis Melhorias

- Utilizar um banco de dados real (SQLite, PostgreSQL).
- Implementar autenticação na API.
- Substituir regras manuais por modelo preditivo (scikit-learn).
- Criar interface web simples com Flask + Jinja2.
- Agendar o robô com cron (Linux) ou Task Scheduler (Windows).
- Adicionar testes automatizados com pytest.

---

## 🤝 Contato

Feito com 💻 por **Ronaldo Karas** – em busca de oportunidades como Desenvolvedor de Automação / RPA.

- **GitHub**: [ronaldokaras](https://github.com/ronaldokaras)
- **LinkedIn**: [Ronaldo Karas](https://linkedin.com/in/ronaldo-karas)

---

## 📄 Licença

MIT © Ronaldo Karas
```