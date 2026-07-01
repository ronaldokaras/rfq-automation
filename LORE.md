# 🤖 Automação Inteligente de RFQ – A Saga da Fila que Nunca Dorme

**Instituto Nozes & Matemática Aplicada**  
*Departamento de Automação de Processos e Distribuição Justa* 🚀📊

---

## 📜 Aviso do Juiz (ele só aparece quando a fila emperra)

> Este sistema é uma simulação de automação de cotações.  
> A priorização é feita por regras – não por inteligência artificial real (ainda).  
> O robô não vai roubar seu emprego, só vai te poupar de olhar planilhas.  
> *A automação é esperta, mas a responsabilidade é de quem aperta Enter.*

---

## 🧙‍♂️ A Origem da Automação

Era uma vez um time de analistas que passava horas classificando pedidos de cotação (RFQs) em planilhas.  
Um Membro Honorário do Instituto perguntou ao **Dragão de Óculos VR**:  
*“Não dá para fazer um robô que priorize isso e distribua automaticamente?”*  

O Dragão respondeu: *“Dá. Mas só se você criar uma API, um robô e regras que não sejam injustas.”*  

Assim nasceu o **RFQ Automation**: um sistema que transforma uma pilha de pedidos em uma fila priorizada e atribui cada um ao analista certo — tudo com poucos comandos.

---

## 🏗️ A Arquitetura por Trás da Cortina

O sistema tem três atores principais:

- **A API (Flask)** – A porta de entrada. Ela mostra a fila priorizada e recebe ordens de atribuição.
- **O Robô (RPA)** – O executor. Ele consulta a API, aplica as regras de distribuição e atualiza os status.
- **Os CSVs** – A memória do sistema. Guardam os RFQs e os analistas, como fichas de papel em uma mesa digital.

O fluxo é simples:
1. O robô pede a lista de pendentes.
2. A API calcula a prioridade com base em regras configuráveis.
3. O robô escolhe o analista com menor carga e atribui.
4. O status do RFQ muda para `atribuído`.

---

## 🎯 As Regras de Priorização (o que o Dragão escreveu)

- Prazo curto (≤3 dias) → +30 pontos – porque a urgência grita.
- Valor alto (> R$ 10.000) → +20 pontos – porque dinheiro fala mais alto.
- Cliente VIP (Cliente A) → +15 pontos – porque alguns clientes merecem tapete vermelho.

Essas regras estão no arquivo `prioritizer.py`. O Dragão as chamou de *“heurísticas de bom senso”*.  
Se um dia você quiser substituí-las por um modelo de machine learning, o sistema está preparado — basta trocar a função.

---

## 🔁 O Ciclo Infinito: Reset e Repetição

Depois que o robô roda, a fila de pendentes fica vazia.  
Isso é esperado: o trabalho foi feito.  

Mas para testar novamente, o Instituto criou um **script mágico**: `reset_data.py`.  
Ele restaura os dados originais em um piscar de olhos – como um Ctrl+Z para o mundo real.

---

## 🛡️ O Olhar do Juiz

O Juiz (a consciência do Instituto) aprovou o sistema com uma condição:  
*“Nada de decisões automáticas sem supervisão. O robô pode distribuir, mas a responsabilidade final é humana.”*  

Por isso, o sistema é transparente: a API mostra os dados, e o robô só executa o que foi programado.

---

## 🏛️ Veredito da Diretoria

A Diretoria do Instituto Nozes & Matemática Aplicada declara que o **RFQ Automation** está **aprovado** – por sua simplicidade, eficiência e potencial de evolução.  
Que ele sirva de exemplo para quem deseja automatizar processos sem perder o controle.

---

## 📄 Licença

MIT © Ronaldo Karas – compartilhe o código, mas não compartilhe os dados sensíveis.

---

**Instituto Nozes & Matemática Aplicada**  
*Departamento de Automação de Processos e Distribuição Justa*  
*Quebrando cascas duras para revelar códigos que organizam o caos.* 🚀🥜
```