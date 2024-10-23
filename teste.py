import pandas as pd
import random
from datetime import datetime, timedelta

# Função para gerar uma data aleatória entre dois anos
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Definindo os limites de data
start_date = datetime(2018, 1, 1)
end_date = datetime(2023, 12, 31)

# Dicionário de cidades e estados com suas regiões
cidades_estados = {
    'Norte': [('Manaus', 'AM'), ('Belém', 'PA'), ('Rio Branco', 'AC'), ('Porto Velho', 'RO')],
    'Nordeste': [('Salvador', 'BA'), ('Fortaleza', 'CE'), ('São Luís', 'MA'), ('Recife', 'PE')],
    'Centro-Oeste': [('Brasília', 'DF'), ('Goiânia', 'GO'), ('Campo Grande', 'MS')],
    'Sudeste': [('São Paulo', 'SP'), ('Rio de Janeiro', 'RJ'), ('Belo Horizonte', 'MG'), ('Vitória', 'ES')],
    'Sul': [('Curitiba', 'PR'), ('Porto Alegre', 'RS'), ('Florianópolis', 'SC')]
}

# Criar tabela de clientes
clientes = []
for i in range(1, 5001):
    nome = f'Cliente {i}'
    sexo = random.choice(['Masculino', 'Feminino'])
    
    # Gerar idade e faixa etária
    idade = random.randint(18, 65)
    if idade <= 25:
        faixa_etaria = '18-25'
    elif idade <= 35:
        faixa_etaria = '26-35'
    elif idade <= 45:
        faixa_etaria = '36-45'
    elif idade <= 55:
        faixa_etaria = '46-55'
    else:
        faixa_etaria = '56+'
    
    renda = random.randint(2000, 10000)

    # Escolher uma região, cidade e estado aleatórios
    regiao = random.choice(list(cidades_estados.keys()))
    cidade, estado = random.choice(cidades_estados[regiao])
    
    # Níveis de escolaridade
    nivel_escolaridade = random.choice(['Fundamental', 'Médio', 'Superior', 'Pós-graduação'])
    
    clientes.append([i, nome, sexo, idade, faixa_etaria, renda, cidade, estado, regiao, nivel_escolaridade])

clientes_df = pd.DataFrame(clientes, columns=['ID do Cliente', 'Nome', 'Sexo', 'Idade', 'Faixa Etária', 'Renda Mensal', 'Cidade', 'Estado', 'Região', 'Nível de Escolaridade'])

# Criar tabela de transações
transacoes = []
for i in range(1, 10001):
    cliente_id = random.randint(1, 5000)
    data_transacao = random_date(start_date, end_date)
    valor_total = random.randint(1000, 15000)
    num_parcelas = random.randint(6, 24)
    valor_parcela = round(valor_total / num_parcelas, 2)
    taxa_juros = round(random.uniform(0, 5), 2)
    transacoes.append([i, cliente_id, data_transacao.strftime('%Y-%m-%d'), valor_total, num_parcelas, valor_parcela, taxa_juros])

transacoes_df = pd.DataFrame(transacoes, columns=['ID da Transação', 'ID do Cliente', 'Data da Transação', 'Valor Total', 'Número de Parcelas', 'Valor da Parcela', 'Taxa de Juros'])

# Criar tabela de parcelas
parcelas = []
for transacao_id in range(1, 10001):
    num_parcelas = transacoes_df.loc[transacao_id-1, 'Número de Parcelas']
    data_transacao = datetime.strptime(transacoes_df.loc[transacao_id-1, 'Data da Transação'], '%Y-%m-%d')
    
    # Inicializa um flag para controle de pagamento
    previous_paid = True

    for j in range(num_parcelas):
        data_vencimento = data_transacao + timedelta(days=(j + 1) * 30)
        
        # Aumentar a probabilidade de pagamento
        if previous_paid and random.random() < 0.7:  # 70% de chance de pagar
            status = 'Paga'
            valor_pago = transacoes_df.loc[transacao_id-1, 'Valor da Parcela']
            previous_paid = True
        else:
            status = 'Pendente' if previous_paid else 'Atrasada'
            valor_pago = 0
            previous_paid = False if status == 'Pendente' else previous_paid
        
        data_pagamento = data_vencimento if status == 'Paga' else None
        parcelas.append([len(parcelas)+1, transacao_id, data_vencimento.strftime('%Y-%m-%d'), status, valor_pago, data_pagamento])

parcelas_df = pd.DataFrame(parcelas, columns=['ID da Parcela', 'ID da Transação', 'Data de Vencimento', 'Status', 'Valor Pago', 'Data do Pagamento'])

# Salvar em CSV
clientes_df.to_csv('clientes.csv', index=False)
transacoes_df.to_csv('transacoes.csv', index=False)
parcelas_df.to_csv('parcelas.csv', index=False)
