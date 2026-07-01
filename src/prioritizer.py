# lógica de pontuação (simula IA)
def calcular_prioridade(df):
    df = df.copy()
    # Pontuação base zero
    df['prioridade'] = 0

    # Regra 1: Prazo menor que 3 dias → +30 pontos
    df.loc[df['prazo_dias'] < 3, 'prioridade'] += 30

    # Regra 2: Valor estimado acima de 10.000 → +20 pontos
    df.loc[df['valor_estimado'] > 10000, 'prioridade'] += 20

    # Regra 3: Cliente VIP (A) → +15 pontos
    df.loc[df['cliente'] == 'Cliente A', 'prioridade'] += 15

    # Ordena do maior para o menor
    df = df.sort_values(by='prioridade', ascending=False)
    return df