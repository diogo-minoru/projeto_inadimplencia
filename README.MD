## Case Powe BI

Este código cria dados fictícios de clientes e crédito disponibilizado por uma instituição financeira com o objetivo de analisar a inadimplência.

### Tabelas:
Foram geradas três tabelas para compor o modelo de dados, sendo elas as tabelas de Clientes, Transações e Parcelas. As descrições de cada uma delas pode ser vista logo abaixo.

#### Clientes

* ID do Cliente: Primary Key
* Nome: Nome do cliente
* Sexo: Sexo do cliente
* Idade: Idade do cliente
* Faixa Etária: Faixa etária que o cliente pertence
* Renda Mensal: Renda mensal em reais
* Cidade: Cidade onde o cliente reside
* Estado: Estado onde o cliente reside
* Região: Região onde o cliente reside
* Nível de escolaridade: Nível de escolaridade do cliente

#### Transações
* ID da Transação: Primary Key
* ID do Cliente: Foreign Key tabela clientes
* Data da Transação: Data quando foi concedido o crédito
* Valor Total: Valor total do crédito
* Número de Parcelas: Total de parcelas que devem ser pagas
* Valor da Parcela: Valor de cada parcela
* Taxa de Juros: Juros por mês do crédito

#### Parcelas
* ID da Parcela: Primary Key
* ID da Transação: Foreign Key tabela transações
* Data de Vencimento: Data de vencimento da parcela
* Status: Status do pagamento da parcela Pago/Atrasada/Pendente
* Valor Pago: Valor pago da parcela
* Data do Pagamento: Data de pagamento da parcela